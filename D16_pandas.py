#參考資料(pandas.DatetimeIndex.to_period)
#1.將所有轉為週資料
import numpy as np
import pandas as pd
index = pd.date_range('1/1/2019', periods=20, freq='D')
series = pd.Series(range(20), index=index)
print("資料轉為週資料:\n",series.to_period("w"))
#2.將週資料的值取平均
print("週資料的值取平均:\n",series.resample("w").mean())


