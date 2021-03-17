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

# 特徵選取會用到的函數
from sklearn.feature_selection import VarianceThreshold
from sklearn import preprocessing

from sklearn.datasets import make_friedman1
from sklearn.feature_selection import RFE
from sklearn.svm import SVC

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
# 運用 python 執行包裝法
df_train = pd.read_csv("Titanic_train.csv")
df_train['Survived_cate']=df_train['Survived']
df_train['Survived_cate']=df_train['Survived_cate'].astype('object')
df_train=df_train.dropna()
df_train=df_train.drop(columns=['Name','Ticket','PassengerId'])

# Step 1：sex、 Embarked離散型要先轉成數值型態
sex_mapping = {
           'male': 1,
           'female': 0}
df_train['Sex'] = df_train['Sex'].map(sex_mapping)
embarked_mapping = {
    'C': 0,
    'Q': 1,
    'S': 2}
df_train['Embarked'] = df_train['Embarked'].map(embarked_mapping)
# 定義 X,Y
x=df_train[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare','Sex', 'Embarked']]
y=df_train['Survived']
# Step 2：目標變量是離散，來決定判斷的準則。
estimator = SVC(kernel="linear")
# Step 3：設定 RFE 裡面的參數(n_features_to_select：最後要選擇留下多少特徵,Step：刪除法，每一部刪除多少特徵)
selector = RFE(estimator, n_features_to_select=1, step=1)
# Step 4：.fit(x.y)：每一步都依不同的特徵組合建立模型，判斷最終要選擇那些特徵
selector = selector.fit(x, y)
# Step 5：透過 support_ 呈現包裝法搭配 SVC 下，選擇最好的特徵，用 True 來表示(True= selected feature)
print(selector.support_)
# Selected (i.e., estimated best) features are assigned rank 1.
ranking=selector.ranking_
print(ranking)
rfe_feature = x.loc[:,selector.support_].columns.tolist()
print(rfe_feature)

# 參考資料(卡方檢定-獨立性檢定_The Chi-Squared Test of Independence_統計說明與SPSS操作)
# https://www.youtube.com/watch?v=MgKL8ax_Oik