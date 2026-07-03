import pandas as pd

# Create a series from a dictionary
data = {'a': 10, 'b': 20, 'c': 30, 'd': 40}  #values in the dictionary represent the data, and the keys represent 
#the index labels of the series.
series = pd.Series(data)    ##index=['a','b','c','d'] is used to assign custom index labels to the series.

print(series)
