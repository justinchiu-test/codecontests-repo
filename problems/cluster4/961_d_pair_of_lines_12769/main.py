#!/usr/bin/env python3

from library import Point, are_collinear, can_fit_on_two_lines

n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))

# Special cases
if n <= 4:  # All points can be placed on at most 2 lines
    print("YES")
    exit()

# Check if all points can be placed on at most 2 lines
if can_fit_on_two_lines(points):
    print("YES")
else:
    print("NO")