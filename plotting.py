from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import pandas as pd
import numpy as np
import plotly.express as px


data = []
with open("final_data_cleaned.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)
mass = []
radius = []


for i in data:
    mass.append(data[2])
    radius.append(data[3])

mass_float = []
radius_float = []
for element in mass:
    mass_float.append(float(element))
for element2 in radius:
    radius_float.append(float(element))

mass_float.sort()
radius_float.sort()



X = []
for index,star_mass in enumerate(mass):
  temp_list = [radius[index],star_mass]
  X.append(temp_list)

wcss = []
for i in range(1,11):
  kmeans = KMeans(n_clusters = i,init = "k-means++",random_state = 42)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)

plt.figure(figsize = (10,5))
sns.lineplot(range(1,11),wcss,marker = "o",color = "red")
plt.title("Elbow Method")
plt.xlabel("No.of clusters")
plt.ylabel("wcss")
plt.show() 

star_mass = []
star_radius = []
planet_types = []
for star_data in data:
  star_radius.append(star_data[3])
  star_mass.append(star_data[2])
fig = px.scatter(x = star_radius,y = star_mass)
fig.show()
