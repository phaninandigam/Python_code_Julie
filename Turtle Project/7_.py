import pandas as pd

df=pd.read_csv('data.txt', sep = "\t")
print(df.head())
print(df['Company'].value_counts())
