import pandas as pd
import csv

df = pd.read_csv("final_data.csv",encoding="ISO-8859–1")
print(df.shape)

del df["Luminosity"]

df.to_csv("final_data_cleaned.csv")

print(list(df))
