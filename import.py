import pandas as pd

df=pd.read_csv("data.csv")  ##This will read the CSV file named "data.csv" and create a DataFrame from it.
print(df)  ##This will print the contents of the DataFrame.
# use df.to_string() to print the entire DataFrame without truncation.

df=pd.read_json("data.json")  ##This will read the JSON file named "data.json" and create a DataFrame from it.
print(df)  ##This will print the contents of the DataFrame. 
#use df.to_string() to print the entire DataFrame without truncation.