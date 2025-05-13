#!/usr/bin/env python3

from library import read_int, read_point, orientation

n = read_int()
points = [read_point() for _ in range(n)]

def are_collinear(p1, p2, p3):
    """Check if three points are collinear."""
    # Using the cross product method from the library's orientation function
    return orientation(p1, p2, p3) == 0

def check_two_lines():
    """Check if points can be covered by two lines."""
    # Base case for n ≤ 4
    if n <= 4:
        return True
    
    # Try using the first two points to define a line
    s1 = [0, 1]  # Indices of points on first line
    s2 = []      # Indices of points on second line
    
    # Check the rest of the points
    for i in range(2, n):
        if are_collinear(points[0], points[1], points[i]):
            s1.append(i)
        else:
            s2.append(i)
    
    # If s2 has 0 or 1 points, we can fit all points on two lines
    if len(s2) <= 1:
        return True
    
    # Now check if all points in s2 are collinear
    for i in range(2, len(s2)):
        if not are_collinear(points[s2[0]], points[s2[1]], points[s2[i]]):
            return False
    
    return True

def check_using_different_lines():
    """Try different pairs of initial points to define the lines."""
    # Try with original ordering
    if check_two_lines():
        return True
    
    # If n ≤ 4, we already handled this case
    if n <= 4:
        return False
    
    # Try using points 0 and 2 to define the first line
    points[1], points[2] = points[2], points[1]
    if check_two_lines():
        return True
    
    # Try using points 2 and 1 to define the first line
    points[0], points[2] = points[2], points[0]
    if check_two_lines():
        return True
    
    return False

if check_using_different_lines():
    print("YES")
else:
    print("NO")