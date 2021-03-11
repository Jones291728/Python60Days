# library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns
from IPython.display import display
import sklearn
from sklearn import preprocessing
df_train = pd.read_csv("Titanic_train.csv")

# 計算每一行是否有遺失值，計算遺失比例
missing_vals = df_train.isnull().sum()/len(df_train)
missing_vals.sort_values(ascending=False)
missing_vals = pd.DataFrame(missing_vals,columns=['missing_rate'])
print(missing_vals)


# # Case01-1_觀察 Age 和 Pclass是否有關連性?
g = sns.FacetGrid(df_train, col="Pclass", height=5, aspect=.75)
g.map(sns.histplot, "Age")
plt.show()
print("Age 和 Pclass 關連性較高,特別是在Pclass=3")

# # Case01-2_觀察 Age 和 Sex 是否有關連性?
g = sns.FacetGrid(df_train, col="Sex", height=5, aspect=.75)
g.map(sns.histplot, "Age")
plt.show()
print("Age 和 Sex 關連性較低,但在Sex=male還是看得出來")

ori_data=df_train[['Sex', 'Age',"Pclass"]]
data=ori_data.copy() #複製一份資料給 data
# ValueError: could not convert string to float: 'Male', sklearn 中的 KNN 只能處理數值型態
# 轉型(使用preprocessing 轉換)
# 下面兩行程式，讓 Male=1, FeMale-0.
le = preprocessing.LabelEncoder()
data['Sex']=le.fit_transform(data['Sex'])
from sklearn.metrics.pairwise import nan_euclidean_distances

# KNN(設定 k 值)
value_neighbors=1
from sklearn.impute import KNNImputer
# 初始化: Initialize KNNImputer
imputer = KNNImputer(n_neighbors=value_neighbors)
df_filled = pd.DataFrame(imputer.fit_transform(data))
df_filled.columns = ['Sex', 'Age',"Pclass"]
print(df_filled)


# 參考資料(KNN補值的Python語法)
# Step01_離散轉連續型資料
# Step02_計算資料點的倆倆距離
# Step03_透過 KNN 進行補值


