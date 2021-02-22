# library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics


# Case_01_使用平均數、中位數、眾數描述這男孩、女孩資料樣態
boys=[164, 176, 169, 169, 165, 175, 159, 151, 144, 160, 183, 165, 156, 170,164, 173, 165, 163, 177, 171]
girls=[169, 183, 170, 168, 182, 170, 173, 185, 151, 156, 162, 169, 162, 181,159, 154, 167, 175, 170, 160]

# Case_02_男生和女生在平均身高上誰比較高？
# Case_03_請問第二題的答案和日常生活中觀察的一致嗎？如果不一致，你覺得原因可能為何？
# 統計量_平均數
statistics_mean_boy=statistics.mean(boys)
print("statistics_mean_boy=",statistics_mean_boy)
statistics_mean_girl=statistics.mean(girls)
print("statistics_mean_girl=",statistics_mean_girl)
print("女孩平均身高高於男孩")
print("抽的樣本數量不夠多，導致看起來和現實中有誤差，或是紀錄上得誤差")

# 統計量_中位數
statistics_median_boy=statistics.median(boys)
print("statistics_median_boy=",statistics_median_boy)
statistics_median_girl=statistics.median(girls)
print("statistics_median_girl=",statistics_median_girl)

# 統計量_眾數
statistics_mode_boy=statistics.mode(boys)
print("statistics_mode_boy=",statistics_mode_boy)
statistics_mode_girl=statistics.mode(girls)
print("statistics_mode_girl=",statistics_mode_girl)

#全距(rangeV=max(boys)-min(boys))
def rangeV(x): 
  return(max(x)-min(x))    
print("男孩身高全距=",rangeV(boys))
print("女孩身高全距=",rangeV(girls))

# 計算_變異數
print("男孩身高變異數=",statistics.variance(boys))
print("女孩身高變異數=",statistics.variance(girls))

# 統計量_標準差
statistics_stdev_boy=statistics.stdev(boys)
print("statistics_stdev_boy=",statistics_stdev_boy)
statistics_stdev_girl=statistics.stdev(girls)
print("statistics_stdev_girl=",statistics_stdev_girl)

# 百分位數(stats)
print("男孩90百分位數=",stats.scoreatpercentile(boys, 90))
print("女孩90百分位數=",stats.scoreatpercentile(girls, 90))

#分布型態_偏度和峰度
print("男孩偏度=",stats.skew(boys))
print("男孩峰度=",stats.kurtosis(boys))
print("女孩偏度=",stats.skew(girls))
print("女孩峰度=",stats.kurtosis(girls))

#畫圖看分布
plt.hist(boys,alpha=.4,bins=40)
plt.title('boy,skewness={0},kurtosis={1}'.format(round(stats.skew(boys),2),round(stats.kurtosis(boys),2)))
plt.axvline(x=statistics_mean_boy)
plt.show()
plt.hist(boys,alpha=.4,bins=40)
plt.title('girl,skewness={0},kurtosis={1}'.format(round(stats.skew(girls),2),round(stats.kurtosis(girls),2)))
plt.axvline(x=statistics_mean_girl)
plt.show()