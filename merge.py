import pandas as pd

df1=pd.read_csv("data1.csv")
df2=pd.read_csv("data2.csv")

inner=pd.merge(df1,df2)
print(inner)  ##This will print the contents of the DataFrame that is the result
#of the merge operation on the basis of rows,columns that are similar in both DataFrames

pd.merge(df1,df2,on='Id')   ##This will print the contents of the DataFrame that is the result
#of the merge operation on the basis of the specified column,columns that are similar in both DataFrames 

pd.merge(df1,df2,suffixes=('_left','_right'),left_on='col 2',right_on='col a')  ##This will print the contents of the DataFrame that is the result
#of the merge operation on the basis of the specified column,columns that are similar in both DataFrames

pd.merge(df1,df2,how='outer')  ##this will retain all the data even if there is no match
pd.merge(df1,df2,how='left')  ##this will retain all the data from the left DataFrame even if there is no match
pd.merge(df1,df2,how='right')  ##this will retain all the data from the right DataFrame even if there is no match

