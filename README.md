# battery_peak_analysis
### This git provides useful peak-based statistics to time-series. This captures 6 statistics, which can help finding sudden peak, outlier point, unusual patterns. 
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
### Here also provides filter which amplifies peak or eliminate trivial noises or outlier.
 Type of Filter💡 
  1.  exponential filter(normalize with mean)
  2.  Butterworth filter
  3.  Moving average filter
  4.  Chebyshev filter
  5.  Elliptic filter
 
