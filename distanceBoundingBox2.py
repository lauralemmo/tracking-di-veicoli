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

        dx = (abs(abs(y2[0]) - l / 2))**2
        dy = (abs(abs(y2[1]) - w / 2))**2
        dz = (abs(abs(y2[2]) - h / 2))**2

        distance = np.sqrt(dx**2 + dy**2 + dz**2)

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
        result = minimize(self.sommatoria, parametriDaOttimizzare, args=(tabella,), method='L-BFGS-B')

        print("valore funzione obiettivo: ", result.fun)
        print("distanza media da ogni punto: ", result.fun / i)
        print("Valori ottimizzati:", result.x)