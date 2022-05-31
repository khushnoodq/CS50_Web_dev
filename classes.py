from regex import P
from sympy import Point


class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

pt = Point(10,20)
print(pt)
print(pt.x)
print(pt.y)