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


class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        area = abs(
            x1*(y2 - y3) +
            x2*(y3 - y1) +
            x3*(y1 - y2)
        ) / 2
        if area == 0:
            raise ValueError("Punkty są współliniowe-nie da się utwożyć trójkąta")
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
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise ValueError("Podane Przesunięcie nie jest liczbą")
        if isinstance(x, bool) or isinstance(y, bool):
            raise ValueError("Podane Przesunięcie nie jest liczbą (BOOL)")
        x1 = self.pt1.x + x
        x2 = self.pt2.x + x
        x3 = self.pt3.x + x
        y1 = self.pt1.y + y
        y2 = self.pt2.y + y
        y3 = self.pt3.y + y
        return Triangle(x1, y1, x2, y2, x3, y3)
    
    def make4(self):            # zwraca krotkę czterech mniejszych
        #     A       po podziale    A
        #    / \                    / \
        #   /   \                  F---D
        #  /     \                / \ / \
        # C-------B              C---E---B
        A = self.pt1  
        B = self.pt2  
        C = self.pt3
        D = Point((A.x+B.x)/2, (A.y+B.y)/2)    #AB
        E = Point((B.x+C.x)/2, (B.y+C.y)/2)    #BC
        F = Point((C.x+A.x)/2, (C.y+A.y)/2)    #CA
        return (
            Triangle(A.x, A.y, D.x, D.y, F.x, F.y),
            Triangle(D.x, D.y, B.x, B.y, E.x, E.y),
            Triangle(F.x, F.y, E.x, E.y, C.x, C.y),
            Triangle(D.x, D.y, E.x, E.y, F.x, F.y)
        )
    
@classmethod
def from_points(cls, points):
    if not isinstance(points, (list, tuple)) or len(points) != 3:
        raise ValueError("Element musi być listą lub krotką zawierającą trzy punkty")

    p1, p2, p3 = points

    if not all(isinstance(p, Point) for p in (p1, p2, p3)):
        raise ValueError("Elementy muszą być obiektami Point")

    return cls(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)

        



