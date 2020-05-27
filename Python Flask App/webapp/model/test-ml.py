import pandas as pd
df_icmrlab = pd.read_csv("C:/Users/h/Downloads/ICMRLabDetails.csv")


import pgeocode
nomi = pgeocode.Nominatim('in')
df_query = nomi.query_postal_code(query)
lat = df_query.latitude
lon = df_query.longitude
query_point = (lat,lon,0.0)



import geopy.distance



index = 0
count = 0
min_dis = float("inf")
for itr in df_icmrlab['location']:
    res = itr[1:-1]
    res = tuple(map(float, res.split(',')))
    dis = geopy.distance.geodesic(query_point, res).km
    if dis<min_dis:
        min_dis = dis
        index = count
    count+=1
print(min_dis)

near_lab = df_icmrlab.loc[index,'address']

