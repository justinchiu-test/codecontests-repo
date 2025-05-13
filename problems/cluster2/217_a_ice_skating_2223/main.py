#!/usr/bin/env python3

from library import DSU

n = int(input().strip())
coords = []

for _ in range(n):
    x, y = map(int, input().strip().split())
    coords.append((x, y))

# Use DSU to track connected components
dsu = DSU(n)

for i in range(n):
    for j in range(i + 1, n):
        # If two points share an x or y coordinate, they are connected
        if coords[i][0] == coords[j][0] or coords[i][1] == coords[j][1]:
            dsu.union(i, j)

# Count connected components, each additional component beyond 
# the first requires one extra line to connect
print(dsu.num_components() - 1)