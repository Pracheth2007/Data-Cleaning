import pandas as pd
import csv
df = pd.read_csv("bright_dwarf_stars.csv")
print(df.shape)

del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

df = df.rename({
                'Radius': "Star_radius",
                'Distance': "Distance_From_Earth",
                'Mass': "Star_mass",
            }, axis='columns')

df.to_csv('main.csv') 
print(list(df))