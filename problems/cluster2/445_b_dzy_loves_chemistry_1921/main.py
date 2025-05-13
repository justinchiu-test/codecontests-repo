#!/usr/bin/env python3

from library import DSU

n, m = map(int, input().split())

# If there are no chemicals or no reactions, the danger is 1
if n == 0 or m == 0:
    print(1)
    exit()

# Use DSU to find connected components
dsu = DSU(n)

for _ in range(m):
    a, b = map(int, input().split())
    dsu.union(a - 1, b - 1)  # Convert to 0-indexed

# For each component with k nodes, we can get 2^(k-1) danger
# This is because each time we add a chemical that can react
# with something already in the tube, the danger doubles.
# For a component of size k, we can double the danger k-1 times.
result = 1
components = {}

for i in range(n):
    root = dsu.find(i)
    components[root] = True

# The answer is 2^(edges in a spanning forest)
# In a connected component with k nodes, a spanning tree has k-1 edges
# So the total edges in a spanning forest is n - (number of components)
print(2 ** (n - len(components)))