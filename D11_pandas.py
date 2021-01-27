#1.將以下問卷資料的職業(Profession)欄位缺失值填入字串"others"
import pandas as pd
q_df = pd.DataFrame([
              ['male', 'teacher'], 
              ['male', 'engineer'],
              ['female', None],
              ['female', 'engineer']],
              columns=['Sex','Profession'])
q_df.fillna(value="others",inplace=True)
print("修改後資料:\n",q_df)
#2.將字串做編碼。 此時用什麼方式做編碼比較適合？為什麼？
general=pd.get_dummies(q_df[["Profession"]])
results=pd.concat([q_df,general],axis=1)
print("類別之間沒有順序關係,因此使用get_dummies函數:\n",results)
