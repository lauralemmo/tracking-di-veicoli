from macchina import BoundingBox
import pandas as pd

x = 8
y = 6
z = 5
o = 0
l1 = 10
l2 = 6
h = 2

parametriIniziali = [x, y, z, o, l1, l2, h]


box1 = BoundingBox('box1')




#ottimizzazione con point cloud data da un solo sensore
print("ottimizzazione con point cloud data da un solo sensore")
tabella1A = pd.read_csv("PointCloud_1Sensore/PointCloud_traj_argo_50_AV_MercedesGLS580_scans50_s7_h2_5_10_vehicle_time_1.csv")
box1.ottimizzazione(parametriIniziali, tabella1A)


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
print("ottimizzazione con point cloud data da n sensori")
tabella1B = pd.read_csv("PointCloud_nSensorI/PointCloud_traj_argo_50_AV_MercedesGLS580_scans50_s7_h2_5_10_v3_vehicle_time_1.csv")
box1.ottimizzazione(parametriIniziali, tabella1B)