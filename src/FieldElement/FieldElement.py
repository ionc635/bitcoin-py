import unittest

class FieldElement:
    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime
    
    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime
    
    def __ne__(self, other):
        if other is None:
            return False
        return self.num != other.num or self.prime != other.prime
    
    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot sub two numbers in different Fields')
        num = (self.num - other.num) % self.prime
        
        if (num < 0):
            num = self.prime - num

        return self.__class__(num, self.prime)
    
    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot mul two numbers in different Fields')
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)
    
    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot truediv two numbers in different Fields')
        num = self.num * (other.num ** (self.prime - 2)) % self.prime
        return self.__class__(num, self.prime)


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