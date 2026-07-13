import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")
print(
    df.describe()
)  ##This will print a summary of the DataFrame, including the count, mean, standard deviation, minimum, and maximum values for each numeric column
##count → Number of non-missing values
# mean → Average
# std → Standard deviation (spread of the data)
# min → Smallest value
# 25% → First quartile (25% of values are below this)
# 50% → Median
# 75% → Third quartile
# max → Largest value

print(df.info())  ##This will print information about the DataFrame,
##including the column names, data types, and memory usage

print(df.sample(5))  ##This will print a random sample of 5 rows from the DataFrame
