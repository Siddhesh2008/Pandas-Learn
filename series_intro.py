import pandas as pd

data=[11,102,104]
series = pd.Series(data)

print(series)   ##dtype: int64 depends on the data type of the elements in the series. In this case,
    ##since all elements are integers, the dtype is int64.