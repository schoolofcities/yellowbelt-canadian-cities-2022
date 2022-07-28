import pandas as pd
import geopandas as gpd

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

def assign_zone(LU_z):
	if LU_z == 3:
		zone_type = "MU"
	elif LU_z == 2:
		zone_type = "OR"
	elif LU_z == 1:
		zone_type = "SD"
	else:
		zone_type = None
	return zone_type

dfcd["zone_type"] = dfcd["LU_z"].apply(assign_zone)

# dfcd.to_csv("zoning-districts-CD-categorized.csv")

print(dfcd["object_id","zone_type"])

dfcd[""]