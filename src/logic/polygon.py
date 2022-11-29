import numpy as np


def rotation_matrix(theta):
    theta_radians = np.radians(theta)
    return np.array([
        [np.cos(theta_radians), -np.sin(theta_radians)],
        [np.sin(theta_radians), np.cos(theta_radians)]
    ])


class Polygon:
    def __init__(self, points):
        self.points = np.array(points)

        self.center_vector = np.array([0.0, 0.0])

    @property
    def edges(self):
        res = []
        for point, next_point in zip(self.points, self.points[1:]):
            res.append([point, next_point])
        res.append([self.points[-1], self.points[0]])
        return res

    def move(self, vector):
        self.center_vector += vector
        self.points += vector

    def rotate(self, theta):
        r_matrix = rotation_matrix(theta)
        for i, point in enumerate(self.points):
            self.points[i] = r_matrix @ (point - self.center_vector) + \
                self.center_vector

    def point_in_polygon(self, point, epsilon=3):
        # epsilon is error term as pixels
        x_pos = point[0]
        y_pos = point[1]

        min_x = min(p[0] for p in self.points)
        max_x = max(p[0] for p in self.points)
        min_y = min(p[1] for p in self.points)
        max_y = max(p[1] for p in self.points)

        if (x_pos < min_x or x_pos > max_x) or (y_pos < min_y or y_pos > max_y):
            return False

        count = 0
        for (point1, point2) in self.edges:
            min_y, max_y = min(point1[1], point2[1]), max(point1[1], point2[1])
            if min_y < y_pos < max_y:
                delta_x = point1[0] - point2[0]
                delta_y = point1[1] - point2[1]
                if x_pos < (delta_x/delta_y)*(y_pos - point1[1]) + point1[0] + epsilon:
                    count += 1
        if count % 2 == 1:
            return True
        return False

    def __str__(self):
        return str(self.points)
