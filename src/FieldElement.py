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

class FieldElementTest(unittest.TestCase):
    def test_add1(self):
        a = FieldElement(44, 57)
        b = FieldElement(33, 57)
        self.assertEqual(a + b, FieldElement(20, 57))
        c = FieldElement(17, 57)
        d = FieldElement(42, 57)
        e = FieldElement(49, 57)
        self.assertEqual(c + d + e, FieldElement(51, 57))

    def test_sub(self):
        a = FieldElement(9, 57)
        b = FieldElement(29, 57)
        self.assertEqual(a - b, FieldElement(37, 57))
        c = FieldElement(52, 57)
        d = FieldElement(30, 57)
        e = FieldElement(38, 57)
        self.assertEqual(c - d - e, FieldElement(41, 57))
