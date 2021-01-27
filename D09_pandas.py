import pandas as pd
data=pd.read_csv("boston.csv",usecols=["CHAS","NOX","RM"])
data.to_excel("US_boston.xlsx",sheet_name="20210127")