#!/usr/bin/env python3

from library import Point, are_collinear
from collections import defaultdict
from math import gcd

n = int(input())

# Read all points
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))

# If we have fewer than 3 points, there are no triangles
if n < 3:
    print(0)
    exit()

# To count triangles with non-zero area, for each point, we'll count
# how many points lie on each line passing through that point
total_triangles = 0

for i, center in enumerate(points):
    # Store the direction vectors from center to each other point
    direction_vectors = defaultdict(int)
    
    for j, p in enumerate(points):
        if i == j:  # Skip the same point
            continue
        
        # Calculate direction vector from center to point p
        dx = p.x - center.x
        dy = p.y - center.y
        
        # Normalize the direction vector
        if dx < 0 or (dx == 0 and dy < 0):
            dx, dy = -dx, -dy
        
        # Reduce to smallest integer form
        g = abs(gcd(int(dx), int(dy)))
        dx, dy = dx // g, dy // g
        
        # Count points in this direction
        direction_vectors[(dx, dy)] += 1
    
    # For each direction, calculate the number of triangles
    # that can be formed with points not in that direction
    collinear_triples = 0
    for direction, count in direction_vectors.items():
        # For each point in this direction, we can form triangles with any
        # other point not in this direction
        collinear_triples += count * (n - 1 - count)
    
    # Each triangle is counted 2 times in the above calculation
    total_triangles += collinear_triples // 2

# Each triangle is counted 3 times (once from each vertex)
print(total_triangles // 3)