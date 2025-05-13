#!/usr/bin/env python3

from library import Point, read_int_points

# Read 8 points from input
points = []
for _ in range(8):
    x, y = map(int, input().split())
    points.append(Point(x, y))

# Sort points by x coordinate, then by y coordinate
points.sort(key=lambda p: (p.x, p.y))

# For a respectable set, we need to have:
# 1. Exactly 3 distinct x-coordinates
# 2. Exactly 3 distinct y-coordinates
# 3. A specific grid pattern (x1,y1), (x1,y2), (x1,y3), (x2,y1), (x2,y2), (x2,y3), (x3,y1), (x3,y2), (x3,y3)
# with one point missing to make it 8 points in total

# Extract distinct x and y coordinates
x_coords = sorted(set(p.x for p in points))
y_coords = sorted(set(p.y for p in points))

# Check if we have exactly 3 distinct x-coordinates and 3 distinct y-coordinates
if len(x_coords) != 3 or len(y_coords) != 3:
    print("ugly")
    exit()

# Define the expected grid pattern (all 9 possible points)
grid_points = set()
for x in x_coords:
    for y in y_coords:
        grid_points.add((x, y))

# Check which point is missing from the grid
actual_points = set((p.x, p.y) for p in points)
missing_points = grid_points - actual_points

# For a respectable set, exactly one point should be missing, 
# and it should be the middle point of the grid (x2, y2)
if len(missing_points) != 1:
    print("ugly")
    exit()

missing_x, missing_y = list(missing_points)[0]
if (missing_x != x_coords[1] or missing_y != y_coords[1]):
    print("ugly")
    exit()

print("respectable")