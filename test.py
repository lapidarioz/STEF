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
cols = ['p2e', 'pase2', 'ose', 'pase1', 'p1e', ]
print(landmarks[cols])

x = np.array(landmarks[cols].loc['x'])
y = np.array(landmarks[cols].loc['y'])


l=len(x)

t=np.linspace(0,1,l-2,endpoint=True)
t=np.append([0,0,0],t)
t=np.append(t,[1,1,1])

tck=[t,[x,y],3]
u3=np.linspace(0,1,(max(l*2,70)),endpoint=True)
out = interpolate.splev(u3,tck)

plt.plot(x,y,'k--',label='Control polygon',marker='o',markerfacecolor='red')
#plt.plot(x,y,'ro',label='Control points only')
plt.plot(out[0],out[1],'b',linewidth=2.0,label='B-spline curve')
plt.legend(loc='best')
plt.ylim(max(y)+20, 0)
plt.title('Cubic B-spline curve evaluation')
plt.show()

# tck,u = interpolate.splprep([x,y],k=3,s=0)
# u=np.linspace(0,1,num=50,endpoint=True)
# out = interpolate.splev(u,tck)
#
# plt.figure()
# plt.plot(x, y, 'ro', out[0], out[1], 'b')
# plt.legend(['Points', 'Interpolated B-spline', 'True'],loc='best')
# plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
# plt.title('B-Spline interpolation')
# plt.ylim(max(y)+20, 0)
# plt.show()
