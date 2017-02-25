import folium, pandas

volcano_dataframe = pandas.read_csv("Volcanoes-USA.txt")
avg_lat = volcano_dataframe["LAT"].mean()
avg_lon = volcano_dataframe["LON"].mean()

map = folium.Map(location=[avg_lat, avg_lon], zoom_start=4, tiles="Stamen Terrain")

def marker_colour(elev):
    min_elev = int(min(volcano_dataframe["ELEV"]))
    max_elev = int(max(volcano_dataframe["ELEV"]))
    step = int((max_elev - min_elev) / 3)

    if elev in range(min_elev, min_elev + step):
        colour = "green"
    elif elev in range(min_elev + step, min_elev + step * 2):
        colour = "orange" 
    else:
        colour = "red"
    return colour

for lat, lon, name, elev in zip(volcano_dataframe["LAT"], volcano_dataframe["LON"], volcano_dataframe["NAME"], volcano_dataframe["ELEV"]):
    map.simple_marker(location=[lat, lon], popup=name, marker_color=marker_colour(elev))

map.create_map(path="test_map.html")
