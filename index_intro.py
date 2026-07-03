import pandas as pd

data =[11,102,104]

series=pd.Series(data,index=['a','b','c'])

print(series)   ##dtype: int64 depends on the data type of the elements in the series. In this case,
#index=['a','b','c'] is used to assign custom index labels to the series. 
# The resulting series will have the values 11, 102, and 104 associated with the labels 'a', 'b', and
# 'c' respectively.

print(series.loc['b'])  ##This will print the value associated with the index label 'b'.
series.loc['b'] = 200  ##This will update the value associated with the index label 'b' to 200.

print(series.iloc[1])   ##This will print the value at the position 1 in the series
