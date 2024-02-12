import csv

data_1 = []
data_2 = []

with open("archive_dataset_new.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data_1.append(row)

with open("dwarf_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data_2.append(row)

headers_1 = data_1[0]
star_data_1 = data_1[1:]

headers_2 = data_2[0]
star_data_2 = data_2[1:]

headers = headers_1 + headers_2
stars_data = []
for index, data_row in enumerate(star_data_1):
    stars_data.append(star_data_1[1:] + star_data_2[1:])

with open("final_data.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)