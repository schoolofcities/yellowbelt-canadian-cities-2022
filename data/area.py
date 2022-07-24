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

file_in = "calgary/data/land-use.shp"
field = "LU_CODE"
d = {
	"SD": {"R-1","R-1N","R-1s","R-C1","R-C1L","R-C1Ls","R-C1N","R-C1s","R-MH"},
	"RO": {"CC-MH","M-1", "M-2", "M-C1", "M-C2","M-CG","M-G","M-H1","M-H2","M-H3","M-X1","M-X2","R-2","R-2M","R-C2","R-CG","R-CG-ex","R-G","R-Gm"},
	"MU": {"CC-EIR", "CC-EMU", "CC-EPR","CC-ER","CC-ERR","CC-ET","CC-MHX","CC-X","CR20-C20/R20","MU-1","MU-2"}
}
utm = "epsg:32612"

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