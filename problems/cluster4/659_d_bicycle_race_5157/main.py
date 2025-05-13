#!/usr/bin/env python3

from library import read_int, read_point, Vector

# Read input
n = read_int()
points = [read_point() for _ in range(n+1)]  # n + 1 points forming n straight sections

dangerous_turns = 0

# Process each turn in the track (excluding the first and last points)
for i in range(2, n+1):
    # Create vectors for adjacent segments
    v1 = Vector(points[i][0] - points[i-1][0], points[i][1] - points[i-1][1])
    v2 = Vector(points[i-1][0] - points[i-2][0], points[i-1][1] - points[i-2][1])
    
    # Calculate the cross product to determine turn direction
    # If cross product < 0, it's a right turn, which is potentially dangerous
    cross_product = v1 % v2
    
    if cross_product < 0:
        dangerous_turns += 1

print(dangerous_turns)