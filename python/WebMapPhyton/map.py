import folium
# para ver las opciones de Map -> help(folium.Map)
map = folium.Map(location=[38.2, -99.1], zoom_start=6, tiles="CartoDB Positron")

fg = folium.FeatureGroup(name="My Map") # creando un FeatureGroup
#fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color="red")))
#fg.add_child(folium.Marker(location=[30.2, -85.1], popup="Hi I am a Marker", icon=folium.Icon(color="green")))
# usando un for loop

for coordinates in [[38.2, -99.1], [30.2, -86.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color="red")))

map.add_child(fg)
map.save("maps/Map2.html")