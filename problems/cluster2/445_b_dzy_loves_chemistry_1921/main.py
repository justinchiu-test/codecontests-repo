#!/usr/bin/env python3

from library import DSU

nodes, edges = map(int, input().split())
dsu = DSU(nodes)

for _ in range(edges):
    a, b = map(int, input().split())
    dsu.union(a-1, b-1)

# Power of 2 for each edge in connected components
# For each component, we need n-1 edges for n nodes
# So the answer is 2^(nodes - number of components)
print(2**(nodes - dsu.count_sets()))