#!/usr/bin/env python3

from library import read_point, parallelogram_fourth_points

# Read input points
x1, y1 = read_point()
x2, y2 = read_point()
x3, y3 = read_point()

# Calculate possible fourth points
result = parallelogram_fourth_points(x1, y1, x2, y2, x3, y3)

# Output results
print(len(result))
for x, y in result:
    print(x, y)