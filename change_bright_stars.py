import csv
import pandas as pd
data = []
with open("bright_stars.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)
for i in data[2]:
    solar_mass = data[2]*int(0.000954588)
for i in data[3]:
    solar_radius = data[3]*int(0.102763)

headers = data[0]
star_data = data[1:]

with open("archive_dataset_new.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)
