print ("EXERCISE 12.1")
import unittest
import math

from Homework12_vector import Vector

class TestVector(unittest.TestCase):

    def test_eq(self):
        v = Vector(-1, 2, -3)
        w = Vector(3, -1, 2)
        self.assertNotEqual(v, w)

    def test_add(self):
        v = Vector(-1, 2, -3)
        w = Vector(3, -1, 2)
        result = v + w
        self.assertEqual(result, Vector(2, 1, -1))

    def test_sub(self):
        v = Vector(-1, 2, -3)
        w = Vector(3, -1, 2)
        result = v - w
        self.assertEqual(result, Vector(-4, 3, -5))

    def test_mul(self):
        v = Vector(-1, 2, -3)
        w = Vector(3, -1, 2)
        result = v * w
        self.assertEqual(result, -11)

    def test_cross(self):
        v = Vector(-1, 2, -3)
        w = Vector(3, -1, 2)
        result = v.cross(w)
        self.assertEqual(result, Vector(1, -7, -5))

    def test_length(self):
        v = Vector(-1, 2, -3)
        result = v.length()
        self.assertEqual(result, math.sqrt(14))

    def test_hash(self):
        v = Vector(-1, 2, -3)
        w = Vector(3, -1, 2)
        S = set([v, v, w])
        self.assertEqual(len(S), 2)

if __name__ == '__main__':
    unittest.main()
