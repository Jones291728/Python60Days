import pandas as pd
stock2009=pd.read_csv("STOCK_DAY_0050_202009.csv")
stock2010=pd.read_csv("STOCK_DAY_0050_202010.csv")
combinestock=stock2009.append(stock2010,ignore_index=True)
result=combinestock.loc[(combinestock.open < combinestock.close),["open","close"]]
print("印出欄位open 小於 close 的資料:\n",result)