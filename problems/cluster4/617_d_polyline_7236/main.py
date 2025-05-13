#!/usr/bin/env python3

from library import Point

# Read the three points
points = []
for _ in range(3):
    x, y = map(int, input().split())
    points.append(Point(x, y))

a, b, c = points

# Check for aligned points
x_aligned = False  # If there are points with the same x-coordinate
y_aligned = False  # If there are points with the same y-coordinate

# Check which points share the same x or y coordinate
same_x_count = 0
if a.x == b.x:
    same_x_count += 1
if a.x == c.x:
    same_x_count += 1
if b.x == c.x:
    same_x_count += 1

same_y_count = 0
if a.y == b.y:
    same_y_count += 1
if a.y == c.y:
    same_y_count += 1
if b.y == c.y:
    same_y_count += 1

# Check if any point lies between two others (forms a straight line)
point_between = False

# For points with the same x-coordinate
if a.x == b.x:
    if c.x == a.x:  # All three points on the same vertical line
        x_aligned = True
    else:
        # Check if c's y-coordinate is between a's and b's
        if (c.y > min(a.y, b.y) and c.y < max(a.y, b.y)):
            point_between = True

if a.x == c.x:
    if b.x == a.x:  # Already checked above
        pass
    else:
        # Check if b's y-coordinate is between a's and c's
        if (b.y > min(a.y, c.y) and b.y < max(a.y, c.y)):
            point_between = True

if b.x == c.x:
    if a.x == b.x:  # Already checked above
        pass
    else:
        # Check if a's y-coordinate is between b's and c's
        if (a.y > min(b.y, c.y) and a.y < max(b.y, c.y)):
            point_between = True

# For points with the same y-coordinate
if a.y == b.y:
    if c.y == a.y:  # All three points on the same horizontal line
        y_aligned = True
    else:
        # Check if c's x-coordinate is between a's and b's
        if (c.x > min(a.x, b.x) and c.x < max(a.x, b.x)):
            point_between = True

if a.y == c.y:
    if b.y == a.y:  # Already checked above
        pass
    else:
        # Check if b's x-coordinate is between a's and c's
        if (b.x > min(a.x, c.x) and b.x < max(a.x, c.x)):
            point_between = True

if b.y == c.y:
    if a.y == b.y:  # Already checked above
        pass
    else:
        # Check if a's x-coordinate is between b's and c's
        if (a.x > min(b.x, c.x) and a.x < max(b.x, c.x)):
            point_between = True

# Determine the minimum number of segments needed
if same_x_count == 3:  # All points on one vertical line
    print(1)
elif same_y_count == 3:  # All points on one horizontal line
    print(1)
elif (same_x_count >= 1 or same_y_count >= 1) and not point_between:
    # Some points aligned, but not in a way that forces 3 segments
    print(2)
else:
    # Either no alignment or the points are aligned in a way that requires 3 segments
    print(3)