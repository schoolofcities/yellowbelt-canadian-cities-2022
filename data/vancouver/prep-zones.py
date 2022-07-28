import pandas as pd
import geopandas as gpd

# just the CD zones

union = gpd.read_file("data/zoning-districts-CD-LU-union.shp")

union = union[["object_id","Descriptio"]].sort_values("object_id")

union["LU_z"] = 0

def assign_type(land_use):	
	LU_z = 0
	if land_use in ["Mixed Residential (Low-rise Apartment) Commercial", "Mixed Residential (Mid/High-Rise Apartment) Commercial"]:
		LU_z = 3
	elif land_use in ["Residential - Institutional and Non-Market Housing", "Residential - Low-rise Apartment", "Residential - Mid/High-rise Apartment", "Residential - Townhouse"]:
		LU_z = 2
	elif land_use in ["Residential - Single Detached", "Residential - Mobile Homes"]:
		LU_z = 1
	else:
		LU_z = 0
	return LU_z

union["LU_z"] = union["Descriptio"].apply(assign_type)

dfcd = pd.DataFrame(union.groupby('object_id')["LU_z"].max())

def assign_zone_from_LUz(LU_z):
	if LU_z == 3:
		zone_type = "MU"
	elif LU_z == 2:
		zone_type = "OR"
	elif LU_z == 1:
		zone_type = "SD"
	else:
		zone_type = "None"
	return zone_type

dfcd["zone_type"] = dfcd["LU_z"].apply(assign_zone_from_LUz)

dfcd.index.name = 'object_id'
dfcd.reset_index(inplace=True)
dfcd = dfcd[["object_id","zone_type"]]


# all other zones 

zones = gpd.read_file("data/zoning-districts-and-labels.shp")

dfz = zones[zones["zoning_clas"] != "Comprehensive Development"]

def assign_zone_from_districts(district):
	if district in ["RS","RA","FSHCA"]:
		zone_type = "SD"
	elif district in ["RT","RM","FM"]:
		zone_type = "OR"
	elif district in ["HA","FC","C","DD","DEOD","FCCDD"]:
		zone_type = "MU"
	else:
		zone_type = "None"
	return zone_type

dfz["zone_type"] = dfz["zoning_cate"].apply(assign_zone_from_districts)

dfz = dfz[["object_id","zone_type"]]


# combine the two 

df = pd.concat([dfcd, dfz], axis=0)

print(df)

df.to_csv("data/zones_with_categories.csv")
