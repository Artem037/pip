import math
import unittest

from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rect_area, perimeter as rect_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as tri_area, perimeter as tri_perimeter


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(4), math.pi * 4 * 4, places=10)

    def test_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(4), 2 * math.pi * 4, places=10)

    def test_zero(self):
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_perimeter(0), 0)


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rect_area(3, 7), 21)

    def test_perimeter(self):
        self.assertEqual(rect_perimeter(3, 7), 20)

    def test_zero_side(self):
        self.assertEqual(rect_area(10, 0), 0)
        self.assertEqual(rect_perimeter(10, 0), 20)


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(12), 144)

    def test_perimeter(self):
        self.assertEqual(square_perimeter(12), 48)

    def test_incorrect_perimeter(self):
        self.assertEqual(square_perimeter(239), 52)


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(tri_area(7, 5), 17.5)

    def test_perimeter(self):
        self.assertEqual(tri_perimeter(5, 9, 2), 16)


if __name__ == "__main__":
    unittest.main()
