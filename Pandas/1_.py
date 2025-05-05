import pandas as pd

# to load the csv file
df=pd.read_csv("pokemon_data.csv")
print(df.head(5))
print(df.tail(3))
print("----------------")

# to get the headers
print(df.columns)
print("----------------")

# to read the colums
print(df['Name'])
print(df['Name'][0:5])
print("----------------")
print(df.Name)
# both 14 and 17 works


# to read rows
print("----------------")
print(df.iloc[4]) #this will print the 4th index row
print(df.iloc[1:5])#this will print from 1st index to 4th index

# to print the specific location (row, column)
print(df.iloc[1,1])


# sorting
print(df.sort_values("Name"))
print(df.sort_values("Name", ascending=False))