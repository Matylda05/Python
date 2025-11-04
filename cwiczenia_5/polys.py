def add_poly(poly1, poly2):         # poly1(x) + poly2(x)
    result = []
    if len(poly1) == len(poly2):
        
        for i in range(len(poly2)):
            result.append(poly1[i] + poly2[i])

    elif len(poly1) > len(poly2):

        for i in range(len(poly2)):
            result.append(poly1[i]+poly2[i])

        for i in range(len(poly2), len(poly1)):
            result.append(poly1[i])

    elif len(poly1) < len(poly2):

        for i in range(len(poly1)):
            result.append(poly1[i]+poly2[i])

        for i in range(len(poly1), len(poly2)):
            result.append(poly2[i])

    return result



def sub_poly(poly1, poly2):       # poly1(x) - poly2(x)
    result = []
    if len(poly1) == len(poly2):
        
        for i in range(len(poly2)):
            result.append(poly1[i] - poly2[i])

    elif len(poly1) > len(poly2):

        for i in range(len(poly2)):
            result.append(poly1[i]-poly2[i])

        for i in range(len(poly2), len(poly1)):
            result.append(poly1[i])

    elif len(poly1) < len(poly2):

        for i in range(len(poly1)):
            result.append(poly1[i]-poly2[i])

        for i in range(len(poly1), len(poly2)):
            result.append(poly2[i]*(-1))

    return result   



def mul_poly(poly1, poly2): pass        # poly1(x) * poly2(x)

def is_zero(poly):                 # bool, [0], [0,0], itp.

    for i in range(len(poly)):
        if(poly[i] != 0):
            return False
    return True

def eq_poly(poly1, poly2):        # bool, porównywanie poly1(x) == poly2(x)
    poly1 = usun_zero_z_konca(poly1)
    poly2 = usun_zero_z_konca(poly2)

    if len(poly1) == len(poly2):
        for i in range(len(poly2)):
            if(poly1[i] != poly2[i]):
                return False

    elif len(poly1) != len(poly2):
        return False

    return True
    

def eval_poly(poly, x0):            # poly(x0), algorytm Hornera
    poly = usun_zero_z_konca(poly)
    if poly == [0]:
        return 0
    result = poly[-1]
    for i in range(len(poly)-2, -1, -1):
        result = ((x0*result)+ (poly[i]))
    return result


def combine_poly(poly1, poly2): pass    # poly1(poly2(x)), trudne!

def pow_poly(poly, n): pass             # poly(x) ** n

def diff_poly(poly): pass               # pochodna wielomianu

def usun_zero_z_konca(poly):
    for i in range(len(poly)-1, 0, -1):
        if(poly[i] == 0):
            poly.pop(i) 
        else:
            break 
    return poly   

# p1 = [2, 1]                   # W(x) = 2 + x
# p2 = [2, 1, 0]                # jw  (niejednoznaczność)
# p3 = [-3, 0, 1]               # W(x) = -3 + x^2
# p4 = [3]                      # W(x) = 3, wielomian zerowego stopnia
# p5 = [0]                      # zero
# p6 = [0, 0, 0]                # zero (niejednoznaczność)

import unittest

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x^2
        self.p3 = [5, 6, 7]   # W(x) = 5 + 6x + 7x^2
        self.p4 = [1, 2, 3]   # W(x) = 1 + 2x + 3x^2
        self.p5 = [0] 
        self.p6 = [0, -1] 
        self.p7 = [-1, -2, -3]
        self.p8 = [1]
        self.p9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.p10 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.p11 = [0, 1, 0]



    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])
        self.assertEqual(add_poly(self.p3, self.p4), [6, 8, 10])
        self.assertEqual(add_poly(self.p5, self.p1), [0, 1])
        self.assertEqual(add_poly(self.p1, self.p6), [0, 0])
        self.assertEqual(add_poly(self.p7, self.p3), [4, 4, 4])
        self.assertEqual(add_poly(self.p4, self.p8), [2,2,3])
        self.assertEqual(add_poly(self.p8, self.p3), [6,6,7])
        self.assertEqual(add_poly(self.p1, self.p10), [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_sub_poly(self): 
        self.assertEqual(sub_poly(self.p1, self.p2), [0, 1, -1])
        self.assertEqual(sub_poly(self.p3, self.p4), [4, 4, 4])
        self.assertEqual(sub_poly(self.p5, self.p1), [0, -1])
        self.assertEqual(sub_poly(self.p1, self.p6), [0, 2])
        self.assertEqual(sub_poly(self.p7, self.p3), [-6, -8, -10])
        self.assertEqual(sub_poly(self.p4, self.p8), [0, 2, 3])
        self.assertEqual(sub_poly(self.p8, self.p3), [-4, -6, -7])
        self.assertEqual(sub_poly(self.p6, self.p6), [0, 0])
        self.assertEqual(sub_poly(self.p1, self.p10), [0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_mul_poly(self): pass

    def test_is_zero(self): 
        self.assertEqual(is_zero(self.p1), False)
        self.assertEqual(is_zero(self.p2), False)
        self.assertEqual(is_zero(self.p3), False)
        self.assertEqual(is_zero(self.p5), True)
        self.assertEqual(is_zero(self.p9), True)
        self.assertEqual(is_zero(self.p10), False)

    def test_eq_poly(self): 
        self.assertEqual(eq_poly(self.p1, self.p2), False)
        self.assertEqual(eq_poly(self.p3, self.p4), False)
        self.assertEqual(eq_poly(self.p1, self.p1), True)
        self.assertEqual(eq_poly(self.p5, self.p9), True)
        self.assertEqual(eq_poly(self.p5, self.p8), False)
        self.assertEqual(eq_poly(self.p4, self.p7), False)
        self.assertEqual(eq_poly(self.p10, self.p10), True)
        self.assertEqual(eq_poly(self.p9, self.p10), False)
        self.assertEqual(eq_poly(self.p1, self.p11), True)


    def test_eval_poly(self): 
        self.assertEqual(eval_poly(self.p1, 1), 1)
        self.assertEqual(eval_poly(self.p2, 2), 4)
        self.assertEqual(eval_poly(self.p3, 3), 86)
        self.assertEqual(eval_poly(self.p4, -5), 66)
        self.assertEqual(eval_poly(self.p5, 1), 0)
        self.assertEqual(eval_poly(self.p6, 3), -3)
        self.assertEqual(eval_poly(self.p7, -9), -226)
        self.assertEqual(eval_poly(self.p8, 10), 1)
        self.assertEqual(eval_poly(self.p9, 1), 0)
        self.assertEqual(eval_poly(self.p10, 1), 1)

    def test_combine_poly(self): pass

    def test_pow_poly(self): pass

    def test_diff_poly(self): pass

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
