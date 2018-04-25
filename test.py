from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
import landmarks

landmarks_file = 'data/landmarks.csv'
if Path(landmarks_file).exists():
    landmarks = pd.read_csv('data/landmarks.csv', index_col=0)
else:
    landmarks = landmarks.calculate()
cols = ['p1e', 'pase1', 'ose', 'pase2', 'p2e']
print(landmarks[cols].sort_index(by=['x']))

x = np.array(landmarks[cols].loc['x'])
y = np.array(landmarks[cols].loc['y'])


# x = np.linspace(0, 10, 10)
# y = np.sin(x)
spl = interpolate.splrep(x, y)
x2 = np.linspace(0, 10, 200)
y2 = interpolate.splev(x2, spl)
plt.plot(x, y, 'o', x2, y2)
plt.show()
