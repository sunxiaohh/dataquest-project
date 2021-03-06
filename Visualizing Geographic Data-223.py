## 1. Geographic Data ##

import pandas as pd
airlines=pd.read_csv("airlines.csv")
airports=pd.read_csv("airports.csv")
routes=pd.read_csv("routes.csv")

print(airports.iloc[0])
print(airlines.iloc[0])
print(routes.iloc[0])

## 4. Workflow With Basemap ##

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

m=Basemap(projection="merc",llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180)

## 5. Converting From Spherical to Cartesian Coordinates ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes=airports["longitude"].tolist()
latitudes=airports["latitude"].tolist()
x,y=m(longitudes,latitudes)

## 6. Generating A Scatter Plot ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
x, y = m(longitudes, latitudes)
m.scatter(x,y,s=1)
plt.show()

## 7. Customizing The Plot Using Basemap ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()
plt.show()

## 8. Customizing The Plot Using Matplotlib ##

#figAdd code here, before creating the Basemap instance.
fig,ax=plt.subplots(figsize=(15,20))
plt.title("Scaled Up Earth With Coastlines")
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()
plt.show()

## 9. Introduction to Great Circles ##

geo_routes=pd.read_csv("geo_routes.csv")
print(geo_routes.info())
print(geo_routes.head(5))

## 10. Displaying Great Circles ##

fig, ax = plt.subplots(figsize=(15,20))
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()

def create_great_circles(frame):
    for index, row in frame.iterrows():
        if abs(row["end_lat"]-row["start_lat"]<180):
            if abs(row["end_lon"]-row["start_lon"]<180):
                m.drawgreatcircle(row["start_lon"],row["start_lat"],
                               row["end_lon"],row["end_lat"])
                
                
                
dfw=geo_routes[geo_routes["source"]=="DFW"]
n=create_great_circles(dfw)
plt.show()
                
                