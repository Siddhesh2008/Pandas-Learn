import pandas as pd 
df=pd.read_csv("data.csv")
print(df.shape)
print(df.isnull())         ##to check for null values ,, reutrns true or false
print(df.isnull().sum())  ##to count the null values
print(df.isnull().sum().sum())    ##to count the total null values