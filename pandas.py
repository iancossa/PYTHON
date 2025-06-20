
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


#PANDAS SERIES AND SERIES DATA MANIPULATION
#From list
s1= pd.Series([10,20,30,40])
#From list with custom index
s2 = pd.Series([100,200,300],index=['a','b','c'])
#From dicitionary
s3=pd.Series({'x':5,'y':10,'z':15})
print(s3)
print(s1.index)
print(s2.values)
print(s3.size)
print(s1.shape)
#ACCESING SERIES DATA
print(s2['b'])
print(s2[1])
print(s2[['a','c']])
print(s2[0:2])
#UPDATING VALUES
s2['b']=250 #Update value
s2['d']=400 #Add new item
s2.drop('a',inplace=True)#Delete item

#Vectorized Operarions
s=pd.Series([1,2,3])
print(s+2) #Add 2 to every element
print(s*10) #Mulriply each element
print(s**2) #Power

s=pd.Series([5,10,15,20])

#HANDLING MISSING VALUES
s1 = pd.Series([10,None,30,np.nan])
print(s.isnull()) #True where Nan
print(s.notnull()) #Inverse
s.fillna(0)#Replace NAN with 0
s.dropna()#Remove Nan Entries 


#DESCRIPTIVE STATISTICC
s4= pd.Series([10,20,30,40,50])
prints(s4.sum()) #150
prints(s4.mean()) #30
prints(s4.min(),s4.max()) #10,50
prints(s4.describe()) #Summary stats

a1= pd.Series([10,20,30],index=['a','b','c'])
a2= pd.Series([5,15,25],index=['b','c','d'])
print(a1+a2)
#Index alignment:
#a: NaN
#b: 35
#c: 45
#d: NaN

#SORT AND RANKING STRING 
names = pd.Series(["Alice","bob","CHARLIE","dave"])
s =pd.Series([30,10,40,20],index=['d','b','a','c'])
print(s.sort_values()) #sort by values
print(s.sort_index()) #sort by index
print(s.rank()) #Rank based on values

#Real-Life Example:

old_price=pd.Series({'apple':50,'banana':30,'mango':60})
increase=pd.Series({'banana':5,'mango':10,'orange':20})

new_prices=old_prices +increase
new_prices.fillna("No Data",inplace=True)
print(new_prices)
