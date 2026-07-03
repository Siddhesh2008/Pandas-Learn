import pandas as pd

data={"Name":["Alice","Bob","Charlie","David"],     #using a dictionary to create a DataFrame. The keys of the dictionary
                                                    # represent the column names, and the values are lists that represent the data for each column.
      "Age":[25,30,35,40],
      "Gender":["Female","Male","Male","Male"]}
df=pd.DataFrame(data,index=["Employee1","Employee2","Employee3","Employee4"])  ##index=["row1","row2","row3","row4"] is used to assign custom index labels to the rows of the DataFrame.
print(df)
print(df.loc["Employee2"])   ##This will print the row with the index label "Employee2".

print(df.iloc[1])   ##This will print the row at position 1 in the DataFrame

#add a new column to the DataFrame
df["Department"]=["HR","Finance","IT","Marketing"]  ##This will add a new column named "Department" 
#to the DataFrame with the specified values.

#add a new row to the DataFrame
new_rows=pd.DataFrame({"Name":["Eve"],"Age":[28],"Gender":["Female"],"Department":["Sales"], "Name":["Frank"],"Age":[32],"Gender":["Male"],"Department":["IT"]},index=["Employee5","Employee6"])  ##This will create a new DataFrame with the specified values.
df=pd.concat([df,new_rows])  ##This will concatenate the new rows to the existing DataFrame.