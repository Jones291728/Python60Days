# 1.6號學生(student_id=6)3科平均分數為何？
import pandas as pd
score_df = pd.DataFrame([[1, 56, 66, 70], [2, 90, 45, 34], [3, 45, 32, 55], [4, 70, 77, 89], [5,56,80,70], [6,60,54,55], [7,45,70,79], [8,34,77,76], [9,25,87,60], [10,88,40,43]],
                        columns=["student_id", "math_score", "english_score", "chinese_score"])
# 將student_id設定成index
score_df = score_df.set_index('student_id')
student06=score_df.loc[6]
print("6號學生3科原始平均分數為:",student06.mean().round(decimals=2))
# 2.6號學生3科平均分數是否有贏過班上一半的同學？
score_df["average"] = score_df.mean(axis=1)
allstudents=score_df["average"].median()
if student06.mean() > allstudents:
     print ("6號學生平均贏過了全班一半的同學")
else:
     print ("6號學生平均沒贏過了全班一半的同學")
# 3.由於班上同學成績不好，所以學校統一加分，加分方式為開根號乘以十，請問 6 號同學 3 科成績分別是？
newscore=score_df.apply(lambda x : x**(0.5)*10)
newstudent06=newscore.loc[6]
print("6號同學3科新成績:\n",newstudent06.astype(int))
# 4.承上題，加分後各科班平均變多少？
print("全班3科新的平均:\n",newscore.mean().round(decimals=2))