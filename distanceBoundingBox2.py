import numpy as np
from scipy.optimize import minimize

class BoundingBox2:
    def __init__(self, name):
        self.name = name




    def distanza(self, y, p, o, s):
        l, w, h = s

        y = np.array(y)
        p = np.array(p)

        y1 = y - p

        rMatrix = np.array([ [np.cos(-o), -np.sin(-o), 0],
                            [np.sin(-o),  np.cos(-o), 0],
                            [0, 0, 1] ])

        y2 = rMatrix @ y1

        dx = abs(y2[0]) - l / 2
        dy = abs(y2[1]) - w / 2
        dz = abs(y2[2]) - h / 2

        if (dx <= 0) and (dy <= 0) and (dz <= 0):  #punto interno alla bounding box
            distance = min(dx**2, dy**2, dz**2)
        else:  #punto esterno alla bounding box
            Dx = max(dx, 0)
            Dy = max(dy, 0)
            Dz = max(dz, 0)
            distance = (Dx**2 + Dy**2 + Dz**2)


        return distance




    def sommatoria(self, parametriDaOttimizzare, tabella):
        p = np.array([parametriDaOttimizzare[0], parametriDaOttimizzare[1], parametriDaOttimizzare[2]])
        o = parametriDaOttimizzare[3]
        s = np.array([parametriDaOttimizzare[4], parametriDaOttimizzare[5], parametriDaOttimizzare[6]])

        sum = 0

        for _, row in tabella.iterrows():
            if row.isnull().any():
                continue
            point = (row['x'], row['y'], row['z'])
            sum += self.distanza(point, p, o, s)


        print("distanza: ", sum)
        return sum




    def ottimizzazione(self, parametriDaOttimizzare, tabella, i):
        bounds = [
            (np.nanmin(tabella['x']), np.nanmax(tabella['x'])),  # Limiti posizione X
            (np.nanmin(tabella['y']), np.nanmax(tabella['y'])),  # Limiti posizione Y
            (np.nanmin(tabella['z']), np.nanmax(tabella['z'])),  # Limiti posizione Z
            (-np.pi, np.pi),  # Limiti angolo di rotazione
            (0.1, np.nanmax(tabella['x']) - np.nanmin(tabella['x'])),  # Lunghezza
            (0.1, np.nanmax(tabella['y']) - np.nanmin(tabella['y'])),  # Larghezza
            (0.1, np.nanmax(tabella['z']) - np.nanmin(tabella['z']))  # Altezza
        ]
        print("bounds = ", bounds)
        result = minimize(self.sommatoria, parametriDaOttimizzare, args=(tabella,), method='L-BFGS-B',
                          bounds=bounds, options={'ftol': 1e-3, 'gtol': 1e-3, 'maxiter': 300, 'maxfun': 300})

        print("valore funzione obiettivo: ", result.fun)
        print("distanza media da ogni punto: ", result.fun / i)
        print("Valori ottimizzati:", result.x)

        return result.x