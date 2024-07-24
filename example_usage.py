from my_package.metrics_analyzer import MetricsAnalyzer

# 사용 예시
folder_path = './data'
analyzer = MetricsAnalyzer(folder_path, sigma_multiplier=2, top_k=1)
combined_metrics_df = analyzer.calculate_all_metrics()

print(combined_metrics_df)
