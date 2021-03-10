# 把需要的 library import 進來
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df_train = pd.read_csv("Titanic_train.csv")
df_test = pd.read_csv("Titanic_test.csv")

# # Case01_觀察測試(test) 資料集和訓練(Train) 資料集的變數的差異性？
# df_train.info()
# df_test.info()
# print("Test資料缺少Survived欄位")

# # Case02_測試資料集是否有遺失值? 
# print("有缺資料的欄位分別為:Age,Fare,Cabin:\n",df_test.isnull().any())

# Case03_從合併資料選取一個變數，嘗試去做各種不同遺失值的處理，並透過圖形來做輔助判斷，補值前與後的差異，你覺得以這個變數而言，試著說明每一個方法的差異。
df_combined = pd.concat([df_train,df_test],axis=0, ignore_index=True)
# 觀看欄位(Cabin)資料特徵
print(df_combined["Cabin"].value_counts())
# Cabin欄位值(nan)以(NoCabin)取代
df_combined["Cabin"] = df_combined['Cabin'].apply(lambda x : str(x)[0] if not pd.isnull(x) else 'NoCabin')
# 印出欄位(Cabin)新的資料特徵
print(df_combined["Cabin"].value_counts())
# 連續型用分布圖行來看(Cabin V.S. Survived)
ax=sns.countplot(df_combined['Cabin'],hue=df_combined['Survived'])
plt.show()
# 連續型用分布圖行來看(Cabin V.S. Sex)
ax=sns.countplot(df_combined['Cabin'],hue=df_combined['Sex'])
plt.show()
# 數值計算
df_combined[['Cabin', 'Sex']].groupby(['Cabin'], as_index=False).mean().sort_values(by='Sex', ascending=False)
# 進行 NoCabin 補 F
# 連續型用分布圖行來看
print(df_combined["Cabin"].value_counts())
ax=sns.countplot(df_combined['Cabin'], hue=df_combined['Sex'])
plt.show()