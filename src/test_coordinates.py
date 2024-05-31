import math
import unittest

from src.common.coordinates import cartesianToPolar, cartesianToSpherical, polarToCartesian, sphericalToCartesian


class TestPolar(unittest.TestCase):

    def test_0(self):
        radius, theta = cartesianToPolar(0, 0)
        x, y = polarToCartesian(radius, theta)
        self.assertAlmostEqual(x, 0)
        self.assertAlmostEqual(y, 0)

    def test_pos_pos(self):
        radius, theta = cartesianToPolar(1, 2)
        x, y = polarToCartesian(radius, theta)
        self.assertAlmostEqual(x, 1)
        self.assertAlmostEqual(y, 2)

    def test_pos_neg(self):
        radius, theta = cartesianToPolar(1, -2)
        x, y = polarToCartesian(radius, theta)
        self.assertAlmostEqual(x, 1)
        self.assertAlmostEqual(y, -2)

    def test_neg_neg(self):
        radius, theta = cartesianToPolar(-1, -2)
        x, y = polarToCartesian(radius, theta)
        self.assertAlmostEqual(x, -1)
        self.assertAlmostEqual(y, -2)

    def test_neg_pos(self):
        radius, theta = cartesianToPolar(-1, 2)
        x, y = polarToCartesian(radius, theta)
        self.assertAlmostEqual(x, -1)
        self.assertAlmostEqual(y, 2)


class TestSpherical(unittest.TestCase):

    def test_magnitude(self):
        radius, _, _ = cartesianToSpherical(3, 4, 5)
        self.assertAlmostEqual(radius, math.sqrt(3*3 + 4*4 + 5*5))

    def test_0(self):
        radius, _, _ = cartesianToSpherical(0, 0, 0)
        self.assertAlmostEqual(radius, 0)

    def test_pos_pos_pos(self):
        radius, phi, theta = cartesianToSpherical(3, 4, 5)
        print(radius, phi, theta)
        x, y, z = sphericalToCartesian(radius, phi, theta)
        self.assertAlmostEqual(x, 3)
        self.assertAlmostEqual(y, 4)
        self.assertAlmostEqual(z, 5)


if __name__ == '__main__':
    unittest.main()
