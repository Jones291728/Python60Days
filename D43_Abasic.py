# 載入所需要的套件
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.stats.api as sms
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from math import ceil

# Some plot styling preferences
plt.style.use('seaborn-whitegrid')
font = {'family' : 'Helvetica',
        'weight' : 'bold',
        'size'   : 14}

mpl.rc('font', **font)

# Calculating effect size based on our expected rates
effect_size = sms.proportion_effectsize(0.13, 0.15)
required_n = sms.NormalIndPower().solve_power(
    effect_size, 
    power=0.8, 
    alpha=0.05, 
    ratio=1
    )                                                 
# Calculating sample size needed
required_n = ceil(required_n)                                                 
# Rounding up to next whole number  
# print(required_n)

#展示實驗資料
df = pd.read_csv('ab_data.csv')
# To make sure all the control group are seeing the old page and viceversa
# 用 crosstab 將 landing_page 當作 column，group 當作 row
# df=pd.crosstab(df['group'], df['landing_page'])

#偵測重複出現使用者
session_counts = df['user_id'].value_counts(ascending=False)
multi_users = session_counts[session_counts > 1].count()
# print(f'There are {multi_users} users that appear multiple times in the dataset')

#除去重複出現使用者
users_to_drop = session_counts[session_counts > 1].index
df = df[~df['user_id'].isin(users_to_drop)]
# print(f'The updated dataset now has {df.shape[0]} entries')

# 選取 控制組和實驗組各半 4720 * 2 = 9440
control_sample = df[df['group'] == 'control'].sample(n=required_n, random_state=22)
treatment_sample = df[df['group'] == 'treatment'].sample(n=required_n, random_state=22)
ab_test = pd.concat([control_sample, treatment_sample], axis=0)
ab_test.reset_index(drop=True, inplace=True)
# print(ab_test)

# 確認 ab_test 控制組實驗組各半
ab_test['group'].value_counts()

# 計算conversion rate 平均值，標準差，標準誤
conversion_rates = ab_test.groupby('group')['converted']
# Std. deviation of the proportion
std_p = lambda x: np.std(x, ddof=0)
# Std. error of the proportion (std / sqrt(n))             
se_p = lambda x: stats.sem(x, ddof=0)           
conversion_rates = conversion_rates.agg([np.mean, std_p, se_p])
conversion_rates.columns = ['conversion_rate', 'std_deviation', 'std_error']
# print(conversion_rates.style.format('{:.3f}'))

#繪出 conversion rate 棒狀圖
plt.figure(figsize=(8,6))
sns.barplot(x=ab_test['group'], y=ab_test['converted'], ci=False)
plt.ylim(0, 0.17)
plt.title('Conversion rate by group', pad=20)
plt.xlabel('Group', labelpad=15)
plt.ylabel('Converted (proportion)', labelpad=15);
# plt.show()

#以函數計算z_stat, pval, confidence interval
from statsmodels.stats.proportion import proportions_ztest, proportion_confint
control_results = ab_test[ab_test['group'] == 'control']['converted']
treatment_results = ab_test[ab_test['group'] == 'treatment']['converted']
n_con = control_results.count()
n_treat = treatment_results.count()
successes = [control_results.sum(), treatment_results.sum()]
nobs = [n_con, n_treat]
z_stat, pval = proportions_ztest(successes, nobs=nobs)
(lower_con, lower_treat), (upper_con, upper_treat) = proportion_confint(successes, nobs=nobs, alpha=0.05)
# print(f'z statistic: {z_stat:.2f}')
# print(f'p-value: {pval:.3f}')
# print(f'ci 95% for control group: [{lower_con:.3f}, {upper_con:.3f}]')
# print(f'ci 95% for treatment group: [{lower_treat:.3f}, {upper_treat:.3f}]')

# Case01_判讀程式最後統計結果，A/B test 是否顯著
# print("p-value大於0.05，效果不顯著")

#Case02_試以(0.12, 0.11)計算結果是否顯著
Data=pd.read_csv('ab_data.csv')
# print(Data.info())
# print(Data.head(10))
print(Data['user_id'].value_counts())
#Calculating effect size based on our expected rates
effect_size = sms.proportion_effectsize(0.12, 0.11)
required_n = sms.NormalIndPower().solve_power(effect_size,power=0.8,alpha=0.05,ratio=1)                                                 
# Calculating sample size needed
required_n = ceil(required_n)                                                 
# Rounding up to next whole number  
print(required_n)
Data=Data.drop_duplicates(subset=['user_id'],keep=False)
control_sample = Data[Data['group'] == 'control'].sample(n=required_n, random_state=22)
treatment_sample = Data[Data['group'] == 'treatment'].sample(n=required_n, random_state=22)
ab_test = pd.concat([control_sample, treatment_sample], axis=0)
ab_test.reset_index(drop=True, inplace=True)
print(ab_test)

#以函數計算z_stat, pval, confidence interval
from statsmodels.stats.proportion import proportions_ztest, proportion_confint
control_results = ab_test[ab_test['group'] == 'control']['converted']
treatment_results = ab_test[ab_test['group'] == 'treatment']['converted']
n_con = control_results.count()
n_treat = treatment_results.count()
successes = [control_results.sum(), treatment_results.sum()]
nobs = [n_con, n_treat]
z_stat, pval = proportions_ztest(successes, nobs=nobs)
(lower_con, lower_treat), (upper_con, upper_treat) = proportion_confint(successes, nobs=nobs, alpha=0.05)
print(f'z statistic: {z_stat:.2f}')
print(f'p-value: {pval:.3f}')
print(f'ci 95% for control group: [{lower_con:.3f}, {upper_con:.3f}]')
print(f'ci 95% for treatment group: [{lower_treat:.3f}, {upper_treat:.3f}]')
print("效果不顯著")

# Case03_樣本數是以那些模組/函數算的
print("模組_import statsmodels.stats.api as sms")
print("函數01_effect_size = sms.proportion_effectsize")
print("函數02_required_n = sms.NormalIndPower().solve_power(effect_size,power,alpha,ratio") 