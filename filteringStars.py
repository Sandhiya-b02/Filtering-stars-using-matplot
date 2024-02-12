import csv
import matplotlib as plt
import pandas as pd

data = []

with open("final_data.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

distance = data[1]

new_dataframe = {}

for index,star_data in enumerate(data):
  filters = []
  try:
    if distance < 100 or distance == 100:
      filters.append("distance")
  except:
    pass
  new_dataframe[index] = filters
print(new_dataframe)
df = pd.DataFrame.from_dict(new_dataframe)
df.to_csv("filtered_data.csv"[1:])