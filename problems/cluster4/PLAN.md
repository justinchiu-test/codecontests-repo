# Library Development Plan for Cluster 4

## Overview

This cluster contains primarily geometry and mathematical problems. After examining the existing solutions, I've identified several common patterns and utilities that can be extracted into a reusable library. The goal is to minimize code duplication while maintaining readability and correctness.

## Library Structure

The library will be organized into the following modules:

1. **Input/Output (io)**
   - Fast IO implementation
   - Common input parsing patterns
   - Output formatting

2. **Geometry (geometry)**
   - Point representation and operations
   - Vector operations
   - Line operations (including slope calculations)
   - Common geometric calculations
   - Triangle area/validity
   - Parallelogram calculations

3. **Math Utilities (math)**
   - GCD and other number theory functions
   - Prime number checks
   - Common mathematical operations

4. **Data Structures (ds)**
   - Specialized data structures for geometric problems
   - Counter utilities
   - Collections wrappers

## Detailed Component Design

### 1. Input/Output (io)

```python
# Fast IO implementation
class FastIO:
    # Implementation from existing code
    # ...

# Common input parsing patterns
def read_int():
    """Read a single integer from input."""
    return int(input())

def read_ints():
    """Read a list of integers from a line."""
    return list(map(int, input().split()))

def read_int_tuple():
    """Read integers as tuple."""
    return tuple(map(int, input().split()))

def read_points(n, as_tuples=True):
    """Read n points from input."""
    points = []
    for _ in range(n):
        if as_tuples:
            points.append(tuple(map(int, input().split())))
        else:
            points.append(list(map(int, input().split())))
    return points
```

### 2. Geometry (geometry)

```python
# Point class for 2D coordinates
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def distance_to(self, other):
        """Calculate Euclidean distance between two points."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

# Vector class for 2D vectors
class Vector:
    def __init__(self, p1, p2=None):
        if p2 is None:
            # Treat p1 as (x, y) components directly
            self.x = p1[0]
            self.y = p1[1]
        else:
            # Calculate vector from p1 to p2
            self.x = p2[0] - p1[0]
            self.y = p2[1] - p1[1]

    def normalize(self):
        """Normalize the vector to its simplest form using GCD."""
        g = gcd(abs(self.x), abs(self.y))
        if g == 0:
            return self
        x = self.x // g
        y = self.y // g
        # Standardize direction (ensure x > 0 or if x=0 then y > 0)
        if x < 0 or (x == 0 and y < 0):
            x, y = -x, -y
        return Vector((x, y))

    def dot_product(self, other):
        """Calculate the dot product with another vector."""
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        """Calculate the cross product with another vector."""
        return self.x * other.y - self.y * other.x

    def length_squared(self):
        """Calculate squared length of the vector."""
        return self.x ** 2 + self.y ** 2

    def length(self):
        """Calculate length of the vector."""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def is_parallel(self, other):
        """Check if this vector is parallel to another vector."""
        return self.cross_product(other) == 0

    def angle_with(self, other):
        """Calculate angle between this vector and another vector."""
        dot = self.dot_product(other)
        len1 = self.length()
        len2 = other.length()
        return math.acos(dot / (len1 * len2))

# Line class for line equations (ax + by + c = 0)
class Line:
    def __init__(self, p1, p2=None, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            # Line given by equation ax + by + c = 0
            self.a = a
            self.b = b
            self.c = c
        elif p2 is not None:
            # Line given by two points
            self.a = p1[1] - p2[1]
            self.b = p2[0] - p1[0]
            self.c = p1[0] * p2[1] - p2[0] * p1[1]
            # Normalize coefficients
            g = gcd(gcd(abs(self.a), abs(self.b)), abs(self.c))
            if g != 0:
                self.a //= g
                self.b //= g
                self.c //= g
            # Standardize sign (ensure a > 0 or if a=0 then b > 0)
            if self.a < 0 or (self.a == 0 and self.b < 0):
                self.a, self.b, self.c = -self.a, -self.b, -self.c
        else:
            raise ValueError("Invalid line specification")

    def __eq__(self, other):
        return (self.a, self.b, self.c) == (other.a, other.b, other.c)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def is_parallel(self, other):
        """Check if this line is parallel to another line."""
        return self.a * other.b == self.b * other.a

    def intersects(self, other):
        """Check if this line intersects with another line."""
        return not self.is_parallel(other)

    def contains_point(self, point):
        """Check if this line contains the given point."""
        return self.a * point[0] + self.b * point[1] + self.c == 0

# Utility functions
def calculate_triangle_area(p1, p2, p3):
    """Calculate the area of a triangle using cross product."""
    return abs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2)

def are_collinear(p1, p2, p3):
    """Check if three points are collinear."""
    return calculate_triangle_area(p1, p2, p3) == 0

def fourth_parallelogram_point(p1, p2, p3):
    """Calculate the fourth point of a parallelogram given three points."""
    # Fourth point is p4 where p1 + p3 - p2 = p4
    return (p1[0] + p3[0] - p2[0], p1[1] + p3[1] - p2[1])

def is_supercentral(point, points):
    """Check if a point is supercentral (has neighbors in all four directions)."""
    x, y = point
    left = right = up = down = False

    for px, py in points:
        if px == x and py > y:
            up = True
        elif px == x and py < y:
            down = True
        elif px > x and py == y:
            right = True
        elif px < x and py == y:
            left = True

    return left and right and up and down
```

### 3. Math Utilities (math)

```python
from math import gcd as math_gcd

def gcd(a, b):
    """Calculate the greatest common divisor of two numbers."""
    return math_gcd(a, b)

def is_prime(n):
    """Check if a number is prime."""
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

def binary_to_decimal(binary_str):
    """Convert binary string to decimal."""
    return int(binary_str, 2)

def decimal_to_binary(n):
    """Convert decimal to binary string without '0b' prefix."""
    return bin(n).replace("0b", "")

def count_set_bits(n):
    """Count the number of set bits in a number."""
    return bin(n).count('1')

def is_integer_square(n):
    """Check if a number is a perfect square."""
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n
```

### 4. Data Structures (ds)

```python
from collections import defaultdict, Counter

class SlopeCounter:
    """Class to count lines with the same slope (for line intersection problems)."""
    def __init__(self):
        self.slopes = defaultdict(set)

    def add_line(self, p1, p2):
        """Add a line defined by two points."""
        x1, y1 = p1
        x2, y2 = p2

        a = y1 - y2
        b = x2 - x1

        # Normalize using GCD
        d = gcd(abs(a), abs(b))
        a //= d
        b //= d

        # Standardize the slope representation
        if a < 0 or (a == 0 and b < 0):
            a, b = -a, -b

        # Calculate c in the equation ax - by + c = 0
        c = a * x1 - b * y1

        # Store the line
        self.slopes[(a, b)].add(c)

    def count_unique_lines(self):
        """Count total number of unique lines."""
        return sum(len(lines) for lines in self.slopes.values())

    def count_intersections(self):
        """Count number of line intersections."""
        slope_groups = [(slope, len(lines)) for slope, lines in self.slopes.items()]
        m = len(slope_groups)
        total = 0

        for i in range(m - 1):
            for j in range(i + 1, m):
                # Different slopes will always intersect
                # Multiply line counts from each group to get total intersections
                total += slope_groups[i][1] * slope_groups[j][1]

        return total

class PointSet:
    """Class to store and operate on a set of points."""
    def __init__(self):
        self.points = []
        self.point_set = set()

    def add_point(self, x, y):
        """Add a point to the set."""
        point = (x, y)
        if point not in self.point_set:
            self.points.append(point)
            self.point_set.add(point)

    def get_unique_x_values(self):
        """Get unique x-coordinates."""
        return sorted(set(p[0] for p in self.points))

    def get_unique_y_values(self):
        """Get unique y-coordinates."""
        return sorted(set(p[1] for p in self.points))

    def count_neighbors(self, point):
        """Count neighbors of a point in four directions."""
        x, y = point
        left = sum(1 for px, py in self.points if px < x and py == y)
        right = sum(1 for px, py in self.points if px > x and py == y)
        up = sum(1 for px, py in self.points if px == x and py > y)
        down = sum(1 for px, py in self.points if px == x and py < y)
        return left, right, up, down
```

## Problem Refactoring Strategy

1. **Input/Output Handling**: Replace repetitive parsing code with library functions.
2. **Point and Vector Operations**: Use the Point and Vector classes for calculations.
3. **Line Operations**: Use the Line class for problems involving lines and slopes.
4. **Common Algorithms**: Replace common algorithms with library functions.

## Implementation Plan

I'll implement the library in the following phases:

1. **Basic Structures**: Implement Point, Vector, and Line classes.
2. **IO Functions**: Implement common input parsing patterns.
3. **Utility Functions**: Implement useful mathematical and geometric operations.
4. **Data Structures**: Implement specialized data structures for geometric problems.

## Refactoring Checklist

After implementing the library, I'll refactor each problem solution to use the library components. Here's the initial checklist of all problems in the cluster:

- [ ] 1046_i_say_hello_9380
- [ ] 1163_c1_power_transmission_easy_edition_2411
- [ ] 1163_c2_power_transmission_hard_edition_12093
- [ ] 1271_c_shawarma_tent_643
- [ ] 135_b_rectangle_and_square_9812
- [ ] 136_d_rectangle_and_square_9500
- [ ] 13_b_letter_a_6066
- [ ] 1468_f_full_turn_7213
- [ ] 165_a_supercentral_point_7945
- [ ] 183_b_zoo_1910
- [ ] 2_c_commentator_problem_4414
- [ ] 32_e_hideandseek_3373
- [ ] 334_b_eight_point_sets_7016
- [ ] 407_a_triangle_11184
- [ ] 464_b_restore_cube__2130
- [ ] 498_a_crazy_town_4318
- [ ] 499_c_crazy_town_6399
- [ ] 514_b_han_solo_and_lazer_gun_9314
- [ ] 552_d_vanya_and_triangles_5048
- [ ] 598_f_cut_length_4738
- [ ] 617_d_polyline_7236
- [ ] 618_c_constellation_3489
- [ ] 630_o_arrow_1929
- [ ] 659_d_bicycle_race_5157
- [ ] 749_b_parallelogram_is_back_2975
- [ ] 850_a_five_dimensional_points_3812
- [ ] 886_f_symmetric_projections_6728
- [ ] 889_d_symmetric_projections_6832
- [ ] 934_e_a_colourful_prospect_3399
- [ ] 961_d_pair_of_lines_12769

## Considerations and Tradeoffs

1. **Abstraction Level**: The library needs to balance abstraction with simplicity. Too abstract might make it harder to use, while too simple might not save much code.

2. **Performance**: The library should maintain or improve performance compared to the original solutions.

3. **Readability**: Code using the library should remain readable and intuitive.

4. **Flexibility**: Library components should be adaptable to various problem variations.

As I refactor each problem, I'll update this plan and the checklist to reflect progress and any adjustments needed to the library design.
