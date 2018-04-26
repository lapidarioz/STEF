import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import landmarks
from data.facial_features_points import facial_features, pupils


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


def plot_circle(point, radius, show_points=False):
    circle = plt.Circle(point, radius.loc['x'],
                        linestyle='solid',
                        linewidth=2,
                        fill=False,
                        edgecolor='b')
    if show_points:
        plt.plot(point.loc['x'], point.loc['x'], 'ro')
    plt.gca().add_patch(circle)


def main():
    points = landmarks.calculate()
    for feature_name, feature_points in facial_features.items():
        plot_spline(points[feature_points])

    for feature_points in pupils['positions']:
        plot_circle(points[feature_points], points[pupils['radius']])
    plt.axis('off')
    plt.gca().invert_yaxis()
    plt.savefig("results/face.svg")


if __name__ == '__main__':
    main()

