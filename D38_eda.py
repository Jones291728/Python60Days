# import library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns
from IPython.display import display
import pingouin as pg
import researchpy
# 將有遺失值的數值刪除,同時產生一個新的變數 Survived_cate，資料型態傳換成類別型態
df_train = pd.read_csv("Titanic_train.csv")
df_train["Survived_cate"]=df_train["Survived"].astype(object)
df_train=df_train[["Age","Survived_cate","Sex","Fare"]].dropna()


# Case01_透過數值法計算 Age 和 Survived_cate 是否有相關性?
aov = pg.anova(dv='Age', between='Survived_cate', data=df_train, detailed=True)
etaSq = aov.SS[0] / (aov.SS[0] + aov.SS[1])
def judgment_etaSq(etaSq):
    if etaSq < .01:
        qual = 'Negligible'
    elif etaSq < .06:
        qual = 'Small'
    elif etaSq < .14:
        qual = 'Medium'
    else:
        qual = 'Large'
    return(qual)
print(" Age 和 Survived 是否有相關性?",judgment_etaSq(etaSq))

# Case02_透過數值法計算 Sex 和 Survived_cate 是否有相關性?
contTable = pd.crosstab(df_train['Sex'], df_train['Survived_cate'])
print(contTable)
df = min(contTable.shape[0], contTable.shape[1]) - 1
crosstab, res = researchpy.crosstab(df_train['Sex'], df_train['Survived_cate'], test='chi-square')
print("Cramer's value is",res.loc[2,'results'])
## 寫一個副程式判斷相關性的強度
def judgment_CramerV(df,V):
    if df == 1:
        if V < 0.10:
            qual = 'negligible'
        elif V < 0.30:
            qual = 'small'
        elif V < 0.50:
            qual = 'medium'
        else:
            qual = 'large'
    elif df == 2:
        if V < 0.07:
            qual = 'negligible'
        elif V < 0.21:
            qual = 'small'
        elif V < 0.35:
            qual = 'medium'
        else:
            qual = 'large'
    elif df == 3:
        if V < 0.06:
            qual = 'negligible'
        elif V < 0.17:
            qual = 'small'
        elif V < 0.29:
            qual = 'medium'
        else:
            qual = 'large'
    elif df == 4:
        if V < 0.05:
            qual = 'negligible'
        elif V < 0.15:
            qual = 'small'
        elif V < 0.25:
            qual = 'medium'
        else:
            qual = 'large'
    else:
        if V < 0.05:
            qual = 'negligible'
        elif V < 0.13:
            qual = 'small'
        elif V < 0.22:
            qual = 'medium'
        else:
            qual = 'large'
    return(qual)
print(judgment_CramerV(df,res.loc[2,'results']))

# Case03_透過數值法計算  Age 和 Fare 是否有相關性?
corr, _=stats.pearsonr(df_train['Age'], df_train['Fare'])
print(corr)
def judgment_corr(corr):
    if corr < .1:
        qual = 'Not Relative'
    elif corr < 0.4:
        qual = 'Low Relative'
    elif corr < 0.7:
        qual = 'Medium Relative'
    elif corr < 1:
        qual = 'High Relative'
    else:
        qual = 'Total Relative'
    return(qual)
print(judgment_corr(corr))

# 參考資料(卡方檢定-獨立性檢定的原理)
# Step01_若能符合分配的要求,[觀察值]與[期望值]比較就不應差距太多,卡方值也不會太大而落入拒絕域
# Step02_卡方檢定屬右尾檢定
# Step03_卡方檢定屬無母數分析技巧
# Step04_每個儲存格數量不可低於5,若低於5要與旁邊儲存格合併
# https://www.youtube.com/watch?v=4G_P29jZuy4


