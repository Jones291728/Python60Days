# 把需要的 library import 進來
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn  as sns
from scipy import stats
import math
import statistics
df_train = pd.read_csv("Titanic_train.csv")


# # Case01_進行一個描述性的統計（規定範圍），從而檢視哪些值是不合理的（範圍以外的值）
# #先透過計算統計值， 分別呈現數量，票價平均，標準差，最大值和最小值。
print(df_train['Fare'].describe())
print("經計算後,票價介於最低0 ~ 最高 512")

# # Case01-1_進行3倍標準差原則的計算，從而檢視哪些值是可疑的異常值。
# # 創建一個函數，計算在這個資料中， ys:資料，times : 幾倍標準差，找出在這樣條件下的異常值。
def outliers_z_score(ys,times):
    mean_y = np.mean(ys)
    stdev_y = np.std(ys)
    z_scores = [(y - mean_y) / stdev_y for y in ys]
    return np.where(np.abs(z_scores) > times)

out_index=outliers_z_score(df_train['Fare'],3)
print(out_index[0])
print("用第二種方法的找出的 outlier 有哪些?")
print(df_train.loc[out_index[0],'Fare'])

# # Case01-2_盒鬚圖判別法(IQR method)
def outliers_iqr(ys,times):
    #注意使用 np.percentile 要去除 nan 要不然計算出來會錯誤，所以我們採用下者的程式 np.nanpercentile
    #quartile_1, quartile_3 = np.percentile(ys, [25, 75])
    quartile_1, quartile_3 = np.nanpercentile(ys, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * times)
    upper_bound = quartile_3 + (iqr * times)
    return np.where((ys > upper_bound) | (ys < lower_bound))

out_index2=outliers_iqr(df_train['Fare'],1.5)
print(out_index2)
print("用第三種方法的找出的 outlier 有哪些?(1.5 倍IQR)")
print(df_train.loc[out_index2[0],'Fare'])

# Case01-3_畫盒鬚圖
# 利用matplotlib包中axes物件的boxplot()方法並透過 whis 來設定 IQR 的倍數
# 使用np.isnana(data)，找出在Fare中的遺失值，然後逐位反轉，讓遺失值為 0,則可以透過索引的方式，濾掉遺失值。
plt.boxplot(df_train['Fare'][~np.isnan(df_train['Fare'])],whis=1.5)
plt.title('Box Plot')
plt.show()

#Case02_你覺得找出的異常是真的異常?你覺得需要做處理嗎?
print("異常的數目多的話就要進行處理,個數少的話則不用")