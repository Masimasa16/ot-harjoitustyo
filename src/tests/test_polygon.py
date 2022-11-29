import unittest
import numpy as np
import math

from logic import Polygon

POINTS = [
    [-10.0, 0.0],
    [10.0, 0.0],
    [10.0, 20.0],
    [-10.0, 20.0]
]


class TestPolygon(unittest.TestCase):
    def setUp(self):
        self.polygon = Polygon(POINTS)

    def test_edges(self):
        res_val = [
            [[-10.0, 0.0], [10.0, 0.0]],
            [[10.0, 0.0], [10.0, 20.0]],
            [[10.0, 20.0], [-10.0, 20.0]],
            [[-10.0, 20.0], [-10.0, 0.0]]
        ]

        res = True
        for edge, val in zip(self.polygon.edges, res_val):
            for (x, y), (x_res, y_res) in zip(edge, val):
                if not (math.isclose(x, x_res) and (y, y_res)):
                    res = False

        self.assertEqual(res, True)

    def test_move(self):
        vector = [10, 0]
        self.polygon.move(vector)

        res = np.allclose(self.polygon.points, [
            [0.0, 0.0],
            [20.0, 0.0],
            [20.0, 20.0],
            [0.0, 20.0]
        ])

        self.assertEqual(res, True)

    def test_rotate(self):
        self.polygon.rotate(90)

        res = np.allclose(self.polygon.points, [
            [0.0, -10.0],
            [0.0, 10.0],
            [-20.0, 10.0],
            [-20.0, -10.0]
        ])

        self.assertEqual(res, True)

    def test_point_not_in_polygon(self):
        point = [-1, -1]
        self.assertEqual(self.polygon.point_in_polygon(point), False)

    def test_point_in_polygon(self):
        point = [5, 5]
        self.assertEqual(self.polygon.point_in_polygon(point), True)

    def test_str(self):
        self.assertEqual(str(self.polygon), str(np.array(POINTS)))
