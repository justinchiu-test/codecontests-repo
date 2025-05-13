#!/usr/bin/env python3

from library import read_ints, count_unique_directions

# Read input
n, x0, y0 = read_ints()
points = [read_ints() for _ in range(n)]

# Count unique directions (lines) from the gun to stormtroopers
print(count_unique_directions(x0, y0, points))