import requests
import pandas as pd


df=pd.read_csv('userdata_copy.csv')
for item in range(0,len(df)):
    id = str(df.ID[item])
    email = str(df.Email[item])
    mobileNumber = str(df.MobileNumber[item])
    # id= "phani.nandigam113@moengage.com"
    # email= "phani.nandigam@moengage.com"
    # mobileNumber= "999999999"
    url= 'https://api-01.moengage.com/v1/customer/6GN1O6W4CPDCSH7242E622JY'
    myauth= ('6GN1O6W4CPDCSH7242E622JY','Kwph+o-iOe4Owlz5aoAp53xE')
    myheaders= {"Content-Type":"application/json"}
    myjson= {"type" : "customer","customer_id": id,
             "attributes" : {"u_em":email,"u_mb":mobileNumber}}
    response=requests.post(url, auth=myauth, headers=myheaders, json = myjson)
    response.text
    df['Response']=response.text
    # df1.to_csv("response.csv", index=False)
    df['Response_code']=response.status_code
    df.to_csv("response.csv", index=False)

