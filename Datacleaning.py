import pandas as pd

##Data Cleaning=the process of fixing/removing incomlete,incorrect, or irrelevant data
#~75% of work done with pamdas is data cleaning and preparation

df=pd.read_csv("data.csv")  ##This will read the CSV file named "data.csv" and create a DataFrame from it.
 #1.drop irrelevant columns
df.drop(columns=["Type 2","Total"],inplace=True)  ##This will drop

#2.Handle missing data
df=df.dropna(subset=["Type 2"])  ##This will drop rows where the "Type 2" column is missing.
df=df.fillna({"Type 2":"None"})  ##This will fill missing values with "None" in the "Type 2" column.

#3.Standardize data
df["Type 1"]=df["Type 1"].str.lower()  ##This will convert all values in the "Type 1" column to lowercase.
df["Type 2"]=df["Type 2"].str.lower()  ##This will convert all values in the "Type 2" column to lowercase.

#4.Fix Inconsistent Data
df["Type 1"]=df["Type 1"].replace({"fire":"FIRE","water":"WATER","grass":"GRASS"})  ##This will replace inconsistent values in the "Type 1" column with consistent values.

#5.Fix Data types
df["Height"]=df["Height"].astype(float)  ##This will convert the "Height" column to a float data type.

#6.Remove duplicates
df=df.drop_duplicates()  ##This will remove duplicate rows from the DataFrame.