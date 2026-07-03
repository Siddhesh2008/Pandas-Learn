import pandas as pd

df=pd.read_csv("data.csv",index_col='Name')  #replace 'Name' with the name of the column you want to use as the index.
# This will read the CSV file named "data.csv" and create a DataFrame from it, using the specified column as the index.
print(df)  ##This will print the contents of the DataFrame.

##SELECTIN BY COLUMN 
print(df['column_name'].to_string())  ##This will print the contents of the specified column in the DataFrame.

##SELECTIN BY ROW
print(df.iloc['row_index'].to_string())  ##This will print the contents of the specified row in the DataFrame
print(df.loc['row_index'].to_string())  ##This will print the contents of the specified row in the DataFrame
print(df.loc['row_index', ['column_name', 'column_name']])  ##This will print the value at the specified row and column 
#in the DataFrame

#slicing by row
print(df.iloc[1:4].to_string())  ##This will print the contents of the specified rows in the DataFrame

#to get inputs from the user for row and column selection
try:
    print(df.loc['pokemon'])
except KeyError:
    print("Row not found.")