import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):          # zwraca string "(x, y)"
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):         # zwraca string "Point(x, y)"
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):    # obsługa point1 == point2
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):   # v1 - v2
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny, zwraca liczbę
        return (self.x * other.x) + (self.y * other.y)

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):           # długość wektora
        return math.sqrt((self.x)**2 + (self.y)**2 )
    
    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase): 

    def setUp(self):
        self.p1 = Point(0, 0)
        self.p2 = Point(3, 4)
        self.p3 = Point(-1, -1)
        self.p4 = Point(-5, 5)
        self.p5 = Point(1.5, -2.7)
        self.p6 = Point(1000000, -999999)
        self.p7 = Point(1, 1)
        self.p8 = Point(0, 4)
        self.p9 = Point(4, 0)
        self.p10 = Point(100000, -999991)
        self.p11 = Point(1.507, -2.7)
        self.p12 = Point(5, -5)
        self.p13 = Point(1,2)
        self.p14 = Point(2,4)



    def test__init__(self): 
        self.assertEqual(self.p1.x, 0)
        self.assertEqual(self.p1.y, 0)

        self.assertEqual(self.p2.x, 3)
        self.assertEqual(self.p2.y, 4)

        self.assertEqual(self.p3.x, -1)
        self.assertEqual(self.p3.y, -1)

        self.assertEqual(self.p5.x, 1.5)
        self.assertEqual(self.p5.y, -2.7)

        self.assertEqual(self.p6.y, -999999)
        self.assertEqual(self.p6.x, 1000000)

 
    def test__str__(self):
        self.assertEqual(str(self.p1), "(0, 0)") 
        self.assertEqual(str(self.p2), "(3, 4)")
        self.assertEqual(str(self.p3), "(-1, -1)")
        self.assertEqual(str(self.p4), "(-5, 5)")
        self.assertEqual(str(self.p5), "(1.5, -2.7)")
        self.assertEqual(str(self.p6), "(1000000, -999999)")


    def test__repr__(self):
        self.assertEqual(repr(self.p1), "Point(0, 0)") 
        self.assertEqual(repr(self.p2), "Point(3, 4)")
        self.assertEqual(repr(self.p3), "Point(-1, -1)")
        self.assertEqual(repr(self.p4), "Point(-5, 5)")
        self.assertEqual(repr(self.p5), "Point(1.5, -2.7)")
        self.assertEqual(repr(self.p6), "Point(1000000, -999999)")


    def test__eq__(self):
        self.assertEqual(self.p1 == self.p1, True)
        self.assertEqual(self.p1 == self.p2, False)
        self.assertEqual(self.p1 == self.p8, False)
        self.assertEqual(self.p1 == self.p9, False)
        self.assertEqual(self.p3 == self.p3, True)
        self.assertEqual(self.p3 == self.p7, False)
        self.assertEqual(self.p5 == self.p4, False)
        self.assertEqual(self.p6 == self.p10, False)
        self.assertEqual(self.p8 == self.p9, False)
        self.assertEqual(self.p5 == self.p11, False)



    def test__ne__(self): 
        self.assertEqual(self.p1 != self.p1, False)
        self.assertEqual(self.p1 != self.p2, True)
        self.assertEqual(self.p1 != self.p8, True)
        self.assertEqual(self.p1 != self.p9, True)
        self.assertEqual(self.p3 != self.p3, False)
        self.assertEqual(self.p3 != self.p7, True)
        self.assertEqual(self.p5 != self.p4, True)
        self.assertEqual(self.p6 != self.p10, True)
        self.assertEqual(self.p8 != self.p9, True)
        self.assertEqual(self.p5 != self.p11, True)


    def test__add__(self): 
        self.assertEqual(self.p1 + self.p1, self.p1)
        self.assertEqual(self.p2 + self.p2, Point(6, 8))
        self.assertEqual(self.p1 + self.p4, Point(-5, 5))
        self.assertEqual(self.p1 + self.p3, self.p3)
        self.assertEqual(self.p3 + self.p4, Point(-6, 4))
        self.assertEqual(self.p6 + self.p10, Point(1100000, -1999990))
        self.assertEqual(self.p8 + self.p9, Point(4, 4))
        self.assertEqual(self.p7 + self.p3, self.p1)
        self.assertEqual(self.p4 + self.p12, self.p1)

         
    def test__sub__(self): 
        self.assertEqual(self.p1 - self.p1, self.p1)
        self.assertEqual(self.p2 - self.p2, self.p1)
        self.assertEqual(self.p1 - self.p4, Point(5, -5))
        self.assertEqual(self.p1 - self.p3, Point(1, 1))
        self.assertEqual(self.p3 - self.p4, Point(4, -6))
        self.assertEqual(self.p6 - self.p10, Point(900000, -8))
        self.assertEqual(self.p8 - self.p9, Point(-4, 4))
        self.assertEqual(self.p7 - self.p3, Point(2, 2))
        self.assertEqual(self.p4 - self.p12, Point(-10, 10))


    def test__mul__y(self):
        self.assertEqual(self.p1 * self.p1, 0)
        self.assertEqual(self.p2 * self.p2, 25)
        self.assertEqual(self.p1 * self.p4, 0)
        self.assertEqual(self.p1 * self.p3, 0)
        self.assertEqual(self.p3 * self.p4, 0)
        self.assertEqual(self.p6 * self.p10, 1099990000009)
        self.assertEqual(self.p8 * self.p9, 0)
        self.assertEqual(self.p7 * self.p3, -2)
        self.assertEqual(self.p4 * self.p12, -50)


    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p1), 0)
        self.assertEqual(self.p2.cross(self.p2), 0)

        self.assertEqual(self.p2.cross(self.p3), 1)
        self.assertEqual(self.p3.cross(self.p4), -10)

        self.assertEqual(self.p1.cross(self.p4), 0)
        self.assertEqual(self.p8.cross(self.p9), -16)

        self.assertEqual(self.p6.cross(self.p10), -899991100000)

        self.assertEqual(self.p13.cross(self.p14), 0)

        self.assertEqual(Point(1,0).cross(Point(0,1)), 1)
        self.assertEqual(Point(0,1).cross(Point(1,0)), -1)


    def test_length(self): 
        self.assertEqual(self.p1.length(), 0)
        self.assertEqual(self.p2.length(), 5)
        self.assertAlmostEqual(self.p3.length(), math.sqrt(2))
        self.assertAlmostEqual(self.p5.length(), math.sqrt(1.5**2 + (-2.7)**2))
        self.assertAlmostEqual(self.p6.length(), math.sqrt(1000000**2 + (-999999)**2))
        self.assertEqual(self.p8.length(), 4)
        self.assertEqual(self.p9.length(), 4)     
        self.assertEqual(self.p4.length(), math.sqrt((-5)**2 + 5**2))  

    
    def test__hash__(self): 
        self.assertEqual(hash(self.p1), hash((0, 0)))
        self.assertEqual(hash(self.p2), hash((3, 4)))
        self.assertEqual(hash(self.p3), hash((-1, -1)))
        self.assertEqual(hash(self.p4), hash((-5, 5)))
        self.assertEqual(hash(self.p5), hash((1.5, -2.7)))
        self.assertEqual(hash(self.p6), hash((1000000, -999999)))


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()  
