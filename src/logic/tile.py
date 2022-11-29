import numpy as np
from .polygon import Polygon

HEX_MOVE_VECTORS = np.array([
    [np.cos(np.radians(30*i)), np.sin(np.radians(30*i))] for i in range(12)
])

MOVES = [
    [1, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 1],
    [-1, 0, 0],
    [-1, 0, 0],
    [0, -1, 0],
    [0, -1, 0],
    [0, 0, -1],
    [0, 0, -1]

]


class Hex(Polygon):
    def __init__(self, points_dist_center, center):

        points = []
        theta = np.radians(60)
        for i in range(6):
            x_pos = points_dist_center * \
                np.cos(i*theta + np.radians(30)) + points_dist_center*center[0]
            y_pos = points_dist_center * \
                np.sin(i*theta + np.radians(30)) + points_dist_center*center[1]
            points.append([x_pos, y_pos])

        self.points_dist_center = points_dist_center

        self.moves = [0, 0, 0]

        self.valid_indexes = [0, 2, 4, 6, 8, 10]

        super().__init__(points)

    def move(self, vector):
        if vector in self.valid_indexes:
            self.moves += MOVES[vector]
            super().move(HEX_MOVE_VECTORS[vector]
                         * 2*(self.points_dist_center - 4))

    def check_cordinates(self, grid):
        if grid[self.moves[0]][self.moves[1]][self.moves[2]] == 0:
            return True
        return False

    def place(self, grid):
        grid[self.moves[0]][self.moves[1]][self.moves[2]] = 1


class Tile:
    def __init__(self, radius):
        vectors = np.array([
            [0.0, 0.0],
            [np.sqrt(3)/2, 3/2],
            [np.sqrt(3), 0.0],
            [np.sqrt(3)/2, -3/2]
        ])

        self.hexes = [
            Hex(radius, vector) for vector in vectors
        ]

    def move(self, index):
        for hexagon in self.hexes:
            hexagon.move(index)

    def rotate(self, theta):
        for hexagon in self.hexes:
            hexagon.rotate(theta)

    def place(self, grid):
        if all(hexagon.check_cordinates(grid) for hexagon in self.hexes):
            for hexagon in self.hexes:
                hexagon.place(grid)
            return True
        return False

    def point_in_tile(self, point):
        if any(hexagon.point_in_polygon(point) for hexagon in self.hexes):
            return True
        return False
