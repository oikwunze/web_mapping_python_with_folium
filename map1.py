from os import read
import folium
from folium.features import GeoJson
import pandas

data = pandas.read_csv("Volcanoes.txt")
# print(data)

lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'



map = folium.Map(location=[39.88693977095676, -112.04083366158164], zoom_start=6, tiles="Stamen Terrain")


fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + ' m', icon=folium.Icon(color=color_producer(el))))


# fg.add_child(folium.GeoJson(open('world.json', 'r', encoding='utf-8-sig'),style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
# else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)

map.add_child(folium.LayerControl())
map.save("Map1.html")







