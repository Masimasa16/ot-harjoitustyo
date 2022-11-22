import unittest
import numpy as np
from index import Hex
from index import RADIUS


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.hex = Hex(RADIUS, [0,0])

    def test_move(self):
        vector = [3, 4]
        self.hex.move(vector)

        points = np.array([
            [RADIUS*(np.sqrt(3)/2 + 3), RADIUS*(1/2 + 4)],
            [RADIUS*(0 + 3), RADIUS*(1 + 4)],
            [RADIUS*(-np.sqrt(3)/2 + 3), RADIUS*(1/2 + 4)],
            [RADIUS*(-np.sqrt(3)/2 + 3), RADIUS*(-1/2 + 4)],
            [RADIUS*(0 + 3), RADIUS*(-1 + 4)],
            [RADIUS*(np.sqrt(3)/2 + 3), RADIUS*(-1/2 + 4)]
        ])

        res = np.allclose(self.hex.points, points) and np.allclose(self.hex.dist_center, [RADIUS*3, RADIUS*4])

        self.assertEqual(res, True)
