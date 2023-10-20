import pandas as pd 
  
arr = [1, 2, 3, 7, 9] 
window_size = 3
numbers_series = pd.Series(arr) 
windows = numbers_series.rolling(window_size) 
moving_averages = windows.mean() 
moving_averages_list = moving_averages.tolist() 
final_list = moving_averages_list[window_size - 1:]
print(final_list)

from statsmodels.tsa.seasonal import seasonal_decompose

result_mul = seasonal_decompose(tickerDf.Close, model='multiplicative', period=30)
deseasonalized = tickerDf.Close.values / result_mul.seasonal

plt.plot(deseasonalized)
plt.title('TATAGLOBAL deseasonalized', fontsize=16)
plt.plot()
