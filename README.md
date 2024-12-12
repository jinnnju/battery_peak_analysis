# Battery Peak Analysis

This repository provides tools for analyzing univariate time-series data using peak-based statistics. These statistics are useful for identifying sudden peaks, outliers, and unusual patterns in the data.

## Features

### Input and Output
- **Input**: CSV files (univariate time-series data)
- **Output**: Statistical analysis results

---

## 📊 Statistics Provided

1. **Max Peak Width**  
   - Top \( k(1) \)

2. **Number of Prominent Peaks**  
   - Peaks where \( t > 40 \)

3. **Number of Outliers**  
   - Determined by Upper Control Limit (UCL) and Lower Control Limit (LCL)  
   - Sigma multiplier: \( 3 \) (6 sigma method)

4. **Crest Factor**

5. **Shape Factor**

6. **Impact Factor**

Example dataset included: **Battery-pack acceleration data**

---

## 🔧 Filters Provided

This repository also includes filters to amplify peaks or eliminate trivial noise and outliers:

1. **Exponential Filter**  
   - Normalized with mean

2. **Butterworth Filter**

3. **Moving Average Filter**

4. **Chebyshev Filter**

5. **Elliptic Filter**

---

## Example Dataset

The repository includes a sample dataset of **battery-pack acceleration data** to demonstrate the functionality of the provided statistics and filters.

---

Feel free to contribute or use the provided tools for your time-series analysis needs!

