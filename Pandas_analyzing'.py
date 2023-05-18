# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:54:49 2023

@author: user
"""
#Analysis
'''import pandas as pd
df=pd.read_csv("D:\python\Pandas\dataset\ETFs.csv")
df
df[["region","currency"]]
df.iloc[2]
df.loc[0:10,"region"]
df.info()
df.isna().sum()
d=df.dropna()
df.duplicated().sum()
df.dropna(how="all",inplace=True)

f=df.fillna("Large fund")
df
c=df["fund_short_name"].fillna("Large fund")
df.iloc[2,3]="Large fund"
df
df.loc[4,"fund_short_name"]="Large fund"

temp=df[["fund_short_name","fund_long_name","currency","fund_family","size_type","week52_high","week52_low"]][0:100]
temp.currency
temp.info()
temp["fund_long_name"].unique()
temp["fund_long_name"].nunique()


#task to read  json,sql,html.
# df1=pd.read_json("D:\python\Pandas\dataset\intents.json")#json
# df3=pd.read_

temp.nlargest(5,"week52_high")#it will use in integer datatype only it will show from largest value and show how much u want u should write like 5 in this condition
temp.nsmallest(5,"week52_high")#same like above smallest
temp.sort_values("fund_long_name")#it will sort value in ascending
temp.sort_values(["fund_long_name","fund_short_name"])
temp.sort_values("fund_short_name",ascending=False)#it will sort value in descending if u write true then u will get ascending
z=temp.sort_values(["fund_family","fund_short_name"],ascending=[True,False])#it will give first priorty to first column name it will not apply for 2nd column.
temp.sort_values("fund_short_name").loc[0:10,"fund_short_name"]#in this code it will fetch specific data and it will sort it.
temp.sort_values("fund_short_name",ascending=False).iloc[0:5,1]#same like previous one

temp.info()
temp[["week52_low","week52_high"]]=temp[["week52_low","week52_high"]].astype(str)#it is like typecasting changing datatype
temp.info()

r={"Digit":["1,1","1,2"],
   "Value":["0,1","0,2"]}
df2=pd.DataFrame(r)

df2[["Digit","Value"]]=df2[["Digit","Value"]].replace(',','',regex=True)#if we will give False it will not replace .
        #regex is method to search a string and match it , it use to find , replace string

c={"currency":["$","$","$","Rupees"],
   "country":["U.S.A","U.K","Brazil","India"],
   "Continent":["America","Europe","America","Asia"]}
df4=pd.DataFrame(c)
df4[["currency","country"]]=df4[["currency","country"]].replace(['\\$','\\.'],['USD',''],regex=True)
#we are using backlash \\ for making it literal character as normal letter instead of special character bcuz special character can't use in regular expression .

co={"name":["vinayak","  vinayak","vinayak  ",  "     vinayak","vinayak      " ],
    "course":[" Python"," Datascience","Mysql","Datas cience","Mysql"],
    # "digits":[10 000,2 000,50 000,30 ,000,100],
    "dgts":['10,000','2,000       ','   50,000','30,000','100']}
df5=pd.DataFrame(co)
df5.name.unique()
# df5["name"]=df5["name"].replace('  ','',regex=True)
df5["name"] = df5["name"].str.strip()#str.strip is use for removing space in normal python .strip will use
df5.name.unique()
df5
df5["dgts"] = df5["dgts"].str.strip()
df5
df5['dgts']=df5['dgts'].replace(",","",regex=True)
df5.info()
df5['dgts']=df5['dgts'].astype(int)
#using cleaning ,sir will give u dataset
----------------------------------------------------------------------------------------------------------------------
#giving condition
import pandas as pd
df=pd.read_csv("D:\python\Pandas\dataset\ETFs.csv")
df
# df.loc[df.columns_name ==(condition what u have to give)value]#in this we have take specific values by giving conditions

#single condtions only
df.columns
df.loc[df.week52_high >100 ]
df.loc[df.week52_low <50 ]

#multiple condtions 
df.loc[df.size_type == "Large" ].iloc[0:100,0:]
df.loc[((df.week52_high >100 )&(df.week52_low <50))|(df.size_type == "Low")].loc[0:1000,['week52_high','week52_low','size_type']]#giving multiple condition and want specific dat so doing by loc method

#different method to solve by using query
df.query('(week52_high >100 & week52_low <50 & size_type == "Low")|((currency=="USD")&(week52_low <50)) ').loc[0:1000,['week52_high','week52_low','size_type','currency']]
#note if there is any space in column just give "~" before name

#groupby it will work on categorical data only
df.groupby("size_type").count()
df.groupby("size_type").min()
df.groupby("size_type").max()
df.groupby("size_type").sum()
pd.Series([1,2,3,4,5],index=['a','b','c','d'])#Practice in this value error will occur bcuz the index has given but has given extra thats why


#homework split , project structure
#solve mcq and doubt also#homework
import pandas as pd
d={'Name':['John Wick vinayak XYZ','Tony Stark','Tom Holland','Uchiha Sasuke','Hinata Shoya'],
   'Profession':['Actor','Engineer','Actor','Ninja','Volleyball player'],
   'Age':[50,45,28,24,25]}
df=pd.DataFrame(d)
df[["First Name","Last Name","middle name",'']]=df['Name'].str.split(' ',n=3,expand=True)#if expand is True it will seperate in DataFrame & if it is false then it will give series, there is another property also 'n' whis is used to how many words u have to separate like.,

------------------------------------------------------------------------------------------------------------------------
import pandas as pd
df=pd.read_csv("D:\python\Pandas\dataset\ETFs.csv")
df
df.info()
df.fund_short_name
df.isnull().sum()

df.loc[df.fund_short_name.str.startswith('D')]#startswith is use for searching something by first letter
x.fund_short_name
x1=df.loc[df.fund_long_name.str.endswith('t')]#endswith is use for searching something by end letter
x1.fund_short_name

df.dropna(inplace=True)

df
---------------------------------------------------------------------------------------------------------------
# df.loc[df["Open"].idxmax()]#it is used for searching that index and giving full row in series of that specific data.

'''
# ---------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
d={'Name':['John Wick vinayak XYZ','Tony Stark','Tom Holland','Uchiha Sasuke','Hinata Shoya'],
   'Profession':['Actor','Engineer','Actor','Ninja','Volleyball player'],
   'Age':[50,45,28,24,25]}
df=pd.DataFrame(d)
df.rename(columns={'Profession':'Field'},inplace=True)
df.drop(2,inplace=True)
df
df.reset_index(drop=True)
# -----------------------------------------------------------------------------------------------------------
a={'Name':['Krunal','Komal','Jash','Tanisha','Arjun'],
   "City":['Mumbai','Thane','Mumbai','Thane','Navi Mumbai']}
b={'Name':['Vinayak','Komal','Jash','Tanisha','Diamond'],
   "Course":['Python','DSP','DSP','Python','AI']}
df1=pd.DataFrame(a)
df2=pd.DataFrame(b)
df1
df2
con=pd.concat([df1,df2])#concat will join 2 table in 1 table it will give double time data if it is repeated another table also
con
con=pd.concat([df1,df2],axis='rows')#same like previous one
con
con=pd.concat([df1,df2],axis='columns')#it will show in column way
con
# -------------------------------------------------------------------------------------------------------------
m1=df1.merge(df2)#it will give common data only
m1
m2=df1.merge(df2,how='left')#here it will give left data full which will join city also and give if they have or it will give nan
m2
m3=df1.merge(df2,how='right')#here it will give right data full which will join course also and give if they have or it will give nan
m3
m4=df1.merge(df2,how='outer')# it will merge 2 data but it will not give double data like concat it will merge in it the common factor
m4

# merge
# concat
# join
# ---------------------------------------------------------------------------------------------------------






















