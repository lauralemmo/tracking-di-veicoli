import numpy as np
import open3d as o3d
import pandas as pd

from plot import *
from distanceBoundingBox import BoundingBox
from distanceBoundingBox2 import BoundingBox2
from visualization import visualize2




#ottimizzazione con point cloud data da un solo sensore


#cartellaA = Path("PointCloud_1Sensore")
#for file in cartellaA.glob("*.csv"):
tabellaA = pd.read_csv("PointCloud_1Sensore/PointCloud_traj_argo_50_AV_MercedesGLS580_scans50_s7_h2_5_10_vehicle_time_1.csv")
coordinata_x = 0
coordinata_y = 0
coordinata_z = 0
i = 0
for _, row in tabellaA.iterrows():
    if row.isnull().any():
        continue
    coordinata_x += row['x']
    coordinata_y += row['y']
    coordinata_z += row['z']
    i += 1

media_x = coordinata_x / i
media_y = coordinata_y / i
media_z = coordinata_z / i


lunghezza = 0
larghezza = 0
altezza = 0
for _, row in tabellaA.iterrows():
    if row.isnull().any():
        continue
    if lunghezza < abs(media_x - row['x']):
        lunghezza = abs(media_x - row['x'])
    if larghezza < abs(media_y - row['y']):
        larghezza = abs(media_y - row['y'])
    if altezza < abs(media_z - row['z']):
        altezza = abs(media_z - row['z'])


x = media_x
y = media_y
z = media_z
o = 0
l1 = lunghezza * 2
l2 = larghezza * 2
h = altezza * 2

parametriInizialiA = np.array([x, y, z, o, l1, l2, h])


box1 = BoundingBox('box1')
box2 = BoundingBox2('box2')


print("ottimizzazione con point cloud data da un solo sensore")
print("parametri iniziali: ", parametriInizialiA)
parametriOttimizzati1 = box1.ottimizzazione(parametriInizialiA, tabellaA, i)
print("\n \n \n")
parametriOttimizzati2 = box2.ottimizzazione(parametriInizialiA, tabellaA, i)
print("\n \n \n")




print("\n \n \n")







#ottimizzazione con point cloud data da n sensori


#cartellaB = Path("PointCloud_nSensori")
#for file in cartellaB.glob("*.csv"):
tabellaB = pd.read_csv("PointCloud_nSensori/PointCloud_traj_argo_50_AV_MercedesGLS580_scans50_s7_h2_5_10_v3_vehicle_time_1.csv")

coordinata_x = 0
coordinata_y = 0
coordinata_z = 0
i = 0
for _, row in tabellaB.iterrows():
    if row.isnull().any():
        continue
    coordinata_x += row['x']
    coordinata_y += row['y']
    coordinata_z += row['z']
    i += 1

media_x = coordinata_x / i
media_y = coordinata_y / i
media_z = coordinata_z / i

lunghezza = 0
larghezza = 0
altezza = 0
for _, row in tabellaB.iterrows():
    if row.isnull().any():
        continue
    if lunghezza < abs(media_x - row['x']):
        lunghezza = abs(media_x - row['x'])
    if larghezza < abs(media_y - row['y']):
        larghezza = abs(media_y - row['y'])
    if altezza < abs(media_z - row['z']):
        altezza = abs(media_z - row['z'])

x = media_x
y = media_y
z = media_z
o = 0
l1 = lunghezza * 2
l2 = larghezza * 2
h = altezza * 2

parametriInizialiB = np.array([x, y, z, o, l1, l2, h])


box1 = BoundingBox('box1')
box2 = BoundingBox2('box2')


print("ottimizzazione con point cloud data da n sensori")
print("parametri iniziali: ", parametriInizialiB)
parametriOttimizzati3 = box1.ottimizzazione(parametriInizialiB, tabellaB, i)
print("\n \n \n")
parametriOttimizzati4 = box2.ottimizzazione(parametriInizialiB, tabellaB, i)
print("\n \n \n")





#visualizzazioni

#prima dell'ottimizzazione
csv_path = "PointCloud_1Sensore/PointCloud_traj_argo_50_AV_MercedesGLS580_scans50_s7_h2_5_10_vehicle_time_1.csv"
visualize2(csv_path, parametriInizialiA)

csv_path = "PointCloud_nSensori/PointCloud_traj_argo_50_AV_MercedesGLS580_scans50_s7_h2_5_10_v3_vehicle_time_1.csv"
visualize2(csv_path, parametriInizialiB)

#dopo l'ottimizzazione
csv_path = "PointCloud_1Sensore/PointCloud_traj_argo_50_AV_MercedesGLS580_scans50_s7_h2_5_10_vehicle_time_1.csv"
visualize2(csv_path, parametriOttimizzati1) #primo metodo
visualize2(csv_path, parametriOttimizzati2) #secondo metodo

csv_path = "PointCloud_nSensori/PointCloud_traj_argo_50_AV_MercedesGLS580_scans50_s7_h2_5_10_v3_vehicle_time_1.csv"
visualize2(csv_path, parametriOttimizzati3) #primo metodo
visualize2(csv_path, parametriOttimizzati4) #secondo metodo




#plotFObiettivo()



#plotTradeOff()