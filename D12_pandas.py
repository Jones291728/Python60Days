import pandas as pd
import numpy as np
#1.畫出箱型圖，並判斷哪個欄位的中位數在300~400之間?
df=pd.read_csv("boston.csv")
graphic=pd.DataFrame(df)
graphic.boxplot()
import matplotlib.pyplot as plt
plt.show()
xlarge = graphic.median()
filter01= xlarge >=300
filter02= xlarge <=400
results=filter01 & filter02
print("中位數在300~400之間有:\n",xlarge[results])

#2.畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係?
graphic=pd.DataFrame(df,columns=["NOX","DIS"])
print("NOR-DIS間呈現負相關因果關係")
df.plot.scatter(x="NOX", y="DIS")
import matplotlib.pyplot as plt
plt.show()
