import pandas as pd

df=pd.read_csv("data.csv")  ##This will read the CSV file named "data.csv" and create a DataFrame from it.

#Filtering=Keeping the rows that meet a certain condition and discarding the rest.

tall_pokemon=df[df['Height']>1.0]  ##This will create a new DataFrame named "tall_pokemon" that contains only the rows from the original DataFrame where the value in the "Height" column is greater than 1.0.
print(tall_pokemon) 

heavy_pokemon=df[df['Weight']>100.0]  ##This will create a new DataFrame named "heavy_pokemon" that contains only the rows from the original DataFrame where the value in the "Weight" column is greater than 100.0.
print(heavy_pokemon)

legendary_pokemon=df[df['Legendary']==True]  ##This will create a new DataFrame named "legendary_pokemon" that contains only the rows from the original DataFrame where the value in the "Legendary" column is True.
print(legendary_pokemon)

##the conditions can be used with logical operators to filter the DataFrame based on multiple conditions.
tall_and_heavy_pokemon=df[(df['Height']>1.0) & (df['Weight']>100.0)]  ##This will create a new DataFrame named "tall_and_heavy_pokemon" that contains only the rows from the original DataFrame where the value in the "Height" column is greater than 1.0 and the value in the "Weight" column is greater than 100.0.
print(tall_and_heavy_pokemon)