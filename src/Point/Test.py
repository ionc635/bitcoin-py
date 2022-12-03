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

    def test_FieldElement_Point_add(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)

        additions = (
            (192, 105, 17, 56, 170, 142),
            (47, 71, 117, 141, 60, 139),
            (143, 98, 76, 66, 47, 71),
        )

        for x1_num, y1_num, x2_num, y2_num, x3_num, y3_num in additions:
            x1 = FieldElement(x1_num, prime)
            y1 = FieldElement(y1_num, prime)
            x2 = FieldElement(x2_num, prime)
            y2 = FieldElement(y2_num, prime)
            x3 = FieldElement(x3_num, prime)
            y3 = FieldElement(y3_num, prime)

            p1 = Point(x1, y1, a, b)
            p2 = Point(x2, y2, a, b)
            p3 = Point(x3, y3, a, b)

            self.assertEqual(p1 + p2, p3)

    def test_FieldElement_Point_mul(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)

        multiplications = ((2, 192, 105, 49, 71), (2, 143, 98, 64, 168), (2, 47, 71, 36, 111), (4, 47, 71, 194, 51), (8, 47, 71, 116, 55), (21, 47, 71, None, None))

        for s, x1_num, y1_num, x2_num, y2_num in multiplications:
            x1 = FieldElement(x1_num, prime)
            y1 = FieldElement(y1_num, prime)

            p1 = Point(x1, y1, a, b)

            if x2_num is None:
                p2 = Point(None, None, a, b)
            else:
                x2 = FieldElement(x2_num, prime)
                y2 = FieldElement(y2_num, prime)
                p2 = Point(x2, y2, a, b)
                
            self.assertEqual(p1 * s, p2)