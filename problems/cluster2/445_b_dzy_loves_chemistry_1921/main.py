#!/usr/bin/env python3

from library import get_ints, DSU

n, m = get_ints()
dsu = DSU(n)

for _ in range(m):
    a, b = get_ints()
    dsu.union(a-1, b-1)

# The answer is 2^(n - number of connected components)
print(2**(n - dsu.count_components()))