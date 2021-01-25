import numpy as np
#1.請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略？
english_score=np.array([55,89,76,65,48,70])
match_score=np.array([60,85,60,68,np.nan,60])
chinese_score=np.array([65,90,82,72,66,77])

print("英文平均",np.average(english_score))
print("英文最大值",np.max(english_score))
print("英文最小值",np.min(english_score))
print("英文標準差",np.std(english_score))

print("數學平均",np.nanmean(match_score))
print("數學最大值",np.nanmax(match_score))
print("數學最小值",np.nanmin(match_score))
print("數學標準差",np.nanstd(match_score))

print("中文平均",np.average(chinese_score))
print("中文最大值",np.max(chinese_score))
print("中文最小值",np.min(chinese_score))
print("中文標準差",np.std(chinese_score))
#2.計算補考後數學成績平均、最大值、最小值、標準差？
New_match=np.array([60,85,60,68,55,60])
print("補考後數學平均",np.average(New_match))
print("補考後數學最大值",np.max(New_match))
print("補考後數學最小值",np.min(New_match))
print("補考後數學標準差",np.std(New_match))
#3.用補考後資料找出與國文成績相關係數最高的學科？
comparenglish=np.corrcoef(chinese_score,english_score)
print("英文與國文相關係數較高 \n",comparenglish)
comparematch=np.corrcoef(chinese_score,New_match)
print("數學與國文相關係數較低 \n",comparematch)