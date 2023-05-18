# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# name="vinayaK"
# print(name)
# rn=50
# rn
'''zomato={"rest Name":["Mao family restraunt","Chinese Wok","Wow Momos","Swagat","Taj","Santosh","shree krushna dining","Gopal krishna"],
        "Rating":[4,3.8,5,4,5,3.9,4,5],
        "City":["Andheri","parel","dadar","Santacruz","Andheri","Vile Parle","Virar","vasai"]}

print(zomato)
import pandas as pd   #importing pandas as pd
f=pd.DataFrame(zomato)   #DataFrame is use for making table and Data type is dataframe
print(f)


# 1.First type "dot method" it is use for single columns only
f.Rating
# f.rest name    it will not work here if there is space between them.
f.City


#2.Second method for multiple columns
f["Rating"]
f["rest Name"]#here u should  use this method for space key
f[["Rating","City"]]


#3.Third method "iloc method" (integer location)  : iloc method is used for getting specific data
# syntax : F.iloc[row number,column number]
f.iloc[2]
f.iloc[:]
f.iloc[2:,1]
f.iloc[:,:2]

#task:Santosh     3.9  Vile Parle ,  Swagat     4.0 Taj     5.0 ,     4.0       Virar      5.0       vasai,
#rating full column, from wow momos full data all colm and rows,  Mao family restraunt     4.0 
# from chinese to taj rst name and rating only

f.iloc[5]
f.iloc[3:5,0:2]
f.iloc[2:,1]
f.iloc[6:,1:]
f.Rating
f.iloc[0,:2]
f.iloc[1:5,:2]
f.iloc[2:,:]

#Company ,owners ,profitable business make data using Tupple or list

details=[{"Company":"Tata","Founder":"Ratan Tata","Famous Business":"TCS"},
         {"Company":"Reliance","Founder":"Dhirubhai Ambani","Famous Business":"Jio"},
         {"Company":"ITC","Founder":"William Henry Harrison","Famous Business":"Cigarettes & FMCG"},
         {"Company":"HDFC","Founder":"ICICI ,UTI & NHB","Famous Business":"HDFC Bank"},
         {"Company":"L & T","Founder":"Whenning Holck-Larsen and Søren Kristian Toubro.","Famous Business":"Engineering and construction"}]

import pandas as pd
fr=pd.DataFrame(details)
print(fr)
fr.Founder #printing founders only
fr.iloc[:,:2] #company and founder names
fr.iloc[:,0::1] #this one or next one both are same
fr[["Company","Famous Business"]]
fr.iloc[2,:]
fr.iloc[2:,:]

fr.iloc[[0,1]]
fr.iloc[:,[0,2]]

#loc(Location): diffn btn loc & iloc is instead of colm no. , name should be given and in this instead of excluding upperlimit it will include
#syntax: fr.loc[row number,column name]
fr.loc[2:,["Founder","Company" ]]
fr.loc[[1,2],["Founder","Company","Famous Business" ]]
fr.loc[:,["Founder","Company","Famous Business"]]
fr.loc[0:4,["Company","Founder","Famous Business"]]

fr[["Founder","Company"]].loc[0:2,"Founder"]#here we make a dummy table and from that we are fetching specific data
fr[["Founder","Company"]].iloc[0:2,1]#same like previous one only here iloc properties will be apply.
fr[["Founder","Company"]].loc[:]

#task
fr.iloc[3:]
fr.iloc[3:,[1,2]]
fr.loc[3:4,["Founder","Famous Business"]]
fr[["Founder","Company"]].loc[2,"Company"]
fr[["Founder","Company"]].loc[2:,"Company"]
fr[["Founder","Famous Business"]].iloc[:,1]

fr2=pd.DataFrame(details,index=["a","b","c","d","e"])#by using this u can edit index no. or name
print(fr2)
fr2.iloc[0:3,0:2]#we have to give index number
fr2.loc["a":"c",["Company","Founder"]]#in this what we have edited that index

#Series Function is making data how u given while making data frame
s1=pd.Series(details)
print(s1)
s1[["Company","Founder"]]

s1[2]["Company"]

#To save data in format
#syntax: var.to_format
fr.to_excel("D:\python\Pandas\Companydetailslec2.xlsx")
fr.to_excel("D:\python\Pandas\Companydetailslec2(2).xlsx",index=False)

#task: to save file in various format
fr.to_csv("D:\python\Pandas\Companydetailslec2(csv).csv",index=False)#csv
fr.to_html("D:\python\Pandas\Companydetailslec2(html).html",index=False)#html
fr.to_json("D:\python\Pandas\Companydetailslec2(json).json")#json
a=fr.to_dict("D:\python\Pandas\Companydetailslec2(json).json")#json to dict
type(a)
----------------------------------------------------------------------------------
import numpy as np
import pandas as pd
zomato={"rest Name":["Mao family restraunt","Mao family restraunt","Chinese Wok","Wow Momos","Swagat","Taj","Santosh","shree krushna dining","Gopal krishna",np.nan],
        "Rating":[4,4,3.8,5,4,5,3.9,4,5,np.nan],
        "City":[np.nan,np.nan,"parel","dadar","Santacruz","Andheri","Vile Parle","Virar","vasai",np.nan]}
f=pd.DataFrame(zomato)
print(f)
f.head(2)
f.tail(2)
f.to_csv("D:\python\Pandas\zomatolec3(csv).csv")
# df=f.read_csv(r"D:\python\Pandas\zomatolec3(csv).csv")
--------------------------
f.info()
f.isnull()
f.isna()
f.notnull()
f.notna()
f.isnull().sum()
f.dropna()# it will dropp rows
f.dropna(inplace=True)#pemanent drop
f
f.dropna(how="all",inplace=True)#drop blank column bcuz "all" is refer to full row there is nan.
f
f.duplicated().sum()
f.drop_duplicates()#temporary drop, we have to write inplace true for permanent drop.
f
----------------------------------------------------------------------------------------------------
#filling method
f.fillna("Andheri")
f["City"].fillna("Lower Parel",inplace=True)
f
f["Rating"].fillna(4.5,inplace=True)
f
f["rest Name"].fillna("Krishna",inplace=True)
f


f.loc[8,"Rating"]=4.7
f
f.loc[8,"rest Name"]="Krishna"
f
f.loc[8,["Rating","City"]]=(4.7,"kurla")
f
'''
---------------------------------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
zomato={"rest Name":["Mao family restraunt","Mao family restraunt","Chinese Wok","Wow Momos","Swagat","Taj","Santosh","shree krushna dining","Gopal krishna",np.nan],
        "Rating":[4,4,3.8,5,4,5,3.9,4,5,np.nan],
        "City":[np.nan,np.nan,"parel","dadar","Santacruz","Andheri","Vile Parle","Virar","vasai",np.nan]}
f=pd.DataFrame(zomato)
print(f)
f.drop("City",axis="columns")#it will drop full column in this we should give axis
f
f.drop("City",axis="columns",inplace=True)#it will drop permanently
f

















