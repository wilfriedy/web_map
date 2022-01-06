import folium
map = folium.Map(location= [6.437648626493493, 3.4847853009845253] , zoom_start=10)
fg = folium.FeatureGroup(name = "Map")
# for i in range(10):
#     fg.add_child(folium.Marker(location=[34 + i , -89 - i], popup=str(i) , icon= folium.Icon(color='red')))
#     print(i)
fg.add_child(folium.Marker(location=[6.437659287678129, 3.4845921819431758], popup="Hello" , icon= folium.Icon(color='red')))

map.add_child(fg)
map.save("map.html")