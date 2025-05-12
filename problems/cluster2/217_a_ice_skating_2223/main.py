#!/usr/bin/env python3

import sys
sys.path.append('/home/justinchiu_cohere_com/codecontests-repo/problems/cluster2')
from library import DSU, read_int, read_ints

n = read_int()
points = []
for _ in range(n):
    x, y = read_ints()
    points.append((x, y))

# We connect points that share x or y coordinates
dsu = DSU(n)
for i in range(n):
    for j in range(i+1, n):
        if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
            dsu.union(i, j)

# The answer is the number of components - 1
print(dsu.get_components_count() - 1)