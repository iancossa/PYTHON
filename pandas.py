
#used for data manipulation and analysis
import pandas as pd
import numpy as np

s = pd.Series([10,20,30], index=["a","b","c"])
print(s["b"])
print(s.values)

#DATBASEFRAME: 2D TABLE WITH LABELED 
dic= {"Name":["Ian","Priya","Bhaghavan"],"Age":[24,19,19],"Score":[100,81,99]}
print(type(dic))
#creating a dataframe
df=pd.DataFrame(dic)
'''
print(df)
print(df["Score"])#accessing dataframe
print(df.iloc[0])#access row
print(df.loc[1])#access 2nd row using loc->not index
print(df[df["Score"]>80])#filtering by condition
'''
#DATAFRAME OPERATION

df["Grade"]=["A+","B","C"] #adding entries(New Column)
print(df)
df.drop("Age",axis=1,inplace=True)
print(df)
df.rename(columns={"Score":"Marks"},inplace=True)
#MISSING VALUES
df = pd.DataFrame({
    "Name":["Francis",None,"Charlie"],
    "Marks":[78,np.nan,95] 
})

print(df.isnull()) #detect missing

df.fillna(0,inplace=True) 
#df.fillna("Unknown",inplace=True)#Fill
print(df)
#df.dropna(inplace=True)
print(df)
print(df.describe())
print(df["Marks"].mean())
print(df.groupby("Name")["Marks"].min()>80)


