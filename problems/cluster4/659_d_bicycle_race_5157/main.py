#!/usr/bin/env python3

from library import Point

# Read input
n = int(input())
points = []

for _ in range(n + 1):
    x, y = map(int, input().split())
    points.append(Point(x, y))

# Count dangerous turns
dangerous_count = 0

for i in range(2, n):
    # Calculate vectors between consecutive points
    v1 = points[i] - points[i-1]
    v2 = points[i-1] - points[i-2]
    
    # Calculate the cross product of vectors
    # A negative cross product means a right turn
    # In this problem, right turns are dangerous (outward turns)
    if v1.cross(v2) < 0:
        dangerous_count += 1

print(dangerous_count)