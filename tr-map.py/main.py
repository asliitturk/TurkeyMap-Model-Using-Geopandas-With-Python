import geopandas as gpd
import matplotlib.pyplot as plt

def coloring_map(output_path="map-pic/turkey_map.png"):
    # upload the shapefile containing the provincial borders of Turkey.
    # Edit the file path according to your preference
    turkey_gdf = gpd.read_file("C:/asliitturk/x/x/tr-map.py/gadm41_TUR_shp/gadm41_TUR_1.shp") 
    
    #### error / hata:  
    # tr-map.py\main.py:14: UserWarning: Geometry is in a geographic CRS...
    #### solution / çözüm :
    ##  turkey_gdf = turkey_gdf.to_crs(epsg=3857)
    
    for x, y, label in zip(turkey_gdf.geometry.centroid.x, turkey_gdf.geometry.centroid.y, turkey_gdf["NAME_1"]):    
     turkey_gdf["color"] = ["firebrick" for _ in range(len(turkey_gdf))]  # illerin rengi

    fig, ax = plt.subplots(1, 1, figsize=(50, 30))  
    turkey_gdf.plot(ax=ax, color=turkey_gdf["color"], edgecolor="rosybrown") # illerin çerçeve rengi (sınırlar/çizgiler)

    for x, y, label in zip(turkey_gdf.geometry.centroid.x, turkey_gdf.geometry.centroid.y, turkey_gdf["NAME_1"]):  
        ax.text(x, y, label, fontsize=24, ha="center", color="burlywood")   # illerin isimleri

    plt.axis("off")  # Eksen off
    plt.savefig(output_path, format="png", dpi=300)  # PNG 
    plt.show()


coloring_map()