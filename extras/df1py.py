import pandas as pd
import numpy as np
df=pd.DataFrame({
     "cat1":["a","a",np.nan,"b","c","a","a","b","c","a","c","d"],
     "cat2":["x","x","y","x","y","y","x","y","x","y","x","y"],
     "value":[10,23,44,65,18,54,71,45,34,15,54,7],
     "price":[10,45,100,121,131,76,23,45,65,49,10,48]
     })
print(df)
#df.to_csv("E:/df.csv")#to save this dataframe to our device
#df=pd.read_csv("E:/df.csv")
print(df.isna())
print(df.isna().sum())
df1=df.fillna(0) 
print(df1)
print(df1.isna().sum())
#drop a column
df2=df.drop(["cat1"],axis=1)
print(df2)
df3=df.groupby(["cat1"]).sum()
print(df3)
