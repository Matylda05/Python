from zad8_2 import Point
from zad8_2 import Triangle

import pytest


t1 = Triangle(1, 1, 2, 1, 2, 2)
t2 = Triangle(2, 1, 1, 1, 2, 2) #zamieniona kolejnośc t1

t3 = Triangle(0, 2, 2, 0, 0, -2)
t4 = Triangle(0, 0, 3, 0, 0, 6)

t5 = Triangle(-3, 0, 0, 6, 3, 0)
t6 = Triangle(-6, -3, 3, -3, 0, 6)

t7 = Triangle(0, -6, 6, 0, -3, 3)
t8 = Triangle(3, 3, 9, 3, 3, 9)

t9 = Triangle(-9, 0, -3, 0, -3, 6)
t10 = Triangle(0, 3, 6, 3, 0, 9)

t11 = Triangle(-6, -6, 0, -6, -3, 3)
t12 = Triangle(6, -3, 0, -3, 3, 6)

t13 = Triangle(0, 0, -6, 0, -6, -3)
t14 = Triangle(-1.5, -3.0, 3, -3, 1.5, 1.5)

def test__init__(): 
    assert t1.pt1.x == 1
    assert t1.pt1.y == 1

    assert t4.pt2.x == 3
    assert t7.pt2.y == 0
    assert t9.pt3.x == -3
    assert t10.pt3.y == 9

    with pytest.raises(ValueError): Triangle(0, 0, 1, 1, 2, 2)
    with pytest.raises(ValueError): Triangle(0, 0, 1, 1, -2, -2)
    with pytest.raises(ValueError): Triangle(0, 0, 100, 100, -200, -200)
    with pytest.raises(ValueError): Triangle(0.5, 0.5, 0.25, 0.25, -2.2, -2.2)

def test__str__():
    assert str(t1) == "[(1, 1), (2, 1), (2, 2)]"
    assert str(t3) == "[(0, 2), (2, 0), (0, -2)]"
    assert str(t4) == "[(0, 0), (3, 0), (0, 6)]"
    assert str(t6) == "[(-6, -3), (3, -3), (0, 6)]"
    assert str(t8) == "[(3, 3), (9, 3), (3, 9)]"
    assert str(t12) == "[(6, -3), (0, -3), (3, 6)]"


def test__repr__():
    assert repr(t1) == "Triangle(1, 1, 2, 1, 2, 2)"
    assert repr(t3) == "Triangle(0, 2, 2, 0, 0, -2)"
    assert repr(t5) == "Triangle(-3, 0, 0, 6, 3, 0)"
    assert repr(t7) == "Triangle(0, -6, 6, 0, -3, 3)"
    assert repr(t9) == "Triangle(-9, 0, -3, 0, -3, 6)"
    assert repr(t10) == "Triangle(0, 3, 6, 3, 0, 9)"
    assert repr(t11) == "Triangle(-6, -6, 0, -6, -3, 3)"
    assert repr(t13) == "Triangle(0, 0, -6, 0, -6, -3)"


def test__eq__():
    assert (t1 == t1) is True
    assert (t1 == t2) is True

    assert (t5 == t8) is False
    assert (t9 == t4) is False
    assert (t11 == t13) is False
    assert (t12 == t7) is False


def test__ne__(): 
    assert (t1 != t1) is False
    assert (t1 != t2) is False

    assert (t5 != t8) is True
    assert (t9 != t4) is True
    assert (t11 != t13) is True
    assert (t12 != t7) is True



def test_center(): 
    assert t3.center() == Point((0+2+0)/3, (2+0-2)/3)
    assert t4.center() == Point(1, 2)
    assert t5.center() == Point(0, 2)
    assert t6.center() == Point(-1, 0)
    assert t7.center() == Point(1, -1)
    assert t8.center() == Point(5, 5)
    assert t9.center() == Point(-5, 2)
    assert t10.center() == Point(2, 5)
    assert t11.center() == Point(-3, -3)
    assert t12.center() == Point(3, 0)
    assert t13.center() == Point(-4, -1)
    assert t14.center() == Point(1.0, -1.5)


def test_area(): 
    assert t1.area() == 0.5
    assert t2.area() == 0.5
    assert t3.area() == 4
    assert t4.area() == 9
    assert t5.area() == 18
    assert t6.area() == 40.5
    assert t7.area() == 36
    assert t8.area() == 18
    assert t9.area() == 18
    assert t10.area() == 18
    assert t11.area() == 27
    assert t12.area() == 27
    assert t13.area() == 9
    assert t14.area() == 10.125


def test_move():
    assert t1.move(10, 10) == Triangle(11, 11, 12, 11, 12, 12)
    assert t2.move(-2, -3) == Triangle(0, -2, -1, -2, 0, -1)
    assert t3.move(1.5, 2.5) == Triangle(1.5, 4.5, 3.5, 2.5, 1.5, 0.5)
    assert t4.move(-1.2, -2.8) == Triangle(-1.2, -2.8, 1.8, -2.8, -1.2, 3.2)

    assert t5.move(5, -5) == Triangle(2, -5, 5, 1, 8, -5)
    assert t6.move(-3, 4) == Triangle(-9, 1, 0, 1, -3, 10)
    assert t7.move(0, -3) == Triangle(0, -9, 6, -3, -3, 0)

    assert t8.move(2.5, 1.5) == Triangle(5.5, 4.5, 11.5, 4.5, 5.5, 10.5)
    assert t9.move(-4, -2) == Triangle(-13, -2, -7, -2, -7, 4)
    assert t10.move(3, 3) == Triangle(3, 6, 9, 6, 3, 12)

    assert t11.move(-1, 2) == Triangle(-7, -4, -1, -4, -4, 5)
    assert t12.move(0.5, -1.5) == Triangle(6.5, -4.5, 0.5, -4.5, 3.5, 4.5)
    assert t13.move(7, -3) == Triangle(7, -3, 1, -3, 1, -6)

    assert t14.move(0.5, 2) == Triangle(-1, -1.0, 3.5, -1, 2, 3.5)

    with pytest.raises(ValueError): t11.move("a", "b")
    with pytest.raises(ValueError): t5.move([1, 2], [1, 2])
    with pytest.raises(ValueError): t5.move((1, 2), (1, 2))
    with pytest.raises(ValueError): t5.move(None, None)
    with pytest.raises(ValueError): t5.move(True, False)
    with pytest.raises(ValueError): t5.move(Point(1, 2), Triangle(1, 2, 3, 4, 1, 0))

def test_make4():
    assert t1.make4() == (
        Triangle(1, 1, 1.5, 1, 1.5, 1.5),
        Triangle(1.5, 1, 2, 1, 2, 1.5),
        Triangle(1.5, 1.5, 2, 1.5, 2, 2),
        Triangle(1.5, 1, 2, 1.5, 1.5, 1.5),
    )
    assert t3.make4() == (
        Triangle(0, 2, 1.0, 1.0, 0.0, 0.0),
        Triangle(1.0, 1.0, 2, 0, 1.0, -1.0),
        Triangle(0.0, 0.0, 1.0, -1.0, 0, -2),
        Triangle(1.0, 1.0, 1.0, -1.0, 0.0, 0.0),
    )
    assert t4.make4() == (
        Triangle(0, 0, 1.5, 0.0, 0.0, 3.0),
        Triangle(1.5, 0.0, 3, 0, 1.5, 3.0),
        Triangle(0.0, 3.0, 1.5, 3.0, 0, 6),
        Triangle(1.5, 0.0, 1.5, 3.0, 0.0, 3.0),
    )
    assert t5.make4() == (
        Triangle(-3, 0, -1.5, 3.0, 0.0, 0.0),
        Triangle(-1.5, 3.0, 0, 6, 1.5, 3.0),
        Triangle(0.0, 0.0, 1.5, 3.0, 3, 0),
        Triangle(-1.5, 3.0, 1.5, 3.0, 0.0, 0.0),
    )
    assert t6.make4() == (
        Triangle(-6, -3, -1.5, -3.0, -3.0, 1.5),
        t14,
        Triangle(-3.0, 1.5, 1.5, 1.5, 0, 6),
        Triangle(-1.5, -3.0, 1.5, 1.5, -3.0, 1.5),
    )
    assert t14.make4() == (
        Triangle(-1.5, -3.0, 0.75, -3.0, 0.0, -0.75),
        Triangle(0.75, -3.0, 3, -3, 2.25, -0.75),
        Triangle(0.0, -0.75, 2.25, -0.75, 1.5, 1.5),
        Triangle(0.75, -3.0, 2.25, -0.75, 0.0, -0.75),
    )


pytest