import numpy as np

from macchina import BoundingBox
import pandas as pd


#QUESTO è TUTTO E SOLO PER IL TEMPO t=1, QUINDI LA PRIMA TABELLA DELLE 50 !!!!!!!!!!!!!


#ottimizzazione con point cloud data da un solo sensore

tabella1A = pd.read_csv("PointCloud_1Sensore/PointCloud_traj_argo_50_AV_MercedesGLS580_scans50_s7_h2_5_10_vehicle_time_1.csv")
coordinata_x = 0
coordinata_y = 0
coordinata_z = 0
i = 0
for _, row in tabella1A.iterrows():
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
for _, row in tabella1A.iterrows():
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





print("ottimizzazione con point cloud data da un solo sensore")
print("parametri iniziali: ", parametriInizialiA)
box1.ottimizzazione(parametriInizialiA, tabella1A, i)


#print(tabella1A.head())
#
# prima_riga = tabella1A.iloc[0]
# primaRigaArray = np.array(prima_riga)
# box1.distanza(primaRigaArray, position, orientation, shape)
#
# seconda_riga = tabella1A.iloc[1]
# secondaRigaArray = np.array(seconda_riga)
# box1.distanza(secondaRigaArray, position, orientation, shape)
#
# box1.sommatoria(parametriIniziali, tabella1A)





print("\n \n \n")




#ottimizzazione con point cloud data da n sensori

tabella1B = pd.read_csv("PointCloud_nSensorI/PointCloud_traj_argo_50_AV_MercedesGLS580_scans50_s7_h2_5_10_v3_vehicle_time_1.csv")
coordinata_x = 0
coordinata_y = 0
coordinata_z = 0
i = 0
for _, row in tabella1B.iterrows():
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
for _, row in tabella1B.iterrows():
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


print("ottimizzazione con point cloud data da n sensori")
print("parametri iniziali: ", parametriInizialiB)
box1.ottimizzazione(parametriInizialiB, tabella1B, i)





#QUA FARò PER GLI ALTRI TEMPI, DA 2 A 50