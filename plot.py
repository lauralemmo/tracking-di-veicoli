import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from distanceBoundingBox import BoundingBox
from distanceBoundingBox2 import BoundingBox2


def plotFObiettivo():
    fObiettivo1 = []
    fObiettivo2 = []
    file_paths = ['PointCloud_1Sensore/PointCloud_traj_argo_50_AV_MercedesGLS580_scans50_s7_h2_5_10_vehicle_time_{}.csv'.format(k) for k in range(1, 51)]
    for k in range(0, len(file_paths), 5):
        tabellaA = pd.read_csv(file_paths[k])
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
        a = box1.ottimizzazione(parametriInizialiA, tabellaA, i)
        fObiettivo1.append(a)
        print("\n \n \n")
        b = box2.ottimizzazione(parametriInizialiA, tabellaA, i)
        fObiettivo2.append(b)
        print("\n \n \n")


    print("\n \n \n")
    fObiettivo3 = []
    fObiettivo4 = []
    file_paths = ['PointCloud_nSensori/PointCloud_traj_argo_50_AV_MercedesGLS580_scans50_s7_h2_5_10_v3_vehicle_time_{}.csv'.format(k) for k in range(1, 51)]
    for k in range(0, len(file_paths), 5):
        tabellaB = pd.read_csv(file_paths[k])
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
        c = box1.ottimizzazione(parametriInizialiB, tabellaB, i)
        fObiettivo3.append(c)
        print("\n \n \n")
        d = box2.ottimizzazione(parametriInizialiB, tabellaB, i)
        fObiettivo4.append(d)
        print("\n \n \n")


    x = np.arange(1, 51, 5)
    y = fObiettivo1
    plt.plot(x, y, color="red")
    plt.title('1 sensore, primo metodo')
    plt.xlabel('istanti di tempo')
    plt.ylabel('distanza media da ogni punto')
    plt.show()

    x = np.arange(1, 51, 5)
    y = fObiettivo2
    plt.plot(x, y, color="blue")
    plt.title('1 sensore, secondo metodo')
    plt.xlabel('istanti di tempo')
    plt.ylabel('distanza media da ogni punto')
    plt.show()

    x = np.arange(1, 51, 5)
    y = fObiettivo3
    plt.plot(x, y, color="green")
    plt.title('n sensori, primo metodo')
    plt.xlabel('istanti di tempo')
    plt.ylabel('distanza media da ogni punto')
    plt.show()

    x = np.arange(1, 51, 5)
    y = fObiettivo4
    plt.plot(x, y, color="pink")
    plt.title('n sensori, secondo metodo')
    plt.xlabel('istanti di tempo')
    plt.ylabel('distanza media da ogni punto')
    plt.show()







def plotTradeOff():
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


    print("ottimizzazione con point cloud data da un solo sensore")
    print("parametri iniziali: ", parametriInizialiA)
    parametriOttimizzati1 = box1.ottimizzazione(parametriInizialiA, tabellaA, i)
    print("\n \n \n")




    print("\n \n \n")




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


    print("ottimizzazione con point cloud data da n sensori")
    print("parametri iniziali: ", parametriInizialiB)
    parametriOttimizzati3 = box1.ottimizzazione(parametriInizialiB, tabellaB, i)
    print("\n \n \n")