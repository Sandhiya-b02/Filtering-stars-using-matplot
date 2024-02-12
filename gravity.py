import numpy as np
import pandas as pd
import csv
import numpy as np

data = []

with open("final_data.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

list(np.float_(data[3]))
list(np.float_(data[3]))

mass = []
radius = []

for i in data[3]:
    mass_si = data[3]*1.989e+30
    mass.append(mass_si)
for i in data[3]:
    radius_si = data[3]*6.957e+8
    radius.append(radius_si)

list(np.float_(mass))
list(np.float_(radius))

star_names = data[0]
stars_gravity = []
mass_list = [float(x) for x in mass]
radius_list = [float(x) for x in radius]

gravity = mass_list*5.972e+24 / radius_list*radius_list*6371000*6371000 * 6.674e-11
stars_gravity.append(gravity)