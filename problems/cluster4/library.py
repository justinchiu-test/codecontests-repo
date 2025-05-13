#!/usr/bin/env python3
"""Shared library for code contests problems."""

import os
import sys
from io import BytesIO, IOBase
from math import gcd, sqrt
from collections import defaultdict, Counter

# IO utilities
class FastIO(IOBase):
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
        self.newlines = 0

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, 8192))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, 8192))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

def setup_io():
    """Set up fast IO wrappers and input functions."""
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    return lambda: sys.stdin.readline().rstrip()

# Common input patterns
def int_input(input_func=input):
    """Read a single integer from input."""
    return int(input_func())

def ints_input(input_func=input):
    """Read a list of integers from a single line."""
    return list(map(int, input_func().split()))

def int_tuple_input(input_func=input):
    """Read a tuple of integers from a single line."""
    return tuple(map(int, input_func().split()))

def ints_grid(n, input_func=input):
    """Read an n-line grid of integers."""
    return [ints_input(input_func) for _ in range(n)]

def points_input(n, input_func=input):
    """Read n 2D points from input."""
    return [int_tuple_input(input_func) for _ in range(n)]

# Geometry utilities
def vector(p1, p2):
    """Create a vector from p1 to p2."""
    return (p2[0] - p1[0], p2[1] - p1[1])

def normalize_vector(v):
    """Normalize a vector using GCD."""
    if v[0] == 0 and v[1] == 0:
        return (0, 0)
    if v[0] == 0:
        return (0, 1 if v[1] > 0 else -1)
    if v[1] == 0:
        return (1 if v[0] > 0 else -1, 0)
    
    g = gcd(abs(v[0]), abs(v[1]))
    # Keep the sign consistent between original and Han Solo problem
    if v[0] < 0:
        return (-v[0] // g, -v[1] // g)
    return (v[0] // g, v[1] // g)

def dot_product(v1, v2):
    """Calculate the dot product of two vectors."""
    return v1[0] * v2[0] + v1[1] * v2[1]

def cross_product(v1, v2):
    """Calculate the cross product of two vectors."""
    return v1[0] * v2[1] - v1[1] * v2[0]

def dist_squared(p1, p2):
    """Calculate the square of the distance between two points."""
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def dist(p1, p2):
    """Calculate the distance between two points."""
    return sqrt(dist_squared(p1, p2))

def collinear(p1, p2, p3):
    """Check if three points are collinear."""
    return cross_product(vector(p1, p2), vector(p1, p3)) == 0

def perpendicular(v1, v2):
    """Check if two vectors are perpendicular."""
    return dot_product(v1, v2) == 0

def slope(p1, p2):
    """Calculate the slope between two points."""
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    
    if dx == 0:
        return float('inf')
    return dy / dx

def unique_slopes(points, origin=(0, 0)):
    """Count the number of unique slopes from the origin to the points."""
    slopes = set()
    for p in points:
        if p == origin:  # Skip origin
            continue
        dx = p[0] - origin[0]
        dy = p[1] - origin[1]
        
        if dx == 0:
            slopes.add(float('inf'))
        else:
            # Keep track of the slope as a rational number
            g = gcd(abs(dx), abs(dy))
            if dx < 0:
                dx, dy = -dx, -dy
            slopes.add((dx // g, dy // g))
    
    return len(slopes)

def slope_counter(points, origin):
    """Count occurrences of slopes from the origin to the points."""
    counter = Counter()
    for p in points:
        if p == origin:
            continue
        v = vector(origin, p)
        counter[normalize_vector(v)] += 1
    return counter

def line_equation(p1, p2):
    """
    Get the equation of a line in the form ax + by + c = 0
    where gcd(a, b) = 1 and a >= 0 (or a = 0 and b = 1)
    """
    a = p2[1] - p1[1]
    b = p1[0] - p2[0]
    c = p1[1] * p2[0] - p1[0] * p2[1]

    # Normalize coefficients
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    
    if a == 0 and b == 0:
        return (0, 0, 0)
    
    g = abs(gcd(a, b) if a != 0 and b != 0 else (abs(a) if a != 0 else abs(b)))
    if c != 0:
        g = gcd(g, abs(c))
    
    return (a // g, b // g, c // g)

def point_on_line(p, line):
    """Check if a point is on a line (ax + by + c = 0)."""
    a, b, c = line
    return a * p[0] + b * p[1] + c == 0

def are_points_on_two_lines(points, find_two_lines=False):
    """
    Check if points can be covered by two lines.
    
    If find_two_lines is True, return the two lines as well.
    """
    n = len(points)
    if n <= 4:
        return True, (None, None) if find_two_lines else True
    
    # Try all pairs of points to form the first line
    for i in range(n):
        for j in range(i+1, n):
            p1, p2 = points[i], points[j]
            if p1 == p2:
                continue
                
            line1 = line_equation(p1, p2)
            remaining_points = []
            
            for k in range(n):
                if not point_on_line(points[k], line1):
                    remaining_points.append(points[k])
            
            # If 0 or 1 points remain, we're done
            if len(remaining_points) <= 1:
                if find_two_lines:
                    line2 = (0, 0, 0) if not remaining_points else line_equation(remaining_points[0], remaining_points[0])
                    return True, (line1, line2)
                return True
            
            # If 2+ points remain, they should all be on a second line
            p3, p4 = remaining_points[0], remaining_points[1]
            line2 = line_equation(p3, p4)
            
            all_on_second_line = True
            for p in remaining_points[2:]:
                if not point_on_line(p, line2):
                    all_on_second_line = False
                    break
            
            if all_on_second_line:
                if find_two_lines:
                    return True, (line1, line2)
                return True
                
    return (False, (None, None)) if find_two_lines else False

def is_square(points):
    """Check if the given 4 points form a square."""
    if len(points) != 4:
        return False
    
    # Calculate all pairwise distances
    dists = []
    for i in range(4):
        for j in range(i+1, 4):
            dists.append(dist_squared(points[i], points[j]))
    
    dists.sort()
    
    # Should have 4 equal sides and 2 equal diagonals
    return (dists[0] == dists[1] == dists[2] == dists[3] and 
            dists[4] == dists[5] and 
            dists[0] * 2 == dists[4])  # Pythagorean theorem

def is_rectangle(points):
    """Check if the given 4 points form a rectangle."""
    if len(points) != 4:
        return False
    
    # Calculate all pairwise distances
    dists = []
    for i in range(4):
        for j in range(i+1, 4):
            dists.append(dist_squared(points[i], points[j]))
    
    dists.sort()
    
    # Should have 2 pairs of equal sides and 2 equal diagonals
    return (dists[0] == dists[1] and dists[2] == dists[3] and 
            dists[4] == dists[5])

def parallelogram_fourth_point(p1, p2, p3):
    """Find the fourth point of a parallelogram given three points."""
    return (p1[0] + p3[0] - p2[0], p1[1] + p3[1] - p2[1])

def supercentral_point(points):
    """Count supercentral points in a set of points."""
    count = 0
    for i, p in enumerate(points):
        has_right = has_left = has_up = has_down = False
        
        for j, q in enumerate(points):
            if i == j:
                continue
                
            if p[0] < q[0] and p[1] == q[1]:
                has_right = True
            elif p[0] > q[0] and p[1] == q[1]:
                has_left = True
            elif p[0] == q[0] and p[1] < q[1]:
                has_up = True
            elif p[0] == q[0] and p[1] > q[1]:
                has_down = True
                
        if has_right and has_left and has_up and has_down:
            count += 1
            
    return count