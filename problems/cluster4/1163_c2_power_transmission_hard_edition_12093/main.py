#!/usr/bin/env python3

from library import Point, count_unique_lines, count_line_intersections

n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))

# Find all unique lines and count their intersections
lines = count_unique_lines(points)
result = count_line_intersections(lines)

print(result)