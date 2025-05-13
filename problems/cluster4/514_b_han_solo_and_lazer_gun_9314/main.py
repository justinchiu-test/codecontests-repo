#!/usr/bin/env python3

from library import Point, unique_slopes

n, x0, y0 = map(int, input().split())
origin = Point(x0, y0)
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))

# Count unique slopes of lines from the gun to each stormtrooper
result = unique_slopes(points, origin)
print(result)