import requests
import pandas as pd


df=pd.read_csv('userdata.csv')
# print(df.columns)
# print(len(df))
# print(df.shape)
# print(len(df.columns))
# print(df.head)
# print("----------------------")

for item in range(0,len(df)):
    # print(df.ID[item])
    # print(df.Email[item])
    # print(df.MobileNumber[item])
    # print(df)

    id= df.ID[item]
    email= df.Email[item]
    mobileNumber= df.MobileNumber[item]
    # id= "phani.nandigam113@moengage.com"
    # email= "phani.nandigam@moengage.com"
    # mobileNumber= "999999999"
    url= 'https://api-01.moengage.com/v1/customer/6GN1O6W4CPDCSH7242E622JY'
    myauth= ('6GN1O6W4CPDCSH7242E622JY','Kwph+o-iOe4Owlz5aoAp53xE')
    myheaders= {"Content-Type":"application/json"}
    myjson= {"type" : "customer","customer_id": id,
             "attributes" : {"u_em":email,"u_mb":mobileNumber}}
    response=requests.post(url, auth=myauth, headers=myheaders, json = myjson)
    response=response.text
    response_code=response.status_code
    response.to_csv("response.csv",index=False)
