from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate
import landmarks
from data.facial_features_points import facial_features


def plot_spline(points, show_points=False):
    # points = points.iloc[:, np.argsort(points.loc['x'])]
    x = np.array(points.loc['x'])
    y = np.array(points.loc['y'])

    tck, u = interpolate.splprep([x, y], k=len(x)-1, s=0)
    u = np.linspace(0, 1, num=50, endpoint=True)
    x2, y2 = interpolate.splev(u, tck)

    if show_points:
        plt.plot(x, y, 'ro')
    plt.plot(x2, y2, 'b')


def main():
    points = landmarks.calculate()
    for feature_name, feature_points in facial_features.items():
        plot_spline(points[feature_points])
    # right_eyebrow.reverse()
    # print(right_eyebrow)
    # plt.axis('off')
    x = points.loc['x']
    y = points.loc['y']
    # plt.axis([x.min() - 1, x.max() + 1, y.max() + 1, y.min() - 1])
    plt.show()


if __name__ == '__main__':
    main()

