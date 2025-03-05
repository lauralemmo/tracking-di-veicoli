#import open3d as o3d
#import numpy as np
#import pandas as pd


# def visualize(csv_file):
#     # Caricare il file CSV
#     df = pd.read_csv(csv_file)
#
#     # Rimuove righe con valori NaN nelle colonne x, y, z
#     df = df.dropna(subset=["x", "y", "z"])
#
#     # Assumiamo che il CSV abbia tre colonne: "x", "y", "z"
#     points = df[["x", "y", "z"]].to_numpy()
#
#     # Creare una nuvola di punti
#     pcd = o3d.geometry.PointCloud()
#     pcd.points = o3d.utility.Vector3dVector(points)
#
#     # Visualizzare la nuvola di punti
#     o3d.visualization.draw_geometries([pcd])




import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial.transform import Rotation as R

def visualize2(csv_file, parametri):

    # Caricamento dati
    df = pd.read_csv(csv_file)  # Assumi che il file contenga colonne x, y, z

    # Creazione del parallelepipedo unitario centrato nell'origine
    unit_cube = np.array([
        [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5, 0.5, -0.5], [-0.5, 0.5, -0.5],
        [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5], [0.5, 0.5, 0.5], [-0.5, 0.5, 0.5]
    ])

    # Scalatura alle dimensioni effettive
    size = np.array([parametri[4], parametri[5], parametri[6]])
    vertices = unit_cube * size

    # Rotazione attorno all'asse Z
    rotation = R.from_euler('z', parametri[3], degrees=True)
    vertices = rotation.apply(vertices)

    # Traslazione nella posizione finale
    pos = np.array([parametri[0], parametri[1], parametri[2]])
    vertices += pos

    # Definizione delle facce del parallelepipedo
    faces = [[vertices[j] for j in face] for face in [
        [0, 1, 2, 3], [4, 5, 6, 7],  # Base inferiore e superiore
        [0, 1, 5, 4], [2, 3, 7, 6],  # Lati anteriori e posteriori
        [0, 3, 7, 4], [1, 2, 6, 5]  # Lati sinistro e destro
    ]]

    # Creazione della figura 3D
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Plot dei punti della tabella
    ax.scatter(df['x'], df['y'], df['z'], c='b', marker='o', label="Punti")

    # Plot del parallelepipedo
    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', edgecolors='k', alpha=0.3))

    # Etichette assi
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.legend()
    plt.show()
