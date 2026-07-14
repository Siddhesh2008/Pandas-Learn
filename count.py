import pandas as pd

df = pd.read_csv("data.csv")
print(
    df.count()
)  ##This will print the count of non-null values in each column of the DataFrame

print(
    (df["Calories"]).value_counts()
)  ##This will print the count of unique values in the "Type 1" column

print(
    df["Duration"].unique()
)  ##This will print the unique values in the "Type 1" column

print(
    df["Duration"].nunique()
)  ##This will print the number of unique values in the "Type 1" column

print(df["Duration"].skew())
