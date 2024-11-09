import pandas
import folium

map = folium.Map(location=[38.2, -99.1], zoom_start=6, tiles="CartoDB Positron")
fg = folium.FeatureGroup(name="My volcanoes")

volcanoes = pandas.read_csv("volcanoes.txt")

lt = list(volcanoes["LAT"])
ln = list(volcanoes["LON"])
nams = list(volcanoes["ELEV"])

for i, j, k in zip(lt, ln, nams):
    fg.add_child(folium.Marker(location=[i, j], popup=str(k) + " m", icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("maps/Volcanoes.html")