"""
Library file for cluster4.
This contains shared code for fast I/O and 2D geometry operations.
"""
import sys, math
from math import gcd, atan2, pi, hypot

_data = sys.stdin.read().split()
_it = iter(_data)

def ni():  # next int
    return int(next(_it))

def nf():  # next float
    return float(next(_it))

def ns():  # next string
    return next(_it)

def na(n):  # list of n ints
    return [ni() for _ in range(n)]

def eq(a, b, eps=1e-9):
    return abs(a - b) < eps

class Vec:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, o):
        return Vec(self.x + o.x, self.y + o.y)
    def __sub__(self, o):
        return Vec(self.x - o.x, self.y - o.y)
    def dot(self, o):
        return self.x * o.x + self.y * o.y
    def cross(self, o):
        return self.x * o.y - self.y * o.x
    def norm2(self):
        return self.dot(self)
    def norm(self):
        r = hypot(self.x, self.y)
        return Vec(self.x / r, self.y / r) if r else Vec(self.x, self.y)
    def rotate90(self):  # 90-degree CCW
        return Vec(-self.y, self.x)
    def scale(self, k):
        return Vec(self.x * k, self.y * k)
    def angle(self, o):
        return atan2(self.cross(o), self.dot(o))
    def __repr__(self):
        return f"Vec({self.x},{self.y})"
    def __mul__(self, k):  # scale by scalar (v * k)
        if isinstance(k, (int, float)):
            return Vec(self.x * k, self.y * k)
        return NotImplemented
    __rmul__ = __mul__
    def __truediv__(self, k):  # divide by scalar (v / k)
        return Vec(self.x / k, self.y / k)
    def __abs__(self):  # vector magnitude
        return hypot(self.x, self.y)
    def rotate(self, theta):  # rotate by angle theta (radians) CCW
        c, s = math.cos(theta), math.sin(theta)
        return Vec(self.x * c - self.y * s, self.x * s + self.y * c)
