#!/usr/bin/env python3

from itertools import combinations, permutations
from library import Point, is_square, is_rectangle

# Read the 8 points (1-based indexing in the original code)
points = [None]  # Add a placeholder at index 0
for _ in range(8):
    x, y = map(int, input().split())
    points.append(Point(x, y))

# Try all possible ways to split the 8 points into two groups of 4
for square_indices in combinations(range(1, 9), 4):
    # The indices of the rectangle are the complement of the square indices
    rect_indices = [i for i in range(1, 9) if i not in square_indices]
    
    # Extract the square and rectangle points
    square_points = [points[i] for i in square_indices]
    rect_points = [points[i] for i in rect_indices]
    
    # Check if the first set forms a square and the second forms a rectangle
    if is_square(square_points) and is_rectangle(rect_points):
        print("YES")
        print(*square_indices)
        print(*rect_indices)
        exit(0)
    
    # Check if the first set forms a rectangle and the second forms a square
    if is_rectangle(square_points) and is_square(rect_points):
        print("YES")
        print(*rect_indices)
        print(*square_indices)
        exit(0)

print("NO")