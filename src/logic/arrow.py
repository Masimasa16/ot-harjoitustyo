import numpy as np


from .polygon import rotation_matrix
from .polygon import Polygon


BASIC_ARROW = 20 * np.array([
    [0, -1],
    [0, 1],
    [3, 1],
    [2, 3],
    [6, 0],
    [2, -3],
    [3, -1]
])


class Arrow(Polygon):
    def __init__(self, center, theta):
        self.center = center

        self.index = theta//30

        r_matrix = rotation_matrix(theta)
        points = []
        for point in BASIC_ARROW:
            rotated_point = r_matrix @ point + center
            points.append(rotated_point)

        super().__init__(points)

    def click(self, point, tile):
        if self.point_in_polygon(point):
            tile.move(self.index)


def create_arrows(theta, scalar):
    theta_rad = np.radians(theta)
    delta_theta = np.radians(60)
    return [
        Arrow([scalar*np.cos(delta_theta*i + theta_rad), scalar*np.sin(delta_theta*i+theta_rad)], +
              60*i + theta) for i in range(6)
    ]
