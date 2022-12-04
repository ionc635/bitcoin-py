from ..FieldElement.FieldElement import FieldElement
from ..Point.Point import Point
from .S256Field import S256Field

A = 0
B = 7
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

class S256Point(Point):
    def __init__(self, x, y, a = None, b = None):
        a, b = S256Field(A), S256Field(B)
        if type(x) == int:
            super().__init__(x = S256Field(x), y = S256Field(y), a = a, b = b)
        else:
            super().__init__(x = x, y = y, a = a, b = b)

    def __mul__(self, coefficient):
        coef = coefficient % N
        return super().__mul__(coef)