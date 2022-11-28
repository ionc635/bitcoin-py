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
