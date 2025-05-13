#!/usr/bin/env python3

from library import Point, read_int_points

n = int(input())
points = read_int_points(n)

# Find supercentral points (points with at least one neighbor in each direction)
supercentral_count = 0

for i in range(n):
    # Initialize flags for each direction
    has_right = has_left = has_upper = has_lower = False
    
    # Check all other points
    for j in range(n):
        if i == j:
            continue
        
        # Check if the point is a neighbor in one of the four directions
        if points[j].x > points[i].x and points[j].y == points[i].y:
            has_right = True
        elif points[j].x < points[i].x and points[j].y == points[i].y:
            has_left = True
        elif points[j].x == points[i].x and points[j].y > points[i].y:
            has_upper = True
        elif points[j].x == points[i].x and points[j].y < points[i].y:
            has_lower = True
    
    # If the point has neighbors in all four directions, it's supercentral
    if has_right and has_left and has_upper and has_lower:
        supercentral_count += 1

print(supercentral_count)