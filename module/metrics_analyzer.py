import os
import glob
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
from scipy.signal import find_peaks, peak_prominences, peak_widths

def load_data(file_path):
    return pd.read_csv(file_path)

def list_csv_files(folder_path):
    return sorted(glob.glob(os.path.join(folder_path, '*.csv')))

def calculate_std_deviation_metrics(file_path):
    data = load_data(file_path)
    flat_data = data.values.flatten()
    
    std_dev = np.std(flat_data)
    max_value = np.max(flat_data)
    rms = np.sqrt(np.mean(np.square(flat_data)))
    mean_value = np.mean(flat_data)
    
    crest_factor = max_value / rms if rms != 0 else np.nan
    impact_factor = max_value / mean_value if mean_value != 0 else np.nan
    shape_factor = rms / mean_value if mean_value != 0 else np.nan

    return {
        'File Name': os.path.basename(file_path),
        'Standard Deviation': std_dev,
        'Crest Factor': crest_factor,
        'Impact Factor': impact_factor,
        'Shape Factor': shape_factor
    }

def calculate_peak_metrics(file_path, sigma_multiplier, top_k):
    data = load_data(file_path)
    filename = os.path.basename(file_path)
    
    mean = data.mean().mean()
    sigma = np.std(data.values)
    upper_limit = mean + sigma_multiplier * sigma
    lower_limit = mean - sigma_multiplier * sigma
    
    anomalies = data[(data < lower_limit) | (data > upper_limit)].dropna()
    if anomalies.empty:
        return {'File Name': filename, 'Max Peak Width': 0, 'Peak Prominence Count': 0}

    anomaly_indices = anomalies.index
    file_peak_widths = []

    for start_idx, end_idx in zip(anomaly_indices[:-1], anomaly_indices[1:]):
        section_data = data.iloc[start_idx:end_idx].values.flatten()
        peaks, _ = find_peaks(section_data)
        results_full = peak_widths(section_data, peaks, rel_height=0.5)
        widths = results_full[0]

        file_peak_widths.extend(widths)

    top_widths = sorted(file_peak_widths, reverse=True)[:top_k]
    max_peak_width = np.mean(top_widths) if top_widths else 0

    flat_data = data.values.flatten()
    all_peaks, _ = find_peaks(flat_data)
    if len(all_peaks) > 0:
        prominences = peak_prominences(flat_data, all_peaks)[0]
        prominences = prominences[prominences > 0]
        peak_prominence_count = np.sum(prominences >= 40)
    else:
        peak_prominence_count = 0

    return {
        'File Name': filename,
        'Max Peak Width': max_peak_width,
        'Peak Prominence Count': peak_prominence_count
    }

def calculate_skewness_kurtosis(file_path):
    data = load_data(file_path)
    flat_data = data.values.flatten()
    
    data_skewness = skew(flat_data)
    data_kurtosis = kurtosis(flat_data)
    
    return {
        'File Name': os.path.basename(file_path),
        'Skewness': data_skewness,
        'Kurtosis': data_kurtosis
    }

class MetricsAnalyzer:
    def __init__(self, folder_path, sigma_multiplier=2, top_k=1):
        self.folder_path = folder_path
        self.sigma_multiplier = sigma_multiplier
        self.top_k = top_k

    def calculate_all_metrics(self):
        csv_files = list_csv_files(self.folder_path)
        
        std_dev_metrics = [calculate_std_deviation_metrics(file) for file in csv_files]
        peak_metrics = [calculate_peak_metrics(file, self.sigma_multiplier, self.top_k) for file in csv_files]
        skewness_kurtosis_metrics = [calculate_skewness_kurtosis(file) for file in csv_files]
        
        std_dev_df = pd.DataFrame(std_dev_metrics)
        peak_df = pd.DataFrame(peak_metrics)
        skewness_kurtosis_df = pd.DataFrame(skewness_kurtosis_metrics)
        
        combined_df = std_dev_df.merge(peak_df, on='File Name').merge(skewness_kurtosis_df, on='File Name')
        
        return combined_df
