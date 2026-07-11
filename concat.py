import pandas as pd

df1=pd.read_csv("pokemon.csv")
df2=pd.read_csv("pokemon2.csv")

df=pd.concat([df1,df2])   ##just stitches two dfs

#to reset the index 
pd.concat([df1,df2],ignore_index=True)

#can side by side by specifying axis=1

pd.concat([df1,df2],axis=1)

#concat has only inner and outer joins.

