# import open3d as o3d
# import numpy as np
# import pandas as pd
#
#
# def visualize(csv_file):
#     # Caricare il file CSV
#     df = pd.read_csv(csv_file)
#
#     # Rimuove righe con valori NaN nelle colonne x, y, z
#     df = df.dropna(subset=["x", "y", "z"])
#
#     # Assumiamo che il CSV abbia tre colonne: "x", "y", "z"
#     points = df[["x", "y", "z"]].to_numpy()
#     print(points)
#     # Creare una nuvola di punti
#     pcd = o3d.geometry.PointCloud()
#     pcd.points = o3d.utility.Vector3dVector(points)
#
#     # Visualizzare la nuvola di punti
#     o3d.visualization.draw_geometries([pcd])




# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection
# from scipy.spatial.transform import Rotation as R
#
# def set_axes_equal(ax):
#     # permette di visualizzare il plot con le proporzioni corrette
#     x_limits = ax.get_xlim()
#     y_limits = ax.get_ylim()
#     z_limits = ax.get_zlim()
#
#     x_range = x_limits[1] - x_limits[0]
#     y_range = y_limits[1] - y_limits[0]
#     z_range = z_limits[1] - z_limits[0]
#     max_range = max(x_range, y_range, z_range) / 2.0
#
#     mid_x = np.mean(x_limits)
#     mid_y = np.mean(y_limits)
#     mid_z = np.mean(z_limits)
#
#     ax.set_xlim(mid_x - max_range, mid_x + max_range)
#     ax.set_ylim(mid_y - max_range, mid_y + max_range)
#     ax.set_zlim(mid_z - max_range, mid_z + max_range)
#
#
#
# def visualize2(csv_file, parametri):
#
#     # Caricamento dati
#     df = pd.read_csv(csv_file)
#
#     # Creazione del parallelepipedo unitario centrato nell'origine
#     unit_cube = np.array([
#         [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5, 0.5, -0.5], [-0.5, 0.5, -0.5],
#         [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5], [0.5, 0.5, 0.5], [-0.5, 0.5, 0.5]
#     ])
#
#     # Scalatura alle dimensioni effettive
#     size = np.array([parametri[4], parametri[5], parametri[6]])
#     vertices = unit_cube * size
#
#     # Rotazione attorno all'asse Z
#     rotation = R.from_euler('z', parametri[3], degrees=True)
#     vertices = rotation.apply(vertices)
#
#     # Traslazione nella posizione finale
#     pos = np.array([parametri[0], parametri[1], parametri[2]])
#     vertices += pos
#
#     # Definizione delle facce del parallelepipedo
#     faces = [[vertices[j] for j in face] for face in [
#         [0, 1, 2, 3], [4, 5, 6, 7],  # Base inferiore e superiore
#         [0, 1, 5, 4], [2, 3, 7, 6],  # Lati anteriori e posteriori
#         [0, 3, 7, 4], [1, 2, 6, 5]  # Lati sinistro e destro
#     ]]
#
#     # Creazione della figura 3D
#     fig = plt.figure(figsize=(8, 6))
#     ax = fig.add_subplot(111, projection='3d')
#
#     #ax.set_box_aspect([1, 1, 1])
#
#     # Plot del parallelepipedo
#     ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', edgecolors='k', alpha=0.3))
#
#     # Plot dei punti della tabella
#     #ax.scatter(df['x'], df['y'], df['z'], c='b', marker='o', label="Punti")
#     ax.scatter(df['x'], df['y'], df['z'], c=df['z'], cmap='rainbow', marker='o', label="Punti")
#
#
#
#     ax.view_init(0, 0)
#     #ax.view_init(0, 90)
#     #ax.view_init(0, 180)
#     #ax.view_init(0, -90)
#
#     # Etichette assi
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')
#
#     set_axes_equal(ax)
#
#     plt.legend()
#     plt.show()







import pandas as pd
import plotly.graph_objects as go
import numpy as np
from scipy.spatial.transform import Rotation as R


def visualize2(csv_file, parametri):
    # Caricamento dati
    df = pd.read_csv(csv_file)

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
    faces = [
        [vertices[j] for j in [0, 1, 2, 3]],  # Base inferiore
        [vertices[j] for j in [4, 5, 6, 7]],  # Base superiore
        [vertices[j] for j in [0, 1, 5, 4]],  # Lato 1
        [vertices[j] for j in [1, 2, 6, 5]],  # Lato 2
        [vertices[j] for j in [2, 3, 7, 6]],  # Lato 3
        [vertices[j] for j in [3, 0, 4, 7]]  # Lato 4
    ]

    # Crea la mesh del parallelepipedo
    parallelepipedo = go.Mesh3d(
        x=vertices[:, 0], y=vertices[:, 1], z=vertices[:, 2],
        color='cyan', opacity=0.3,  # Opacità per la trasparenza
        i=[0, 1, 2, 3, 0, 4, 5, 6, 7, 4, 5, 6],
        j=[1, 2, 3, 0, 4, 5, 6, 7, 4, 5, 6, 7],
        k=[2, 3, 0, 1, 5, 6, 7, 4, 0, 1, 2, 3]
    )

    # Crea la nuvola di punti
    nuvola_punti = go.Scatter3d(
        x=df['x'], y=df['y'], z=df['z'],
        mode='markers',
        marker=dict(size=3, color=df['z'], colorscale='rainbow', opacity=0.8)
    )

    # Disegna il grafico
    fig = go.Figure(data=[parallelepipedo, nuvola_punti])
    fig.update_layout(scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='data'  # Mantiene le proporzioni corrette
    ))

    fig.show()



def visualizePC(csv_file):
    # Caricamento dati
    df = pd.read_csv(csv_file)

    # Crea la nuvola di punti
    nuvola_punti = go.Scatter3d(
        x=df['x'], y=df['y'], z=df['z'],
        mode='markers',
        marker=dict(size=3, color=df['z'], colorscale='rainbow', opacity=0.8)
    )

    # Disegna il grafico
    fig = go.Figure(data=[nuvola_punti])
    fig.update_layout(scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='data'  # Mantiene le proporzioni corrette
    ))

    fig.show()
