import folium, pandas

map = folium.Map(location=[45.372, -121.697], zoom_start=4, tiles="Stamen Terrain")

volcano_dataframe = pandas.read_csv("Volcanoes-USA.txt")

for lat, lon, name, elev in zip(volcano_dataframe["LAT"], volcano_dataframe["LON"], volcano_dataframe["NAME"], volcano_dataframe["ELEV"]):
    map.simple_marker(location=[lat, lon], popup=name, marker_color="green" if elev in range(0, 1000) else "orange" if elev in range(1000, 3000) else "red")

map.create_map(path="test_map.html")
