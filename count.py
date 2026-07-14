import pandas as pd

df = pd.read_csv("data.csv")
print(
    df.count()
)  ##This will print the count of non-null values in each column of the DataFrame

print(
    (df["Duration"]).value_counts()
)  ##This will print the count of unique values in the "Duration" column

print(
    df["Duration"].unique()
)  ##This will print the unique values in the "Duration" column

print(
    df["Duration"].nunique()
)  ##This will print the number of unique values in the "Duration" column

print(df["Duration"].skew())  ##This will print the skewness of the "Duration" column

print(df["Duration"].kurt())  ##This will print the kurtosis of the "Duration" column
