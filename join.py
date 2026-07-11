import pandas as pd
df1=pd.read_csv("pokemon.csv")
df2=pd.read_csv("pokemon2.csv")

df1.join(df2,on='ID',lsuffix='_left',rsuffix='_right')

df1.join(df2,how='left')
df1.join(df2,how='right')
df1.join(df2,how='inner')
df1.join(df2,how='outer')