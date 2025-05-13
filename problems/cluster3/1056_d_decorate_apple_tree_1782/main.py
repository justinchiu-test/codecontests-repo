#!/usr/bin/env python3

from library import read_int, read_ints

n = read_int()
d = [0] * (n + 1)  # Colors needed for each junction

if n > 1:
    p = [0, 0] + read_ints()  # Parent array
    
    # Process from leaves to root
    for i in range(n, 1, -1):
        if d[i] == 0:  # If not visited, it's a leaf
            d[i] = 1
        d[p[i]] += d[i]  # Parent needs as many colors as its children

if n == 1:  # Special case for a single node
    d[1] = 1

d = d[1:]  # Remove the unused vertex 0
d.sort()  # Sort to get the minimum colors for k happy junctions
print(*d)