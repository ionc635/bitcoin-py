from .FieldElement import FieldElement
import unittest

class FieldElementTest(unittest.TestCase):
    def test_add(self):
        p = 57
        a = FieldElement(44, p)
        b = FieldElement(33, p)
        self.assertEqual(a + b, FieldElement(20, p))
        c = FieldElement(17, p)
        d = FieldElement(42, p)
        e = FieldElement(49, p)
        self.assertEqual(c + d + e, FieldElement(51, p))

    def test_sub(self):
        p = 57
        a = FieldElement(9, p)
        b = FieldElement(29, p)
        self.assertEqual(a - b, FieldElement(37, p))
        c = FieldElement(52, p)
        d = FieldElement(30, p)
        e = FieldElement(38, p)
        self.assertEqual(c - d - e, FieldElement(41, p))

    def test_mul(self):
        p = 97
        a = FieldElement(95, p)
        b = FieldElement(45, p)
        c = FieldElement(31, p)
        self.assertEqual(a * b * c, FieldElement(23, p))
        d = FieldElement(17, p)
        e = FieldElement(13, p)
        f = FieldElement(19, p)
        g = FieldElement(44, p)
        self.assertEqual(d * e * f * g, FieldElement(68, p))

    def test_truediv(self):
        p = 31
        a = FieldElement(3, p)
        b = FieldElement(24, p)
        self.assertEqual(a / b, FieldElement(4, p))
        c = FieldElement(4, p)
        d = FieldElement(11, p)
        self.assertEqual(a ** -4 * d, FieldElement(12, p))