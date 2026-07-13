import pandas as pd

#aggregrate functions = functions that perform a calculation on a set of values and return a single value.
#used to summarize data in a DataFrame or Series.
#often used in conjunction with the groupby() method to perform calculations on groups of data.

df=pd.read_csv("data.csv")  ##This will read the CSV file named "data.csv" and create a DataFrame from it.
print(df)

print(df['Height'].mean())  ##This will print the mean of the values in the "Height" column of the DataFrame.
print(df.mean(numeric_only=True))  ##This will print the mean of the values in all numeric columns of the DataFrame.
print(df.sum(numeric_only=True))  ##This will print the sum of the values in all numeric columns of the DataFrame.
print(df.min(numeric_only=True))  ##This will print the minimum value in all numeric columns of the DataFrame.
print(df.count(numeric_only=True))  ##This will print the count of non-null values in all numeric columns of the DataFrame.

#single column
print(df['Height'].sum())  ##This will print the sum of the values in the "Height" column of the DataFrame.
print(df['Height'].min())  ##This will print the minimum value in the "Height" column of the DataFrame.
print(df['Height'].max())  ##This will print the maximum value in the "Height" column of the DataFrame.
print(df['Height'].count())  ##This will print the count of non-null values in the "Height" column of the DataFrame.

group=df.groupby('Type 1')  ##This will group the DataFrame by the values in the "Type 1" column.

print(group['Height'].mean())  ##This will print the mean of the values in the "Height" column of the DataFrame, grouped by the values in the "Type 1" column.
print(group['Height'].sum())  ##This will print the sum of the values in the "Height" column of the DataFrame, grouped by the values in the "Type 1" column.
print(group['Height'].min())  ##This will print the minimum value in the "Height" column of the DataFrame, grouped by the values in the "Type 1" column.
print(group['Height'].max())  ##This will print the maximum value in the "Height" column of the DataFrame, grouped by the values in the "Type 1" column.
print(group['Height'].count())  ##This will print the count of non-null values in the "Height" column of the DataFrame, grouped by the values in the "Type 1" column.


##to do all this at the same time
df.groupby('Type 1').agg({'Height': ['mean', 'sum', 'min', 'max', 'count']})