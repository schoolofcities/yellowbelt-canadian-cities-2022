import pandas as pd
import geopandas as gpd

file_in = "toronto/data/Zoning Area.geojson"
field = "ZN_ZONE"
d = {
	"SD": {"RD"},
	"RO": {"R","RA", "RM", "RS", "RS"},
	"MU": {"RAC", "CR", "CRE"}
}
utm = "epsg:32617"

gdf = gpd.read_file(file_in)

# add categories
newdict = {i: k for k, v in d.items() for i in v}
gdf["zone_type"] = gdf[field].str.findall('|'.join(newdict.keys())).str[0].map(newdict)

# compute area
gdf = gdf.to_crs({'init': utm})
gdf["area"] = gdf['geometry'].area / 10**6

df = gdf.groupby(['zone_type'])['area'].sum().reset_index()
df["area_p"] = 100 * df["area"] / df["area"].sum()
print(df)