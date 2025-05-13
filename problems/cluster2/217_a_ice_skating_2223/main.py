#!/usr/bin/env python3

from library import get_int, DSU

n = get_int()
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

dsu = DSU(n)
for i in range(n):
    for j in range(i+1, n):
        if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
            dsu.union(i, j)

print(dsu.count_components() - 1)