import pytest
from zad8_2 import Point
from zad8_2 import Triangle

class TestTriangle(): 
    def setup_method(self):
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
        self.t14 = Triangle(-1.5, -3.0, 3, -3, 1.5, 1.5)
        self.t15 = Triangle(-1.5, -3.7, 3.2, -3.2, 1.5, 1.5)
        self.t16 = Triangle(-6, -3, 0, -3, -3, -6)

    def test__init__(self): 
        assert self.t1.pt1.x == 1
        assert self.t1.pt1.y == 1

        assert self.t4.pt2.x == 3
        assert self.t7.pt2.y == 0
        assert self.t9.pt3.x == -3
        assert self.t10.pt3.y == 9

        with pytest.raises(ValueError): Triangle(0, 0, 1, 1, 2, 2)
        with pytest.raises(ValueError): Triangle(0, 0, 1, 1, -2, -2)
        with pytest.raises(ValueError): Triangle(0, 0, 100, 100, -200, -200)
        with pytest.raises(ValueError): Triangle(0.5, 0.5, 0.25, 0.25, -2.2, -2.2)


    def test__str__(self):
        assert str(self.t1) == "[(1, 1), (2, 1), (2, 2)]"
        assert str(self.t3) == "[(0, 2), (2, 0), (0, -2)]"
        assert str(self.t4) == "[(0, 0), (3, 0), (0, 6)]"
        assert str(self.t6) == "[(-6, -3), (3, -3), (0, 6)]"
        assert str(self.t8) == "[(3, 3), (9, 3), (3, 9)]"
        assert str(self.t12) == "[(6, -3), (0, -3), (3, 6)]"


    def test__repr__(self):
        assert repr(self.t1) == "Triangle(1, 1, 2, 1, 2, 2)"
        assert repr(self.t3) == "Triangle(0, 2, 2, 0, 0, -2)"
        assert repr(self.t5) == "Triangle(-3, 0, 0, 6, 3, 0)"
        assert repr(self.t7) == "Triangle(0, -6, 6, 0, -3, 3)"
        assert repr(self.t9) == "Triangle(-9, 0, -3, 0, -3, 6)"
        assert repr(self.t10) == "Triangle(0, 3, 6, 3, 0, 9)"
        assert repr(self.t11) == "Triangle(-6, -6, 0, -6, -3, 3)"
        assert repr(self.t13) == "Triangle(0, 0, -6, 0, -6, -3)"


    def test__eq__(self):
        assert (self.t1 == self.t1) is True
        assert (self.t1 == self.t2) is True

        assert (self.t5 == self.t8) is False
        assert (self.t9 == self.t4) is False
        assert (self.t11 == self.t13) is False
        assert (self.t12 == self.t7) is False


    def test__ne__(self): 
        assert (self.t1 != self.t1) is False
        assert (self.t1 != self.t2) is False

        assert (self.t5 != self.t8) is True
        assert (self.t9 != self.t4) is True
        assert (self.t11 != self.t13) is True
        assert (self.t12 != self.t7) is True


    def test_center(self): 
        assert self.t3.center == Point((0+2+0)/3, (2+0-2)/3)
        assert self.t4.center == Point(1, 2)
        assert self.t5.center == Point(0, 2)
        assert self.t6.center == Point(-1, 0)
        assert self.t7.center == Point(1, -1)
        assert self.t8.center == Point(5, 5)
        assert self.t9.center == Point(-5, 2)
        assert self.t10.center == Point(2, 5)
        assert self.t11.center == Point(-3, -3)
        assert self.t12.center == Point(3, 0)
        assert self.t13.center == Point(-4, -1)
        assert self.t14.center == Point(1.0, -1.5)


    def test_area(self): 
        assert self.t1.area() == 0.5
        assert self.t2.area() == 0.5
        assert self.t3.area() == 4
        assert self.t4.area() == 9
        assert self.t5.area() == 18
        assert self.t6.area() == 40.5
        assert self.t7.area() == 36
        assert self.t8.area() == 18
        assert self.t9.area() == 18
        assert self.t10.area() == 18
        assert self.t11.area() == 27
        assert self.t12.area() == 27
        assert self.t13.area() == 9
        assert self.t14.area() == 10.125


    def test_move(self):
        assert self.t1.move(10, 10) == Triangle(11, 11, 12, 11, 12, 12)
        assert self.t2.move(-2, -3) == Triangle(0, -2, -1, -2, 0, -1)
        assert self.t3.move(1.5, 2.5) == Triangle(1.5, 4.5, 3.5, 2.5, 1.5, 0.5)
        assert self.t4.move(-1.2, -2.8) == Triangle(-1.2, -2.8, 1.8, -2.8, -1.2, 3.2)

        assert self.t5.move(5, -5) == Triangle(2, -5, 5, 1, 8, -5)
        assert self.t6.move(-3, 4) == Triangle(-9, 1, 0, 1, -3, 10)
        assert self.t7.move(0, -3) == Triangle(0, -9, 6, -3, -3, 0)

        assert self.t8.move(2.5, 1.5) == Triangle(5.5, 4.5, 11.5, 4.5, 5.5, 10.5)
        assert self.t9.move(-4, -2) == Triangle(-13, -2, -7, -2, -7, 4)
        assert self.t10.move(3, 3) == Triangle(3, 6, 9, 6, 3, 12)

        assert self.t11.move(-1, 2) == Triangle(-7, -4, -1, -4, -4, 5)
        assert self.t12.move(0.5, -1.5) == Triangle(6.5, -4.5, 0.5, -4.5, 3.5, 4.5)
        assert self.t13.move(7, -3) == Triangle(7, -3, 1, -3, 1, -6)

        assert self.t14.move(0.5, 2) == Triangle(-1, -1.0, 3.5, -1, 2, 3.5)

        with pytest.raises(ValueError): self.t11.move("a", "b")
        with pytest.raises(ValueError): self.t5.move([1, 2], [1, 2])
        with pytest.raises(ValueError): self.t5.move((1, 2), (1, 2))
        with pytest.raises(ValueError): self.t5.move(None, None)
        with pytest.raises(ValueError): self.t5.move(True, False)
        with pytest.raises(ValueError): self.t5.move(Point(1, 2), Triangle(1, 2, 3, 4, 1, 0))


    def test_make4(self):
        assert self.t1.make4() == (
            Triangle(1, 1, 1.5, 1, 1.5, 1.5),
            Triangle(1.5, 1, 2, 1, 2, 1.5),
            Triangle(1.5, 1.5, 2, 1.5, 2, 2),
            Triangle(1.5, 1, 2, 1.5, 1.5, 1.5),
        )
        assert self.t3.make4() == (
            Triangle(0, 2, 1.0, 1.0, 0.0, 0.0),
            Triangle(1.0, 1.0, 2, 0, 1.0, -1.0),
            Triangle(0.0, 0.0, 1.0, -1.0, 0, -2),
            Triangle(1.0, 1.0, 1.0, -1.0, 0.0, 0.0),
        )
        assert self.t4.make4() == (
            Triangle(0, 0, 1.5, 0.0, 0.0, 3.0),
            Triangle(1.5, 0.0, 3, 0, 1.5, 3.0),
            Triangle(0.0, 3.0, 1.5, 3.0, 0, 6),
            Triangle(1.5, 0.0, 1.5, 3.0, 0.0, 3.0),
        )
        assert self.t5.make4() == (
            Triangle(-3, 0, -1.5, 3.0, 0.0, 0.0),
            Triangle(-1.5, 3.0, 0, 6, 1.5, 3.0),
            Triangle(0.0, 0.0, 1.5, 3.0, 3, 0),
            Triangle(-1.5, 3.0, 1.5, 3.0, 0.0, 0.0),
        )
        assert self.t6.make4() == (
            Triangle(-6, -3, -1.5, -3.0, -3.0, 1.5),
            self.t14,
            Triangle(-3.0, 1.5, 1.5, 1.5, 0, 6),
            Triangle(-1.5, -3.0, 1.5, 1.5, -3.0, 1.5),
        )
        assert self.t14.make4() == (
            Triangle(-1.5, -3.0, 0.75, -3.0, 0.0, -0.75),
            Triangle(0.75, -3.0, 3, -3, 2.25, -0.75),
            Triangle(0.0, -0.75, 2.25, -0.75, 1.5, 1.5),
            Triangle(0.75, -3.0, 2.25, -0.75, 0.0, -0.75),
        )

    def test_left(self):
        assert self.t1.left == 1
        assert self.t3.left == 0
        assert self.t5.left == -3
        assert self.t9.left == -9
        assert self.t14.left == -1.5

    def test_right(self):
        assert self.t1.right == 2
        assert self.t8.right == 9
        assert self.t9.right == -3
        assert self.t10.right == 6
        assert self.t11.right == 0
        assert self.t15.right == 3.2

    def test_top(self):
        assert self.t1.top == 1
        assert self.t3.top == -2
        assert self.t5.top == 0
        assert self.t7.top == -6
        assert self.t15.top == -3.7

    def test_bottom(self):
        assert self.t1.bottom == 2
        assert self.t4.bottom == 6
        assert self.t10.bottom == 9
        assert self.t13.bottom == 0
        assert self.t15.bottom == 1.5
        assert self.t16.bottom == -3

    def test_width(self):
        assert self.t1.width == 1
        assert self.t5.width == 6
        assert self.t6.width == 9
        assert self.t10.width == 6
        assert self.t14.width == 4.5

    def test_height(self):
        assert self.t1.height == 1
        assert self.t3.height == 4
        assert self.t4.height == 6
        assert self.t7.height == 9
        assert self.t13.height == 3
        assert self.t14.height == 4.5

    def test_topleft(self):
        assert self.t1.topleft == Point(1, 1)
        assert self.t3.topleft == Point(0, -2)
        assert self.t4.topleft == Point(0, 0)
        assert self.t6.topleft == Point(-6, -3)
        assert self.t8.topleft == Point(3, 3)
        assert self.t14.topleft == Point(-1.5, -3)

    def test_topright(self):
        assert self.t1.topright == Point(2, 1)
        assert self.t3.topright == Point(2, -2)
        assert self.t4.topright == Point(3, 0)
        assert self.t8.topright == Point(9, 3)
        assert self.t15.topright == Point(3.2, -3.7)

    def test_bottomleft(self):
        assert self.t1.bottomleft == Point(1, 2)
        assert self.t3.bottomleft == Point(0, 2)
        assert self.t6.bottomleft == Point(-6, 6)
        assert self.t14.bottomleft == Point(-1.5, 1.5)

    def test_bottomright(self):
        assert self.t1.bottomright == Point(2, 2)
        assert self.t4.bottomright == Point(3, 6)
        assert self.t14.bottomright == Point(3, 1.5)
        assert self.t16.bottomright == Point(0, -3)

    def test_bounding_box(self):
        assert self.t1.bounding_box  == (2, 2, 1, 1)
        assert self.t4.bounding_box  == (3, 6, 0, 0)
        assert self.t6.bounding_box  == (3, 6, -6, -3)
        assert self.t14.bounding_box == (3, 1.5, -1.5, -3)