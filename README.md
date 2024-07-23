# battery_peak_analysis
### This code provides useful peak-based statistics. Statistic captures sudden peak, or Outlier point. 
  Input: csv files. (Univariate time-series data)
  Output : Statistics
	
  Type of Statistics💡 
  1.  Max Peak Width (Top = k(1))
  2.  Number of prominence Peak (t > 40)
  3.  Number of outlier from UCL, LCL(sigma multiplier = 3, (6 sigma))
  4.  Crest Factor
  5.  Shape Factor
  6.  Impact Factor

  Example dataset included : battery-pack acceleration data
