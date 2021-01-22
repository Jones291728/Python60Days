import numpy as np
#1.有多少學生英文成績比數學成績高
english_score=np.array([55,89,76,65,48,70])
match_score=np.array([60,85,60,68,55,60])
chinese_score=np.array([65,90,82,72,66,77])
compare01=np.greater_equal(english_score,match_score).sum()
print("英文成績比數學成績高,共(位)",compare01)

#2.是否全班同學最高分都是國文？
compare02=np.greater_equal(chinese_score,match_score)
compare03=np.greater_equal(chinese_score,english_score)
print("全班同學最高分都是國文",np.logical_and(compare02,compare03))