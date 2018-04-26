from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate
import landmarks


def plot_spline(points):
    x = np.array(points.loc['x'])
    y = np.array(points.loc['y'])

    l = len(x)

    t = np.linspace(0, 1, l - 2, endpoint=True)
    t = np.append([0, 0, 0], t)
    t = np.append(t, [1, 1, 1])

    tck = [t, [x, y], 3]
    u3 = np.linspace(0, 1, (max(l * 2, 70)), endpoint=True)
    out = interpolate.splev(u3, tck)

    plt.plot(x, y, 'ro')
    plt.plot(out[0], out[1], 'b', linewidth=2.0)
    plt.legend(loc='best')
    plt.ylim(max(y) + 20, 0)


def main():
    points = landmarks.calculate()
    facial_features = pd.read_csv('data/facial_features_points.csv', index_col=0, header=None)
    for feature_name, feature_points in facial_features.iterrows():
        plot_spline(points[feature_points])
    # right_eyebrow.reverse()
    # print(right_eyebrow)
    # plt.axis('off')
    plt.show()


if __name__ == '__main__':
    main()
