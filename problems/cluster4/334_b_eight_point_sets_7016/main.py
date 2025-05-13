#!/usr/bin/env python3

from library import read_point

# Read the 8 points
points = [read_point() for _ in range(8)]

# Sort points by x-coordinate first, then by y-coordinate
points.sort()

# For a respectable set, we need 3 distinct x-coordinates and 3 distinct y-coordinates
# with the middle point (x2, y2) missing
x_values = set()
y_values = set()

for x, y in points:
    x_values.add(x)
    y_values.add(y)

# We must have exactly 3 distinct values for both x and y
if len(x_values) != 3 or len(y_values) != 3:
    print("ugly")
    exit()

# Sort the x and y values
x_values = sorted(list(x_values))
y_values = sorted(list(y_values))

# Check that we have all valid points except (x2, y2)
expected_points = set()
for x in x_values:
    for y in y_values:
        if x != x_values[1] or y != y_values[1]:  # Skip middle point (x2, y2)
            expected_points.add((x, y))

# Convert points to a set for comparison
actual_points = set(points)

# Check if the sets match
if expected_points == actual_points:
    print("respectable")
else:
    print("ugly")