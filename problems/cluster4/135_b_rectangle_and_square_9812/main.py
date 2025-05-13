#!/usr/bin/env python3

from itertools import combinations
from library import Point, is_square, is_rectangle

# Read the 8 points
points = []
for i in range(8):
    x, y = map(int, input().split())
    points.append(Point(x, y))

found = False

# Try all possible ways to split the 8 points into two groups of 4
for square_indices in combinations(range(8), 4):
    # The indices of the rectangle are the complement of the square indices
    rect_indices = [i for i in range(8) if i not in square_indices]
    
    # Extract the square and rectangle points
    square_points = [points[i] for i in square_indices]
    rect_points = [points[i] for i in rect_indices]
    
    # Check if the first set forms a square and the second forms a rectangle
    if is_square(square_points) and is_rectangle(rect_points):
        found = True
        # Convert to 1-based indexing for output
        square_indices = [i + 1 for i in square_indices]
        rect_indices = [i + 1 for i in rect_indices]
        break
    
    # Also check if the first set forms a rectangle and the second forms a square
    if is_rectangle(square_points) and is_square(rect_points):
        found = True
        # Swap the indices to match the problem requirements
        rect_indices, square_indices = square_indices, rect_indices
        # Convert to 1-based indexing for output
        square_indices = [i + 1 for i in square_indices]
        rect_indices = [i + 1 for i in rect_indices]
        break

if found:
    print("YES")
    print(*square_indices)
    print(*rect_indices)
else:
    print("NO")