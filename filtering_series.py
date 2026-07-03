import pandas as pd

data =[11,102,104]

series=pd.Series(data,index=['a','b','c'])

print(series[series>100])  ##This will filter the series and return only the elements that are greater than 100.