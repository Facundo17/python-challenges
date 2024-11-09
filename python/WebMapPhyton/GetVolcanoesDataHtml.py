import pandas
import folium

volcanoes = pandas.read_csv("volcanoes.txt") # leer el archivo
map = folium.Map(location=[38.2, -99.1], zoom_start=6, tiles="CartoDB Positron") # crear el mapa

# obtengo los valores que necesito de cada columna
lt = list(volcanoes["LAT"])
ln = list(volcanoes["LON"])
nams = list(volcanoes["ELEV"])

# menos de 1000 de altura: verde
# mas de 1000 y menos de 2000: amarillo
# mas de 2000 y menos de 3000: naranja
# mas de 3000 y menos de 4000: marron
# mas de 4000 rojo
def color_producer(elev):
    if elev < 1000:
        return "lightgreen"
    if elev < 2000:
        return "green"
    if elev < 3000:
        return "darkgreen"
    if elev < 4000:
        return "orange"
    
    return "red"

# agregar un html
html = """<h4>Volcano information: %s m</>"""

# crear un grupo
fgv = folium.FeatureGroup(name="My volcanoes")

for i, j, k in zip(lt, ln, nams):
    # crear el html usando IFrame
    iframe = folium.IFrame(html=html % str(k), width=200, height=100)
    # agrego el marker
    #fg.add_child(folium.Marker(location=[i, j], popup=folium.Popup(iframe), icon = folium.Icon(color = color_producer(k))))
    # agregar un Circle Marker
    fgv.add_child(folium.CircleMarker(location=[i, j], popup=folium.Popup(iframe), fill_color = color_producer(k), color = color_producer(k), fillOpacity=0.7))

fgp = folium.FeatureGroup(name="Population") # nota, agregar esta capa antes que la anterior, si no, no se ve el popup
# añadir un "population layer", usando el world.json
#fg.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read()))
# añadir colores a los paises
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), 
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# agregar los grupos (layers)          
map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl()) # añadir un contro layer
map.save("Map_html_popup_simple.html")