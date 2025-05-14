"""
Library file shared across problems.
Provides I/O, math, geometry, and utility functions for reuse.
"""
import sys
from math import gcd, sqrt, asin
from fractions import Fraction
from itertools import combinations

# I/O utilities
def read_int():
    return int(input())

def read_ints():
    return list(map(int, input().split()))

def read_strs():
    return input().split()

def read_point():
    x, y = map(int, input().split())
    return complex(x, y)

def read_points(n):
    return [read_point() for _ in range(n)]

# Math utilities
def lcm(a, b):
    return a // gcd(a, b) * b

def normalize_rational(num, den):
    if den < 0:
        num, den = -num, -den
    g = gcd(abs(num), abs(den))
    if g:
        num //= g
        den //= g
    return num, den

# Geometry utilities using complex for points
def dot(a, b):
    return a.real * b.real + a.imag * b.imag

def cross(a, b):
    return a.real * b.imag - a.imag * b.real

def norm2(a):
    return dot(a, a)

def dist2(a, b):
    dx = a.real - b.real
    dy = a.imag - b.imag
    return dx * dx + dy * dy

def segment_point_dist2(a, b, p):
    v = b - a
    w = p - a
    d2 = norm2(v)
    if d2 == 0:
        return dist2(a, p)
    t = dot(w, v) / d2
    if t <= 0:
        return dist2(a, p)
    if t >= 1:
        return dist2(b, p)
    # squared distance from p to line ab
    return cross(w, v) ** 2 / d2

def segment_segment_dist2(a, b, c, d):
    return min(
        segment_point_dist2(a, b, c),
        segment_point_dist2(a, b, d),
        segment_point_dist2(c, d, a),
        segment_point_dist2(c, d, b),
    )

def line_through(a, b):
    # returns normalized (A, B, C) for line Ax + By + C = 0
    dx = b.real - a.real
    dy = b.imag - a.imag
    A = dy
    B = -dx
    C = dx * a.imag - dy * a.real
    g = gcd(gcd(abs(A), abs(B)), abs(C))
    if g:
        A //= g
        B //= g
        C //= g
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return A, B, C

def intersect_x(line):
    # intersect line Ax+By+C=0 with y=0
    A, B, C = line
    if A == 0:
        return None
    num = -C
    den = A
    if num % den:
        return None
    return num // den

# Shape predicates
def is_square(pts):
    # pts: list of 4 complex points
    ds = [dist2(pts[i], pts[j]) for i in range(4) for j in range(i + 1, 4)]
    ds.sort()
    return (
        ds[0] > 0
        and ds[0] == ds[1] == ds[2] == ds[3]
        and ds[4] == ds[5] == 2 * ds[0]
    )

def is_rectangle(pts):
    ds = [dist2(pts[i], pts[j]) for i in range(4) for j in range(i + 1, 4)]
    ds.sort()
    return (
        ds[0] > 0
        and ds[0] == ds[1]
        and ds[2] == ds[3]
        and ds[4] == ds[5]
        and ds[4] == ds[0] + ds[2]
    )

# Directional counting utility
def best_cardinal_move(x, y, pts):
    up = sum(1 for p in pts if p.imag > y)
    down = sum(1 for p in pts if p.imag < y)
    left = sum(1 for p in pts if p.real < x)
    right = sum(1 for p in pts if p.real > x)
    # order: up, left, right, down to match original tie-breaking
    moves = [
        (up, (x, y + 1)),
        (left, (x - 1, y)),
        (right, (x + 1, y)),
        (down, (x, y - 1)),
    ]
    cnt, (nx, ny) = max(moves, key=lambda m: m[0])
    return cnt, (nx, ny)
