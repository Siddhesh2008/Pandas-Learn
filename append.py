import pandas as pd

df1=pd.read_csv("pokemon.csv")
df2=pd.read_csv("pokemon2.csv")

df1.append(df2)

df1.append(df2,sort=True)  ##sorts the data