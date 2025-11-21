from zad6_2 import Point

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[" + str(self.pt1) + ", "+ str(self.pt2) + ", " + str(self.pt3) + "]"

    def __repr__(self):         # "Triangle(x1, y1, x2, y2, x3, y3)"
        p1= "(" + str(self.pt1.x) + ", " + str(self.pt1.y)
        p2= str(self.pt2.x) + ", " + str(self.pt2.y)
        p3= str(self.pt3.x) + ", " + str(self.pt3.y) + ")"
        return "Triangle" + p1 + ", "+ p2 + ", " + p3

    def __eq__(self, other):   # obsługa tr1 == tr2
         return {self.pt1, self.pt2, self.pt3} == {other.pt1, other.pt2, other.pt3}

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):          # zwraca środek (masy) trójkąta
        x = (self.pt1.x + self.pt2.x + self.pt3.x)/3
        y = (self.pt1.y + self.pt2.y + self.pt3.y)/3
        return Point(x,y)

    def area(self):           # pole powierzchni
        res = (
            self.pt1.x * (self.pt2.y - self.pt3.y) + 
            self.pt2.x * (self.pt3.y - self.pt1.y) + 
            self.pt3.x * (self.pt1.y - self.pt2.y)
        )
        return (abs(res))/2

    def move(self, x, y):      # przesunięcie o (x, y)
        x1 = self.pt1.x + x
        x2 = self.pt2.x + x
        x3 = self.pt3.x + x
        y1 = self.pt1.y + y
        y2 = self.pt2.y + y
        y3 = self.pt3.y + y
        return Triangle(x1, y1, x2, y2, x3, y3)


# Kod testujący moduł.

import unittest

class TestTriangle(unittest.TestCase): pass

class TestPoint(unittest.TestCase): 

    def setUp(self):
        self.t1 = Triangle(1, 1, 2, 1, 2, 2)
        self.t2 = Triangle(2, 1, 1, 1, 2, 2) #zamieniona kolejnośc t1

        self.t3 = Triangle(0, 2, 2, 0, 0, -2)
        self.t4 = Triangle(0, 0, 3, 0, 0, 6)

        self.t5 = Triangle(-3, 0, 0, 6, 3, 0)
        self.t6 = Triangle(-6, -3, 3, -3, 0, 6)

        self.t7 = Triangle(0, -6, 6, 0, -3, 3)
        self.t8 = Triangle(3, 3, 9, 3, 3, 9)

        self.t9 = Triangle(-9, 0, -3, 0, -3, 6)
        self.t10 = Triangle(0, 3, 6, 3, 0, 9)

        self.t11 = Triangle(-6, -6, 0, -6, -3, 3)
        self.t12 = Triangle(6, -3, 0, -3, 3, 6)

        self.t13 = Triangle(0, 0, -6, 0, -6, -3)




    def test__init__(self): 
        self.assertEqual(self.t1.pt1.x, 1)
        self.assertEqual(self.t1.pt1.y, 1)

        self.assertEqual(self.t4.pt2.x, 3)
        self.assertEqual(self.t7.pt2.y, 0)
        self.assertEqual(self.t9.pt3.x, -3)
        self.assertEqual(self.t10.pt3.y, 9)


 
    def test__str__(self):
        self.assertEqual(str(self.t1), "[(1, 1), (2, 1), (2, 2)]") 
        self.assertEqual(str(self.t3), "[(0, 2), (2, 0), (0, -2)]") 

        self.assertEqual(str(self.t4), "[(0, 0), (3, 0), (0, 6)]") 
        self.assertEqual(str(self.t6), "[(-6, -3), (3, -3), (0, 6)]") 

        self.assertEqual(str(self.t8), "[(3, 3), (9, 3), (3, 9)]") 
        self.assertEqual(str(self.t12), "[(6, -3), (0, -3), (3, 6)]") 


    def test__repr__(self):
        self.assertEqual(repr(self.t1), "Triangle(1, 1, 2, 1, 2, 2)") 
        self.assertEqual(repr(self.t3), "Triangle(0, 2, 2, 0, 0, -2)")

        self.assertEqual(repr(self.t5), "Triangle(-3, 0, 0, 6, 3, 0)") 
        self.assertEqual(repr(self.t7), "Triangle(0, -6, 6, 0, -3, 3)")

        self.assertEqual(repr(self.t9), "Triangle(-9, 0, -3, 0, -3, 6)") 
        self.assertEqual(repr(self.t10), "Triangle(0, 3, 6, 3, 0, 9)")

        self.assertEqual(repr(self.t11), "Triangle(-6, -6, 0, -6, -3, 3)") 
        self.assertEqual(repr(self.t13), "Triangle(0, 0, -6, 0, -6, -3)")


    def test__eq__(self):
        self.assertEqual(self.t1 == self.t1, True)
        self.assertEqual(self.t1 == self.t2, True) 

        self.assertEqual(self.t5 == self.t8, False)
        self.assertEqual(self.t9 == self.t4, False) 

        self.assertEqual(self.t11 == self.t13, False)
        self.assertEqual(self.t12 == self.t7, False) 


    def test__ne__(self): 
        self.assertEqual(self.t1 != self.t1, False)
        self.assertEqual(self.t1 != self.t2, False) 

        self.assertEqual(self.t5 != self.t8, True)
        self.assertEqual(self.t9 != self.t4, True) 

        self.assertEqual(self.t11 != self.t13, True)
        self.assertEqual(self.t12 != self.t7, True) 


    def test_center(self): 
        self.assertEqual((self.t3.center()), Point((0+2+0)/3, (2+0-2)/3))
        self.assertEqual((self.t4.center()), Point(1, 2))

        self.assertEqual((self.t5.center()), Point(0, 2))
        self.assertEqual((self.t6.center()), Point(-1, 0))

        self.assertEqual((self.t7.center()), Point(1, -1))
        self.assertEqual((self.t8.center()), Point(5, 5))

        self.assertEqual((self.t9.center()), Point(-5, 2))
        self.assertEqual((self.t10.center()), Point(2, 5))
        
        self.assertEqual((self.t11.center()), Point(-3, -3))
        self.assertEqual((self.t12.center()), Point(3,0))
        self.assertEqual((self.t13.center()), Point(-4, -1))

 
    def test_area(self): 
        self.assertEqual(self.t1.area(), 0.5)
        self.assertEqual(self.t2.area(), 0.5)
        self.assertEqual(self.t3.area(), 4)
        self.assertEqual(self.t4.area(), 9)
        self.assertEqual(self.t5.area(), 18)
        self.assertEqual(self.t6.area(), 40.5)
        self.assertEqual(self.t7.area(), 36)
        self.assertEqual(self.t8.area(), 18)
        self.assertEqual(self.t9.area(), 18)
        self.assertEqual(self.t10.area(), 18)
        self.assertEqual(self.t11.area(), 27)
        self.assertEqual(self.t12.area(), 27)
        self.assertEqual(self.t13.area(), 9)


    def test_move(self):
        self.assertEqual(self.t1.move(10, 10), Triangle(11, 11, 12, 11, 12, 12))

        self.assertEqual(self.t2.move(-2, -3), Triangle(0, -2, -1, -2, 0, -1))

        self.assertEqual(self.t3.move(1.5, 2.5),Triangle(1.5, 4.5, 3.5, 2.5, 1.5, 0.5))
        
        self.assertEqual(self.t4.move(-1.2, -2.8),Triangle(-1.2, -2.8, 1.8, -2.8, -1.2, 3.2))

        self.assertEqual(self.t5.move(5, -5),Triangle(2, -5, 5, 1, 8, -5))
        self.assertEqual(self.t6.move(-3, 4),Triangle(-9, 1, 0, 1, -3, 10))
        self.assertEqual(self.t7.move(0, -3),Triangle(0, -9, 6, -3, -3, 0))

        self.assertEqual(self.t8.move(2.5, 1.5),Triangle(5.5, 4.5, 11.5, 4.5, 5.5, 10.5))
        self.assertEqual(self.t9.move(-4, -2), Triangle(-13, -2, -7, -2, -7, 4))
        self.assertEqual(self.t10.move(3, 3),Triangle(3, 6, 9, 6, 3, 12))
        
        self.assertEqual(self.t11.move(-1, 2),Triangle(-7, -4, -1, -4, -4, 5))
        self.assertEqual(self.t12.move(0.5, -1.5),Triangle(6.5, -4.5, 0.5, -4.5, 3.5, 4.5))
        self.assertEqual(self.t13.move(7, -3),Triangle(7, -3, 1, -3, 1, -6))


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()  
