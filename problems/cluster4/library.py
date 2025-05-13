"""
Shared utility library for problem cluster.
Provides common input parsing, math, data structures, and geometry utilities.
"""
import sys

# fast input
input = sys.stdin.readline
def getint():
    """Read a line and parse a single integer."""
    return int(input())

def getints():
    """Read a line and parse integers, returning an iterator of ints."""
    return map(int, input().split())

def getstr():
    """Read a line as string without trailing newline."""
    return input().rstrip("\n")

# math utilities
from math import gcd as _gcd

def gcd(a, b):
    """Greatest common divisor."""
    return _gcd(a, b)

def lcm(a, b):
    """Least common multiple."""
    return a // _gcd(a, b) * b if a and b else 0

# Disjoint Set Union (Union-Find)
class DSU:
    """Disjoint set union with path compression."""
    __slots__ = ('parent',)

    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        p = self.parent
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    def union(self, a, b):
        """Union sets containing a and b."""
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            self.parent[pb] = pa

# 2D vector for geometry
class Vector:
    """2D vector with basic operations."""
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def norm2(self):
        """Square of Euclidean norm."""
        return self.dot(self)

    norm_square = norm2

    def __repr__(self):
        return f"({self.x}, {self.y})"

# Priority queue (min-heap wrapper)
class PriorityQueue:
    """Min-heap priority queue."""
    __slots__ = ('_data',)

    def __init__(self):
        import heapq
        self._data = []
        self._heapq = heapq

    def push(self, item):
        """Push an item onto the queue."""
        self._heapq.heappush(self._data, item)

    def pop(self):
        """Pop the smallest item."""
        return self._heapq.heappop(self._data)

    def __len__(self):
        return len(self._data)
