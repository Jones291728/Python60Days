import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import keras
import tensorflow as tf

# 利用 PANDAS 取得酒的品質資料 
df_red = pd.read_csv("winequality_red.csv")
df_white = pd.read_csv("winequality_white.csv")

# 資料整理
df_red["color"] = "R"
df_white["color"] = "W"

# 整合紅酒與白酒的資料
df_all=pd.concat([df_red,df_white],axis=0)
# 檢查合併後的資料集
# print(df_all.head())
df_all.rename(columns={'fixed acidity': 'fixed_acidity','citric acid':'citric_acid',
                       'volatile acidity':'volatile_acidity','residual sugar':'residual_sugar',
                       'free sulfur dioxide':'free_sulfur_dioxide',
                       'total sulfur dioxide':'total_sulfur_dioxide'}, inplace=True)
# 檢查合併後的資料集
# print(df_all.head(10))

# 處理缺失值
df = pd.get_dummies(df_all, columns=["color"])
df_all.isnull().sum()

# 要瞭解數據集的統計摘要,即記錄數、平均值、標準差、最小值和最大值,我們使用描述()。
# print(df_all.describe())

# 可視化所有數值數據。在垂直軸上計數,在水平軸上使用值範圍。hist 函數通過將所有屬性繪製在一起使操作變得簡單。
df_all.hist(bins=10, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=False)
plt.tight_layout(rect=(0, 0, 1.2, 1.2))
plt.show()

# 聯合圖用於顯示兩個變數之間的關係。您可以選擇從 5 個選項中繪製的繪圖種類 - 散點、reg、十六進位、kde、resid。下面我展示了三個使用線性回歸線('reg'的例子)
# 第一個示例"檸檬酸"和"固定酸度"具有正相關關係,因此圖形是向上的。然而,硫酸鹽和酒精的變數是相關的。因此,線性回歸線幾乎是平的。具有"揮發性酸度"和"檸檬酸"屬性的示例具有負相關性,因此圖呈向下。
# Plotting Jointplot, 使用 'reg'== regression 回歸線繪製關係圖
a = sns.jointplot("fixed_acidity","citric_acid",data = df_all,kind ='reg', color = None)
b = sns.jointplot("alcohol", "citric_acid", data = df_all, kind = 'reg')
c = sns.jointplot("volatile_acidity", "citric_acid", data = df_all, kind = 'reg')
plt.show()

# Swarm沿分類軸(質量)調整記錄。這種繪圖將記錄分別標記,而不會重疊。這就是為什麼它最適合小型數據集的原因。在此圖表中,您可以看到硫酸鹽的數量,根據品質。品質值為 6 的硫酸鹽密度最高,品質等級為 9 和 3 的最低
sns.catplot(x="quality", y="pH", kind="swarm", data=df_all)
plt.show()
# PairGrid 允許我們使用相同的繪圖類型繪製子圖網格來可視化數據。與 FacetGrid 不同,它在每個子圖使用不同的變數對。它形成子圖的矩陣。它有時也被稱為"散點圖矩陣"。對網格的用法與分面網格類似。首先初始化網格,然後傳遞繪圖函數。
# #設定底圖樣式

# 利用PairGrid 繪製對角圖
sns.set(style="white")
g = sns.pairplot(df_all)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot, colors="C0")
g.map_diag(sns.kdeplot, lw=2)
plt.show()
