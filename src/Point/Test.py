from ..FieldElement.FieldElement import FieldElement
from .Point import Point
import unittest

class PointTest(unittest.TestCase):
    def test_point_add(self):
        a = 5
        b = 7
        p1 = Point(2, 5, a, b)
        p2 = Point(-1, -1, a, b)
        self.assertEqual(p1 + p2, Point(3, -7, a, b))

    def test_point_add1(self):
        a = 5
        b = 7
        p1 = Point(-1, -1, a, b)
        p2 = Point(-1, -1, a, b)
        self.assertEqual(p1 + p2, Point(18, 77, a, b))

    def test_on_curve(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)
        valid_points = ((192, 105), (17, 56), (1, 193))
        invalid_points = ((200, 119), (42, 99))
        for x_raw, y_raw in valid_points:
            x = FieldElement(x_raw, prime)
            y = FieldElement(y_raw, prime)
            Point(x, y, a, b)
        for x_raw, y_raw in invalid_points:
            x = FieldElement(x_raw, prime)
            y = FieldElement(y_raw, prime)
            with self.assertRaises(ValueError):
                Point(x, y, a, b)