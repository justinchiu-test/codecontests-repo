"""
Library file for cluster4.
This contains shared code that can be imported by problems in this cluster.
"""
from math import sqrt, gcd, atan2, pi, hypot, cos, sin, asin, degrees
from collections import defaultdict
from itertools import combinations
import sys


class Point:
    """A 2D point/vector class with common operations."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __neg__(self):
        return Point(-self.x, -self.y)
    
    def __eq__(self, other):
        return abs(self.x - other.x) < 1e-9 and abs(self.y - other.y) < 1e-9
    
    def __hash__(self):
        return hash((round(self.x, 9), round(self.y, 9)))
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def dot(self, other):
        """Dot product with another point/vector."""
        return self.x * other.x + self.y * other.y
    
    def cross(self, other):
        """Cross product with another point/vector (magnitude only in 2D)."""
        return self.x * other.y - self.y * other.x
    
    def norm_square(self):
        """Square of the Euclidean norm."""
        return self.x * self.x + self.y * self.y
    
    def norm(self):
        """Euclidean norm (length) of the vector."""
        return sqrt(self.norm_square())
    
    def distance(self, other):
        """Distance to another point."""
        return (self - other).norm()
    
    def normalize(self):
        """Return a normalized unit vector in the same direction."""
        length = self.norm()
        if length < 1e-9:
            return Point(0, 0)
        return Point(self.x / length, self.y / length)
    
    def angle(self):
        """Returns the angle in radians from the positive x-axis."""
        return atan2(self.y, self.x)
    
    def rotate(self, angle):
        """Rotate the vector by angle radians counter-clockwise."""
        cos_a = cos(angle)
        sin_a = sin(angle)
        return Point(self.x * cos_a - self.y * sin_a, self.x * sin_a + self.y * cos_a)


class Line:
    """A line in 2D space, represented by ax + by + c = 0 form."""
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        # Normalize coefficients
        norm = sqrt(a*a + b*b)
        if abs(norm) > 1e-9:
            self.a, self.b, self.c = a/norm, b/norm, c/norm
    
    @staticmethod
    def from_points(p1, p2):
        """Create a line from two points."""
        if abs(p1.x - p2.x) < 1e-9:  # Vertical line
            return Line(1, 0, -p1.x)
        a = -(p1.y - p2.y) / (p1.x - p2.x)
        b = 1
        c = -(a * p1.x + b * p1.y)
        return Line(a, b, c)
    
    @staticmethod
    def from_point_slope(p, slope):
        """Create a line from a point and a slope."""
        if abs(slope) > 1e9:  # Near vertical line
            return Line(1, 0, -p.x)
        a = -slope
        b = 1
        c = -(a * p.x + b * p.y)
        return Line(a, b, c)
    
    def distance_to_point(self, p):
        """Distance from the line to a point."""
        return abs(self.a * p.x + self.b * p.y + self.c) / sqrt(self.a*self.a + self.b*self.b)
    
    def intersection(self, other):
        """Find the intersection point with another line."""
        det = self.a * other.b - self.b * other.a
        if abs(det) < 1e-9:  # Parallel or coincident lines
            return None
        x = (self.b * other.c - self.c * other.b) / det
        y = (self.c * other.a - self.a * other.c) / det
        return Point(x, y)
    
    def is_parallel(self, other):
        """Check if this line is parallel to another line."""
        return abs(self.a * other.b - self.b * other.a) < 1e-9
    
    def is_same(self, other):
        """Check if this line is the same as another line."""
        return (self.is_parallel(other) and
                abs(self.a * other.c - self.c * other.a) < 1e-9 and
                abs(self.b * other.c - self.c * other.b) < 1e-9)

    def normalize_rational(self):
        """Return a normalized representation of the line equation as a tuple (a, b, c).
        This is useful for comparing or hashing lines."""
        a, b, c = self.a, self.b, self.c

        # Ensure the first non-zero coefficient is positive
        if abs(a) > 1e-9:
            if a < 0:
                a, b, c = -a, -b, -c
        elif abs(b) > 1e-9:
            if b < 0:
                a, b, c = -a, -b, -c
        else:
            if c < 0:
                a, b, c = -a, -b, -c

        # Reduce by GCD if all coefficients are integers
        if all(abs(val - round(val)) < 1e-9 for val in (a, b, c)):
            a, b, c = int(round(a)), int(round(b)), int(round(c))
            g = abs(gcd(gcd(a, b), c))
            if g > 0:
                a, b, c = a // g, b // g, c // g

        return (a, b, c)
    
    def __str__(self):
        return f"{self.a}x + {self.b}y + {self.c} = 0"


class Segment:
    """A line segment in 2D space, represented by its endpoints."""
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def length(self):
        """Length of the segment."""
        return self.p1.distance(self.p2)
    
    def as_line(self):
        """Convert to a Line object."""
        return Line.from_points(self.p1, self.p2)
    
    def point_on_segment(self, p, epsilon=1e-9):
        """Check if a point is on the segment."""
        if p == self.p1 or p == self.p2:
            return True
        
        # Check if the point is on the line
        if abs((p.y - self.p1.y) * (self.p2.x - self.p1.x) - 
               (p.x - self.p1.x) * (self.p2.y - self.p1.y)) > epsilon:
            return False
        
        # Check if the point is within the segment's bounding box
        return (min(self.p1.x, self.p2.x) - epsilon <= p.x <= max(self.p1.x, self.p2.x) + epsilon and
                min(self.p1.y, self.p2.y) - epsilon <= p.y <= max(self.p1.y, self.p2.y) + epsilon)
    
    def distance_to_point(self, p):
        """Distance from the segment to a point."""
        line = self.as_line()
        line_dist = line.distance_to_point(p)
        
        # Check if the perpendicular projection of p onto the line falls on the segment
        segment_vector = self.p2 - self.p1
        p_vector = p - self.p1
        t = segment_vector.dot(p_vector) / segment_vector.norm_square()
        
        if t <= 0:
            return p.distance(self.p1)
        elif t >= 1:
            return p.distance(self.p2)
        else:
            return line_dist
    
    def intersects(self, other):
        """Check if this segment intersects with another segment."""
        # Check using the method of cross products
        def ccw(a, b, c):
            return (c.y - a.y) * (b.x - a.x) > (b.y - a.y) * (c.x - a.x)
        
        return (ccw(self.p1, other.p1, other.p2) != ccw(self.p2, other.p1, other.p2) and
                ccw(self.p1, self.p2, other.p1) != ccw(self.p1, self.p2, other.p2))
    
    def intersection_point(self, other):
        """Find the intersection point with another segment, if it exists."""
        if not self.intersects(other):
            return None
        
        # Convert to lines and find intersection
        line1 = self.as_line()
        line2 = other.as_line()
        intersection = line1.intersection(line2)
        
        # Check if the intersection point is on both segments
        if (intersection and 
            self.point_on_segment(intersection) and 
            other.point_on_segment(intersection)):
            return intersection
        
        return None
    
    def __str__(self):
        return f"Segment({self.p1}, {self.p2})"


class Polygon:
    """A polygon in 2D space, represented by its vertices in counter-clockwise order."""
    def __init__(self, vertices):
        self.vertices = vertices
    
    def area(self):
        """Calculate the area of the polygon using the shoelace formula."""
        n = len(self.vertices)
        result = 0
        for i in range(n):
            j = (i + 1) % n
            result += self.vertices[i].x * self.vertices[j].y
            result -= self.vertices[i].y * self.vertices[j].x
        return abs(result) / 2
    
    def perimeter(self):
        """Calculate the perimeter of the polygon."""
        n = len(self.vertices)
        result = 0
        for i in range(n):
            j = (i + 1) % n
            result += self.vertices[i].distance(self.vertices[j])
        return result
    
    def is_convex(self):
        """Check if the polygon is convex."""
        n = len(self.vertices)
        if n < 3:
            return False
        
        sign = 0
        for i in range(n):
            j = (i + 1) % n
            k = (i + 2) % n
            cross = (self.vertices[j] - self.vertices[i]).cross(self.vertices[k] - self.vertices[j])
            if i == 0:
                sign = 1 if cross > 0 else -1 if cross < 0 else 0
            elif (cross > 0 and sign < 0) or (cross < 0 and sign > 0):
                return False
        
        return True
    
    def contains_point(self, p, strict=True):
        """
        Check if the polygon contains a point (ray casting algorithm).
        If strict is True, points on the boundary are considered outside.
        """
        n = len(self.vertices)
        inside = False
        
        for i in range(n):
            j = (i + 1) % n
            segment = Segment(self.vertices[i], self.vertices[j])
            
            # Check if the point is on the boundary
            if segment.point_on_segment(p):
                return not strict
            
            # Ray casting algorithm
            if ((self.vertices[i].y > p.y) != (self.vertices[j].y > p.y) and
                p.x < (self.vertices[j].x - self.vertices[i].x) * 
                (p.y - self.vertices[i].y) / (self.vertices[j].y - self.vertices[i].y) + 
                self.vertices[i].x):
                inside = not inside
        
        return inside
    
    def __str__(self):
        return f"Polygon({', '.join(str(v) for v in self.vertices)})"


# Geometric utility functions

def orientation(p, q, r):
    """
    Returns the orientation of the triplet (p, q, r).
    0 --> Collinear
    1 --> Clockwise
    2 --> Counterclockwise
    """
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if abs(val) < 1e-9:
        return 0  # Collinear
    return 1 if val > 0 else 2  # CW or CCW

def convex_hull(points):
    """
    Compute the convex hull of a set of points using the Graham scan algorithm.
    Returns the vertices of the convex hull in counter-clockwise order.
    """
    n = len(points)
    if n <= 2:
        return points
    
    # Find the point with the lowest y-coordinate (and leftmost if tied)
    p0 = min(points, key=lambda p: (p.y, p.x))
    
    # Sort points by polar angle with respect to p0
    def polar_angle(p):
        return atan2(p.y - p0.y, p.x - p0.x)
    
    # Remove duplicates and sort
    sorted_points = sorted(set(points), key=polar_angle)
    
    # Build the convex hull
    hull = [p0, sorted_points[0]]
    for i in range(1, len(sorted_points)):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], sorted_points[i]) != 2:
            hull.pop()
        hull.append(sorted_points[i])
    
    return hull

def point_to_line_distance(p, line):
    """Calculate the distance from a point to a line."""
    return line.distance_to_point(p)

def min_distance_between_segments(seg1, seg2):
    """Calculate the minimum distance between two line segments."""
    # Check if the segments intersect
    if seg1.intersects(seg2):
        return 0
    
    # Calculate distances from endpoints to the other segment
    dist1 = seg2.distance_to_point(seg1.p1)
    dist2 = seg2.distance_to_point(seg1.p2)
    dist3 = seg1.distance_to_point(seg2.p1)
    dist4 = seg1.distance_to_point(seg2.p2)
    
    return min(dist1, dist2, dist3, dist4)

def is_point_on_line(p, line):
    """Check if a point lies on a line."""
    return abs(line.a * p.x + line.b * p.y + line.c) < 1e-9

def is_point_on_ray(p, origin, direction):
    """
    Check if a point lies on a ray.
    origin: start point of the ray
    direction: direction vector of the ray
    """
    # Check if the point is on the line
    vec = p - origin
    cross_prod = vec.cross(direction)
    if abs(cross_prod) > 1e-9:
        return False
    
    # Check if the point is in the right direction
    dot_prod = vec.dot(direction)
    return dot_prod >= 0

def angle_between_vectors(v1, v2):
    """Calculate the angle between two vectors in radians."""
    dot = v1.dot(v2)
    cross = v1.cross(v2)
    angle = atan2(abs(cross), dot)
    return angle

def is_polygon_simple(vertices):
    """Check if a polygon is simple (non-self-intersecting)."""
    n = len(vertices)
    if n < 3:
        return False
    
    for i in range(n):
        seg1 = Segment(vertices[i], vertices[(i + 1) % n])
        for j in range(i + 2, n):
            # Skip adjacent edges
            if j % n == (i - 1) % n or j % n == (i + 1) % n:
                continue
            seg2 = Segment(vertices[j], vertices[(j + 1) % n])
            if seg1.intersects(seg2):
                return False
    
    return True

def are_collinear(p1, p2, p3, epsilon=1e-9):
    """Check if three points are collinear."""
    return abs((p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)) < epsilon

def min_distance_between_point_and_segment(p, seg):
    """Calculate the minimum distance between a point and a line segment."""
    return seg.distance_to_point(p)

def are_points_on_same_side_of_line(p1, p2, line):
    """Check if two points are on the same side of a line."""
    val1 = line.a * p1.x + line.b * p1.y + line.c
    val2 = line.a * p2.x + line.b * p2.y + line.c
    return val1 * val2 > 0

def unique_slopes(points, origin):
    """Count unique slopes of lines passing through the origin point and each point in the list."""
    slopes = set()
    for p in points:
        if p.x == origin.x and p.y == origin.y:
            continue  # Skip the origin itself

        # Calculate direction vector and simplify it
        dx, dy = p.x - origin.x, p.y - origin.y

        # Special handling for zero components
        if dx == 0:
            slopes.add((0, 1 if dy > 0 else -1))
        elif dy == 0:
            slopes.add((1 if dx > 0 else -1, 0))
        else:
            # Find the GCD to reduce the fraction
            g = abs(gcd(int(dx), int(dy)))
            # Normalize direction: make sure first component is positive
            if dx < 0:
                dx, dy = -dx, -dy
            slopes.add((dx // g, dy // g))

    return len(slopes)


def count_unique_lines(points):
    """Count unique lines determined by pairs of points.
    Returns a dictionary mapping direction vectors to sets of lines (by their intercepts).
    """
    lines = defaultdict(set)
    for (p1, p2) in combinations(points, 2):
        if p1.x == p2.x:  # Vertical line
            direction = (0, 1)
            intercept = p1.x
        else:
            # Calculate slope and intercept for non-vertical line
            dy = p2.y - p1.y
            dx = p2.x - p1.x
            g = abs(gcd(int(dy), int(dx)))
            # Normalize the direction vector
            dy, dx = dy // g, dx // g
            if dx < 0 or (dx == 0 and dy < 0):
                dy, dx = -dy, -dx
            direction = (dx, dy)

            # Calculate the intercept
            # For line equation: dy·x - dx·y + C = 0
            intercept = dy * p1.x - dx * p1.y

        lines[direction].add(intercept)

    return lines


def count_line_intersections(lines):
    """Count the number of intersections between lines represented by the given groups.
    The lines parameter should be a dictionary mapping direction vectors to sets of line intercepts.
    """
    result = 0
    directions = list(lines.keys())

    # Count intersections between lines with different slopes
    for i in range(len(directions) - 1):
        for j in range(i + 1, len(directions)):
            # Lines with different slopes always intersect unless they're parallel
            result += len(lines[directions[i]]) * len(lines[directions[j]])

    return result

# Input/output utility functions

def read_points(n, input_func=input):
    """Read n points from input."""
    points = []
    for _ in range(n):
        x, y = map(float, input_func().split())
        points.append(Point(x, y))
    return points

def read_int_points(n, input_func=input):
    """Read n points with integer coordinates from input."""
    points = []
    for _ in range(n):
        x, y = map(int, input_func().split())
        points.append(Point(x, y))
    return points


def get_quadrant(p, origin):
    """Get the quadrant of point p relative to origin.
    Returns: One of ('NE', 'NW', 'SE', 'SW') for the four quadrants,
             or ('N', 'E', 'S', 'W') for points directly on an axis."""
    dx = p.x - origin.x
    dy = p.y - origin.y

    if dx > 0 and dy > 0:
        return 'NE'
    elif dx < 0 and dy > 0:
        return 'NW'
    elif dx < 0 and dy < 0:
        return 'SW'
    elif dx > 0 and dy < 0:
        return 'SE'
    elif dx == 0 and dy > 0:
        return 'N'
    elif dx > 0 and dy == 0:
        return 'E'
    elif dx == 0 and dy < 0:
        return 'S'
    elif dx < 0 and dy == 0:
        return 'W'
    else:  # Same point
        return 'SAME'


def is_rectangle(points):
    """Check if 4 points form a rectangle (right angles but sides may have different lengths)."""
    if len(points) != 4:
        return False

    # Sort points to help identify corners
    points = sorted(points, key=lambda p: (p.x, p.y))

    # Calculate side lengths and diagonals
    sides = [
        points[0].distance(points[1]),
        points[0].distance(points[2]),
        points[1].distance(points[3]),
        points[2].distance(points[3])
    ]

    diagonals = [
        points[0].distance(points[3]),
        points[1].distance(points[2])
    ]

    # For a rectangle: opposite sides are equal and diagonals are equal
    return (abs(sides[0] - sides[3]) < 1e-9 and
            abs(sides[1] - sides[2]) < 1e-9 and
            abs(diagonals[0] - diagonals[1]) < 1e-9)


def is_square(points):
    """Check if 4 points form a square (right angles and equal sides)."""
    if len(points) != 4:
        return False

    # Sort points to help identify corners
    points = sorted(points, key=lambda p: (p.x, p.y))

    # Calculate side lengths and diagonals
    sides = [
        points[0].distance(points[1]),
        points[0].distance(points[2]),
        points[1].distance(points[3]),
        points[2].distance(points[3])
    ]

    diagonals = [
        points[0].distance(points[3]),
        points[1].distance(points[2])
    ]

    # For a square: all sides are equal and diagonals are equal
    return (abs(sides[0] - sides[1]) < 1e-9 and
            abs(sides[1] - sides[2]) < 1e-9 and
            abs(sides[2] - sides[3]) < 1e-9 and
            abs(diagonals[0] - diagonals[1]) < 1e-9)


def find_fourth_parallelogram_vertex(p1, p2, p3):
    """Given three vertices of a parallelogram, find the fourth vertex.
    Returns all possible fourth vertices (there's only one for a parallelogram)."""
    return [
        Point(p1.x + p2.x - p3.x, p1.y + p2.y - p3.y),
        Point(p1.x + p3.x - p2.x, p1.y + p3.y - p2.y),
        Point(p2.x + p3.x - p1.x, p2.y + p3.y - p1.y)
    ]


def can_fit_on_two_lines(points):
    """Check if all points can be placed on at most 2 lines."""
    n = len(points)
    if n <= 4:  # 4 or fewer points can always be placed on 2 lines
        return True

    # Try each pair of points to define the first line
    for i in range(n):
        for j in range(i+1, n):
            # First line defined by points[i] and points[j]
            line1_points = [i, j]
            other_points = []

            # Check which other points are on this line
            for k in range(n):
                if k != i and k != j:
                    if are_collinear(points[i], points[j], points[k]):
                        line1_points.append(k)
                    else:
                        other_points.append(k)

            # If all other points are collinear, or if there are no other points,
            # then all points can be placed on at most 2 lines
            if len(other_points) <= 2:
                return True

            # Check if remaining points are collinear
            is_collinear = True
            if len(other_points) >= 3:
                p1, p2 = other_points[0], other_points[1]
                for k in range(2, len(other_points)):
                    if not are_collinear(points[p1], points[p2], points[other_points[k]]):
                        is_collinear = False
                        break

            if is_collinear:
                return True

    return False