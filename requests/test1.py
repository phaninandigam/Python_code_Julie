import pandas as pd

df=pd.read_csv("response.csv")
print(df.columns)
print(df.ID)
print(df.Email)
print(df.MobileNumber)
print(df.Response)
