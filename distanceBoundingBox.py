import numpy as np
from scipy.optimize import minimize

class BoundingBox:
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

        dx = max(abs(y2[0]) - l / 2, 0)
        dy = max(abs(y2[1]) - w / 2, 0)
        dz = max(abs(y2[2]) - h / 2, 0)

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

        r = 0.7
        volume = s[0] * s[1] * s[2] * r

        print("distanza: ", sum)
        print("sommatoria: ", sum+volume)
        return sum + volume


    def ottimizzazione(self, parametriDaOttimizzare, tabella, i):
        o_init = parametriDaOttimizzare[3]  # Memorizziamo l'orientazione iniziale
        max_orient_variation = 5
        bounds = [
            (np.nanmin(tabella['x']), np.nanmax(tabella['x'])),  # Limiti posizione X
            (np.nanmin(tabella['y']), np.nanmax(tabella['y'])),  # Limiti posizione Y
            (np.nanmin(tabella['z']), np.nanmax(tabella['z'])),  # Limiti posizione Z
            (o_init - max_orient_variation, o_init + max_orient_variation),  # Limiti angolo di rotazione
            (0.1, np.nanmax(tabella['x']) - np.nanmin(tabella['x'])),  # Lunghezza
            (0.1, np.nanmax(tabella['y']) - np.nanmin(tabella['y'])),  # Larghezza
            (0.1, np.nanmax(tabella['z']) - np.nanmin(tabella['z']))  # Altezza
        ]
        result = minimize(self.sommatoria, parametriDaOttimizzare, args=(tabella,), method='L-BFGS-B',
                          bounds=bounds, options={'ftol': 1e-3, 'gtol': 1e-3, 'maxiter': 300, 'maxfun': 300})

        print("valore funzione obiettivo: ", result.fun)
        print("distanza media da ogni punto: ", result.fun / i)
        print("Valori ottimizzati:", result.x)

        return result.x
        #return result.fun / i


    def ottimizzazione2(self, parametriDaOttimizzare, tabella, r, i):     #serve con plotTradeOff
        o_init = parametriDaOttimizzare[3]  # Memorizziamo l'orientazione iniziale
        max_orient_variation = 5
        bounds = [
            (np.nanmin(tabella['x']), np.nanmax(tabella['x'])),  # Limiti posizione X
            (np.nanmin(tabella['y']), np.nanmax(tabella['y'])),  # Limiti posizione Y
            (np.nanmin(tabella['z']), np.nanmax(tabella['z'])),  # Limiti posizione Z
            (o_init - max_orient_variation, o_init + max_orient_variation),  # Limiti angolo di rotazione
            (0.1, np.nanmax(tabella['x']) - np.nanmin(tabella['x'])),  # Lunghezza
            (0.1, np.nanmax(tabella['y']) - np.nanmin(tabella['y'])),  # Larghezza
            (0.1, np.nanmax(tabella['z']) - np.nanmin(tabella['z']))  # Altezza
        ]
        result = minimize(self.sommatoria, parametriDaOttimizzare, args=(tabella, r,), method='L-BFGS-B',
                          bounds=bounds, options={'ftol': 1e-3, 'gtol': 1e-3, 'maxiter': 300, 'maxfun': 300})

        print("valore funzione obiettivo: ", result.fun)
        print("distanza media da ogni punto: ", result.fun / i)
        print("Valori ottimizzati:", result.x)

        return result.x