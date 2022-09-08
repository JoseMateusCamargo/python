import folium

coord = [-23.093206, -46.962137]

map_ = folium.Map(location=coord, titles='Rodovia Romildo Prado', zoom_start=16)
folium.Marker(coord, popup='<i>Rodovia Romildo Prado</i>', tooltip='Clique aqui').add_to(map_)

map_.save('maps_using_folium.html')
