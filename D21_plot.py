# 導入必要的程式庫
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("titanic")
sns.set_style("darkgrid")
# 直接使用PANDAS dataframe, 當作參數
# 條形圖()顯示分類變數和連續變數之間的關係。數據以矩形條表示,其中條的長度表示該類別中數據的比例。
ax = sns.barplot(x="sex", y="survived", hue="class", data=df) 
plt.show() 

# 瞭解性別在各艙等的分布的存活率
g = sns.FacetGrid(df, col="survived")
g = g.map(plt.hist,"sex")
plt.show()
# 使用survived_counts.plot做對照組
survived_counts = pd.crosstab([df.pclass, df.sex],df.survived)
survived_counts.plot(kind="bar",stacked=True)
plt.show()
sns.violinplot(data=survived_counts)
plt.show()

g = sns.FacetGrid(df, col="survived")
g = g.map(plt.hist,"pclass")
plt.show()
h = sns.FacetGrid(df, col="survived")
h = h.map(plt.hist,"sex")
plt.show()