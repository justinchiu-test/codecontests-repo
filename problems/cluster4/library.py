"""
Library file for cluster4.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
import math
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from fractions import Fraction
from typing import List, Tuple, Dict, Set, Optional, Union, Any, Callable, Iterator

# Fast I/O
class FastIO:
    def __init__(self):
        self.buffer = []
        self.index = 0
        self.readline = lambda: sys.stdin.readline().rstrip()
    
    def next_line(self) -> str:
        return self.readline()
    
    def next_int(self) -> int:
        return int(self.readline())
    
    def next_float(self) -> float:
        return float(self.readline())
    
    def next_ints(self) -> List[int]:
        return list(map(int, self.readline().split()))
    
    def next_floats(self) -> List[float]:
        return list(map(float, self.readline().split()))
    
    def next_token(self) -> str:
        while self.index >= len(self.buffer):
            self.buffer = self.readline().split()
            self.index = 0
        self.index += 1
        return self.buffer[self.index - 1]
    
    def next_tokens(self, n: int) -> List[str]:
        return [self.next_token() for _ in range(n)]
    
    def next_int_token(self) -> int:
        return int(self.next_token())
    
    def next_float_token(self) -> float:
        return float(self.next_token())
    
    def next_int_tokens(self, n: int) -> List[int]:
        return [self.next_int_token() for _ in range(n)]
    
    def next_float_tokens(self, n: int) -> List[float]:
        return [self.next_float_token() for _ in range(n)]

io = FastIO()

# Print utilities
def print_answer(answer):
    """Print the answer in the format required by the problem."""
    if isinstance(answer, bool):
        print("YES" if answer else "NO")
    elif isinstance(answer, (list, tuple)):
        print(*answer)
    else:
        print(answer)

# Point and Vector operations
class Point:
    def __init__(self, x: Union[int, float], y: Union[int, float]):
        self.x = x
        self.y = y
    
    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __str__(self) -> str:
        return f"{self.x} {self.y}"
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"
    
    def distance(self, other: "Point") -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
    def distance_squared(self, other: "Point") -> Union[int, float]:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2
    
    def manhattan_distance(self, other: "Point") -> Union[int, float]:
        return abs(self.x - other.x) + abs(self.y - other.y)
    
    def cross_product(self, other: "Point") -> Union[int, float]:
        return self.x * other.y - self.y * other.x
    
    def dot_product(self, other: "Point") -> Union[int, float]:
        return self.x * other.x + self.y * other.y
    
    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def length_squared(self) -> Union[int, float]:
        return self.x * self.x + self.y * self.y
    
    def normalize(self) -> "Point":
        """Normalize the vector to a unit vector."""
        length = self.length()
        if length > 0:
            return Point(self.x / length, self.y / length)
        return Point(0, 0)
        
    def perpendicular(self, other: "Point") -> bool:
        """Check if two vectors are perpendicular."""
        return abs(self.dot_product(other)) < 1e-9
        
    def parallel(self, other: "Point") -> bool:
        """Check if two vectors are parallel."""
        return abs(self.cross_product(other)) < 1e-9

# Vector2D class (for compatibility with some problems)
class Vector2D:
    def __init__(self, p1, p2=None):
        if p2 is None:  # If only one parameter, treat it as a vector
            self.x = p1[0] if isinstance(p1, tuple) else p1.x
            self.y = p1[1] if isinstance(p1, tuple) else p1.y
        else:  # If two parameters, treat them as points and compute vector
            if isinstance(p1, tuple) and isinstance(p2, tuple):
                self.x = p2[0] - p1[0]
                self.y = p2[1] - p1[1]
            else:
                self.x = p2[0] - p1[0] if isinstance(p2, tuple) else p2.x - p1[0]
                self.y = p2[1] - p1[1] if isinstance(p2, tuple) else p2.y - p1[1]
    
    def __sub__(self, other):
        return Vector2D((self.x - other.x, self.y - other.y))
    
    def distance_square(self):
        return self.x ** 2 + self.y ** 2
    
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y
    
    def cross_product(self, other):
        return self.x * other.y - self.y * other.x
    
    def parallel(self, other):
        return self.cross_product(other) == 0
    
    def acute_or_perpendicular(self, other):
        return self.dot_product(other) >= 0 and not self.parallel(other)

# Geometric utilities
def gcd(a: int, b: int) -> int:
    """Greatest common divisor using Euclidean algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def normalize_vector(x: int, y: int) -> Tuple[int, int]:
    """Normalize a vector to its simplest form using GCD."""
    if x == 0 and y == 0:
        return (0, 0)
    
    # Handle the case where either coordinate is zero
    if x == 0:
        return (0, 1 if y > 0 else -1)
    if y == 0:
        return (1 if x > 0 else -1, 0)
    
    # Ensure the vector has the correct sign convention
    # For this application, we want the first non-zero component to be positive
    if x < 0:
        x, y = -x, -y
    
    # Calculate GCD and normalize
    d = gcd(abs(x), abs(y))
    return (x // d, y // d)

def cross_product(p1: Union[Point, Tuple, Vector2D], p2: Union[Point, Tuple, Vector2D]) -> Union[int, float]:
    """Calculate the cross product of two points/vectors."""
    if isinstance(p1, Point) and isinstance(p2, Point):
        return p1.cross_product(p2)
    elif isinstance(p1, Vector2D) and isinstance(p2, Vector2D):
        return p1.cross_product(p2)
    elif isinstance(p1, tuple) and isinstance(p2, tuple):
        return p1[0] * p2[1] - p1[1] * p2[0]
    elif isinstance(p1, Point) and isinstance(p2, tuple):
        return p1.x * p2[1] - p1.y * p2[0]
    elif isinstance(p1, tuple) and isinstance(p2, Point):
        return p1[0] * p2.y - p1[1] * p2.x
    elif isinstance(p1, Vector2D) and isinstance(p2, tuple):
        return p1.x * p2[1] - p1.y * p2[0]
    elif isinstance(p1, tuple) and isinstance(p2, Vector2D):
        return p1[0] * p2.y - p1[1] * p2.x
    raise TypeError("Parameters must be Points, Tuples, or Vector2D")

def dot_product(p1: Union[Point, Tuple, Vector2D], p2: Union[Point, Tuple, Vector2D]) -> Union[int, float]:
    """Calculate the dot product of two points/vectors."""
    if isinstance(p1, Point) and isinstance(p2, Point):
        return p1.dot_product(p2)
    elif isinstance(p1, Vector2D) and isinstance(p2, Vector2D):
        return p1.dot_product(p2)
    elif isinstance(p1, tuple) and isinstance(p2, tuple):
        return p1[0] * p2[0] + p1[1] * p2[1]
    elif isinstance(p1, Point) and isinstance(p2, tuple):
        return p1.x * p2[0] + p1.y * p2[1]
    elif isinstance(p1, tuple) and isinstance(p2, Point):
        return p1[0] * p2.x + p1[1] * p2.y
    elif isinstance(p1, Vector2D) and isinstance(p2, tuple):
        return p1.x * p2[0] + p1.y * p2[1]
    elif isinstance(p1, tuple) and isinstance(p2, Vector2D):
        return p1[0] * p2.x + p1[1] * p2.y
    raise TypeError("Parameters must be Points, Tuples, or Vector2D")

def orientation(p: Point, q: Point, r: Point) -> int:
    """
    Return the orientation of triplet (p, q, r).
    0 --> Collinear
    1 --> Clockwise
    2 --> Counterclockwise
    """
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or Counterclockwise

def are_collinear(p1: Point, p2: Point, p3: Point) -> bool:
    """Check if three points are collinear."""
    return orientation(p1, p2, p3) == 0

def triangle_area(p1: Point, p2: Point, p3: Point) -> float:
    """Calculate the area of a triangle formed by three points."""
    return abs((p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)) / 2)

def is_point_on_segment(p: Point, segment_start: Point, segment_end: Point) -> bool:
    """Check if a point lies on a line segment."""
    # Check if point is collinear with segment endpoints
    if orientation(segment_start, p, segment_end) != 0:
        return False
    
    # Check if point is within the bounding box of the segment
    if (p.x <= max(segment_start.x, segment_end.x) and p.x >= min(segment_start.x, segment_end.x) and
        p.y <= max(segment_start.y, segment_end.y) and p.y >= min(segment_start.y, segment_end.y)):
        return True
    
    return False

def line_equation_from_points(p1: Point, p2: Point) -> Tuple[float, float, float]:
    """
    Convert two points to a line equation ax + by + c = 0.
    Returns coefficients (a, b, c).
    """
    a = p2.y - p1.y
    b = p1.x - p2.x
    c = p2.x * p1.y - p1.x * p2.y
    return a, b, c

def point_to_line_distance(p: Point, line_coeffs: Tuple[float, float, float]) -> float:
    """Calculate the distance from a point to a line defined by ax + by + c = 0."""
    a, b, c = line_coeffs
    return abs(a * p.x + b * p.y + c) / math.sqrt(a * a + b * b)

def point_to_segment_distance(p: Point, segment_start: Point, segment_end: Point) -> float:
    """Calculate the distance from a point to a line segment."""
    # If segment is actually a point
    if segment_start == segment_end:
        return p.distance(segment_start)
    
    # Calculate the projection of point onto the line containing the segment
    line_length_squared = (segment_end.x - segment_start.x) ** 2 + (segment_end.y - segment_start.y) ** 2
    t = max(0, min(1, ((p.x - segment_start.x) * (segment_end.x - segment_start.x) + 
                       (p.y - segment_start.y) * (segment_end.y - segment_start.y)) / line_length_squared))
    
    # Calculate the closest point on the segment
    closest_x = segment_start.x + t * (segment_end.x - segment_start.x)
    closest_y = segment_start.y + t * (segment_end.y - segment_start.y)
    
    return p.distance(Point(closest_x, closest_y))

# Line representation for problems involving lines
class Line:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
    
    @classmethod
    def from_points(cls, p1: Point, p2: Point) -> "Line":
        """Create a line from two points."""
        a = p2.y - p1.y
        b = p1.x - p2.x
        c = p2.x * p1.y - p1.x * p2.y
        return cls(a, b, c)
    
    @classmethod
    def from_point_and_slope(cls, p: Point, slope: float) -> "Line":
        """Create a line from a point and a slope."""
        if math.isinf(slope):
            # Vertical line
            return cls(1, 0, -p.x)
        else:
            a = -slope
            b = 1
            c = slope * p.x - p.y
            return cls(a, b, c)
    
    def __eq__(self, other: "Line") -> bool:
        """Check if two lines are equal."""
        # Normalize to compare
        if self.a == 0 and self.b == 0:
            return other.a == 0 and other.b == 0
        
        if other.a == 0 and other.b == 0:
            return self.a == 0 and self.b == 0
        
        if self.a == 0:
            return other.a == 0 and (abs(self.c / self.b - other.c / other.b) < 1e-9)
        
        if self.b == 0:
            return other.b == 0 and (abs(self.c / self.a - other.c / other.a) < 1e-9)
        
        # General case
        k1 = -self.c / self.a
        k2 = -self.c / self.b
        k3 = -other.c / other.a
        k4 = -other.c / other.b
        
        return abs(k1 - k3) < 1e-9 and abs(k2 - k4) < 1e-9
    
    def __hash__(self) -> int:
        # Normalize for hashing
        if self.a == 0 and self.b == 0:
            return hash((0, 0, 0))
        
        if self.a == 0:
            sign = 1 if self.b > 0 else -1
            return hash((0, 1, sign * self.c / abs(self.b)))
        
        if self.b == 0:
            sign = 1 if self.a > 0 else -1
            return hash((1, 0, sign * self.c / abs(self.a)))
        
        # General case, normalize so that a^2 + b^2 = 1
        norm = math.sqrt(self.a * self.a + self.b * self.b)
        sign = 1 if self.a > 0 or (self.a == 0 and self.b > 0) else -1
        return hash((sign * self.a / norm, sign * self.b / norm, sign * self.c / norm))
    
    def is_parallel(self, other: "Line") -> bool:
        """Check if two lines are parallel."""
        return abs(self.a * other.b - self.b * other.a) < 1e-9
    
    def is_perpendicular(self, other: "Line") -> bool:
        """Check if two lines are perpendicular."""
        return abs(self.a * other.a + self.b * other.b) < 1e-9
    
    def point_side(self, p: Point) -> int:
        """
        Determine which side of the line a point is on.
        Returns:
         1 if point is on one side
        -1 if point is on the other side
         0 if point is on the line
        """
        val = self.a * p.x + self.b * p.y + self.c
        if abs(val) < 1e-9:
            return 0
        return 1 if val > 0 else -1
    
    def contains_point(self, p: Point) -> bool:
        """Check if a point lies on the line."""
        return abs(self.a * p.x + self.b * p.y + self.c) < 1e-9
    
    def intersection(self, other: "Line") -> Optional[Point]:
        """Find the intersection point of two lines."""
        det = self.a * other.b - self.b * other.a
        if abs(det) < 1e-9:  # Parallel or coincident lines
            return None
        
        x = (self.b * other.c - self.c * other.b) / det
        y = (self.c * other.a - self.a * other.c) / det
        return Point(x, y)

# Polygon operations
def polygon_area(points: List[Point]) -> float:
    """Calculate the area of a polygon using the Shoelace formula."""
    n = len(points)
    if n < 3:
        return 0.0
    
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += points[i].x * points[j].y - points[j].x * points[i].y
    
    return abs(area) / 2.0

def is_point_in_polygon(p: Point, polygon: List[Point]) -> bool:
    """
    Check if a point is inside a polygon.
    Uses the ray casting algorithm.
    """
    n = len(polygon)
    if n < 3:
        return False
    
    inside = False
    for i in range(n):
        j = (i + 1) % n
        
        if ((polygon[i].y > p.y) != (polygon[j].y > p.y)) and \
           (p.x < (polygon[j].x - polygon[i].x) * (p.y - polygon[i].y) / 
            (polygon[j].y - polygon[i].y) + polygon[i].x):
            inside = not inside
    
    return inside

def convex_hull(points: List[Point]) -> List[Point]:
    """
    Calculate the convex hull of a set of points using Graham scan algorithm.
    Returns a list of points forming the convex hull in counterclockwise order.
    """
    if len(points) <= 2:
        return points
    
    # Find the lowest point (and leftmost if tie)
    lowest = min(points, key=lambda p: (p.y, p.x))
    
    # Sort points by polar angle with respect to the lowest point
    def polar_angle(p):
        return math.atan2(p.y - lowest.y, p.x - lowest.x)
    
    sorted_points = sorted(points, key=polar_angle)
    
    # Graham scan
    hull = [sorted_points[0], sorted_points[1]]
    for i in range(2, len(sorted_points)):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], sorted_points[i]) != 2:
            hull.pop()
        hull.append(sorted_points[i])
    
    return hull

# Input parsing utilities
def read_n_points(n: int) -> List[Point]:
    """Read n points from input."""
    return [Point(*io.next_ints()) for _ in range(n)]

def read_int() -> int:
    """Read a single integer."""
    return io.next_int()

def read_ints() -> List[int]:
    """Read a line of integers."""
    return io.next_ints()

def read_float() -> float:
    """Read a single float."""
    return io.next_float()

def read_floats() -> List[float]:
    """Read a line of floats."""
    return io.next_floats()

def read_test_cases(func: Callable) -> None:
    """Run a function multiple times based on the first integer in input."""
    t = read_int()
    for _ in range(t):
        func()