"""Library file for cluster4.
This contains shared code that can be imported by problems in this cluster."""
import sys
import math
from math import gcd as math_gcd, acos
from collections import defaultdict, Counter

# IO utilities
def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def read_int_tuple():
    return tuple(map(int, sys.stdin.readline().split()))

def read_points(n, as_tuples=True):
    pts = []
    for _ in range(n):
        if as_tuples:
            pts.append(tuple(map(int, sys.stdin.readline().split())))
        else:
            pts.append(list(map(int, sys.stdin.readline().split())))
    return pts

# Math utilities
def gcd(a, b):
    return math_gcd(a, b)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def binary_to_decimal(s):
    return int(s, 2)

def decimal_to_binary(n):
    return bin(n)[2:]

def count_set_bits(n):
    return bin(n).count('1')

def is_integer_square(n):
    r = int(n**0.5)
    return r*r == n

# Geometry utilities
class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))
    def distance_to(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

class Vector:
    __slots__ = ('x', 'y')
    def __init__(self, x, y=None):
        if y is None:
            self.x, self.y = x
        else:
            self.x, self.y = x, y
    @classmethod
    def from_points(cls, p1, p2):
        return cls(p2[0] - p1[0], p2[1] - p1[1])
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar):
        """Scalar multiplication of vector."""
        return Vector(self.x * scalar, self.y * scalar)
    __rmul__ = __mul__
    def dot(self, other):
        return self.x*other.x + self.y*other.y
    def cross(self, other):
        return self.x*other.y - self.y*other.x
    def norm_sq(self):
        return self.dot(self)
    def length(self):
        return (self.x**2 + self.y**2)**0.5
    def normalize(self):
        g = gcd(abs(self.x), abs(self.y))
        if g == 0:
            return Vector(self.x, self.y)
        x, y = self.x//g, self.y//g
        if x < 0 or (x == 0 and y < 0):
            x, y = -x, -y
        return Vector(x, y)
    def is_parallel(self, other):
        return self.cross(other) == 0
    def angle_with(self, other):
        return acos(self.dot(other)/(self.length()*other.length()))

def dist_point_segment_sq(p, v1, v2):
    """Return the squared distance from point p to the segment defined by v1 and v2."""
    # p, v1, v2: Vector objects
    seg = v2 - v1
    denom = seg.norm_sq()
    if denom == 0:
        # v1 == v2, distance to point v1
        delta = p - v1
        return delta.norm_sq()
    # projection parameter t in [0,1]
    t = ( (p - v1).dot(seg) ) / denom
    if t < 0:
        delta = p - v1
        return delta.norm_sq()
    if t > 1:
        delta = p - v2
        return delta.norm_sq()
    proj = v1 + seg * t
    delta = p - proj
    return delta.norm_sq()

class Line:
    __slots__ = ('a', 'b', 'c')
    def __init__(self, p1=None, p2=None, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            self.a, self.b, self.c = a, b, c
        elif p1 is not None and p2 is not None:
            x1, y1 = p1; x2, y2 = p2
            a0 = y1 - y2
            b0 = x2 - x1
            c0 = x1*y2 - x2*y1
            g = gcd(gcd(abs(a0), abs(b0)), abs(c0))
            if g:
                a0//=g; b0//=g; c0//=g
            if a0<0 or (a0==0 and b0<0):
                a0, b0, c0 = -a0, -b0, -c0
            self.a, self.b, self.c = a0, b0, c0
        else:
            raise ValueError("Invalid Line parameters")
    def is_parallel(self, other):
        return self.a*other.b == self.b*other.a
    def intersects(self, other):
        return not self.is_parallel(other)
    def contains(self, p):
        return self.a*p[0] + self.b*p[1] + self.c == 0

def triangle_area(p1, p2, p3):
    return abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))/2)

def are_collinear(p1, p2, p3):
    return triangle_area(p1, p2, p3) == 0

def fourth_parallelogram_point(p1, p2, p3):
    return (p1[0] + p3[0] - p2[0], p1[1] + p3[1] - p2[1])

def is_supercentral(pt, points):
    x, y = pt
    left = right = up = down = False
    for px, py in points:
        if px == x and py > y:
            up = True
        elif px == x and py < y:
            down = True
        elif py == y and px > x:
            right = True
        elif py == y and px < x:
            left = True
    return left and right and up and down

class SlopeCounter:
    def __init__(self):
        self.slopes = defaultdict(set)
    def add_line(self, p1, p2):
        a = p1[1] - p2[1]
        b = p2[0] - p1[0]
        d = gcd(abs(a), abs(b))
        if d:
            a//=d; b//=d
        if a<0 or (a==0 and b<0):
            a, b = -a, -b
        c = a*p1[0] - b*p1[1]
        self.slopes[(a,b)].add(c)
    def count_unique(self):
        return sum(len(v) for v in self.slopes.values())
    def intersections(self):
        groups = [len(v) for v in self.slopes.values()]
        res = 0
        for i in range(len(groups)):
            for j in range(i+1, len(groups)):
                res += groups[i]*groups[j]
        return res

class PointSet:
    def __init__(self):
        self.points = []
        self.set = set()
    def add(self, x, y):
        if (x,y) not in self.set:
            self.points.append((x,y))
            self.set.add((x,y))
    def unique_x(self):
        return sorted({p[0] for p in self.points})
    def unique_y(self):
        return sorted({p[1] for p in self.points})
    def neighbors(self, pt):
        x, y = pt; l=r=u=d = 0
        for px, py in self.points:
            if px < x and py == y: l+=1
            elif px > x and py == y: r+=1
            elif px == x and py > y: u+=1
            elif px == x and py < y: d+=1
        return l, r, u, d
