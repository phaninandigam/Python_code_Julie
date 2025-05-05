import pandas as pd

df=pd.read_csv('duplicate_profiles.csv')
print(df.head(0))

# print(df.string_u_em_157 =='faisalzahgeer34@gmail.com')
# print(df.loc[df['string_u_em_157'] == 'faisalzahgeer34@gmail.com'])

# x=df.sort_values("string_u_em_157", ascending= True)
required_columns=df[['user_id','string_u_em_157','lastseen']]
# print(required_columns)

# if required_columns.string_u_em_157 =='faisalzahgeer34@gmail.com':
#     # print(required_columns.sort_values(['string_u_em_157','lastseen'], ascending=[True,False]))
#     print("ji")
x=df.loc[df['string_u_em_157'] == 'faisalzahgeer34@gmail.com']
print(x)
if x['string_u_em_157'] == 'faisalzahgeer34@gmail.com':
    print("hi")