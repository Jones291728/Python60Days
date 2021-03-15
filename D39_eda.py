# library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns
import sklearn
from sklearn import preprocessing
import researchpy

# 讀入資料 & 整理資料
df_train = pd.read_csv("Titanic_train.csv")
df_train["Survived_cate"]=df_train["Survived"].astype(object)
df_train=df_train[["Age","Sex","Survived_cate"]].dropna()

# # Case01_產生一個新的變數(Ageabove65) Age>=65為 'Y'，其餘為'N'
df_train["Age_above65"]=df_train["Age"].apply(lambda x : "Y" if x>=65 else "N")
print("變數_Ageabove65\n",df_train)


#Case02_添加女性和男性，產生一個新的變數(Age_above65_female)，女性或Age>=65為'Y'，其餘為'N'
def age_female (row):
    if (row.Sex == "female"):
        return ("Y")
    else:
        if (row.Age>=65):
          return ("Y")
        else:
          return ("N")
df_train["Age_above65_female"]=df_train[["Age","Sex"]].apply(age_female,axis=1)
print("變數_Ageabove65_female\n",df_train)


# Case03_透過昨天課程的內容，驗證產生的兩個新變數，哪一個和目標變數(Survived_cate) 的相關性較高？
# Survived_cate 和 兩變數(Age_above65、Age_above65_female)關係都是離散vs離散,因此採用Cramer’s V 係數
le = preprocessing.LabelEncoder()
df_train['Age_above65']=le.fit_transform(df_train['Age_above65'])
above65_table = pd.crosstab(df_train["Age_above65"], df_train['Survived_cate'])
df_above65_table= min(above65_table.shape[0], above65_table.shape[1]) - 1
above65_table, res_above65 = researchpy.crosstab(df_train["Age_above65"], df_train['Survived_cate'], test='chi-square')

df_train['Age_above65_female']=le.fit_transform(df_train['Age_above65_female'])
above65_female_table = pd.crosstab(df_train["Age_above65_female"], df_train['Survived_cate'])
df_above65_female_table = min(above65_female_table.shape[0], above65_female_table.shape[1]) - 1
above65_female_table, res_above65_female= researchpy.crosstab(df_train["Age_above65_female"], df_train['Survived_cate'], test='chi-square')

res={}
res["Survived_vs_Age_above65"]=[df_above65_table,res_above65.loc[2,'results']]
res["Survived_vs_Age_above65_female"]=[df_above65_female_table,res_above65_female.loc[2,'results']]

df_res=pd.DataFrame(data=res,index=["d.f","Cramer’s V coefficient"])
df_res.columns=['Age_above65','Age_above65_female']
print("Age_above65_female 和 survived_cate的相關性較高\n",df_res)