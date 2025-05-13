#!/usr/bin/env python3

from library import read_int, read_points, supercentral_point

n = read_int()
points = read_points(n)
print(supercentral_point(points))