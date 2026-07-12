import pandas as pd
import numpy as np
df=pd.read_csv("data.csv")

df1=df.fillna(0)   ##this will fill the null values with 0

df2=df.ffill()  #Filling null values with prev values

df3=df.bfill()  #Filling null values with next values

df4=df.ffill(axis=1)  #Filling null values with prev values columnwise  

df5=df.bfill(axis=1)  #Filling null values with next values columnwise

df6=df.fillna({'Duration':'abcd','Date':1})  #Filling null values with specific values

df7=df.fillna({'Duration':df['Duration'].mean()})  #Filling null values with mean of the column, max and min can also be used

df8=df.dropna()  #Dropping rows with null values

df9=df.dropna(how='all')  #Dropping rows with all null values

df10=df.dropna(how='any')  #Dropping rows with any null values

df11=df.dropna(thresh=3)  #Dropping rows with less than 3 non-null values

df12=df.dropna(thresh=3, axis=1)  #Dropping columns with less than 3 non-null values

##Replacing null values
df13=df.replace(np.nan,1233)  ##can be used to replace any value

##using interpolate
df['Pulse']=df['Pulse'].interpolate(method='linear',limit_direction='forward')



print(df1)
print(df2)
print(df3)
print(df4)
print(df5)
print(df6)
print(df7)
print(df8)
print(df9)
print(df10)
print(df11) 
print(df12)
print(df13)
print(df)

