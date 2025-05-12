#!/usr/bin/env python3

import sys
sys.path.append('/home/justinchiu_cohere_com/codecontests-repo/problems/cluster2')
from library import DSU, read_ints

n, m = read_ints()
dsu = DSU(n)

for _ in range(m):
    a, b = read_ints()
    dsu.union(a-1, b-1)

# The answer is 2^(n - number of connected components)
print(2**(n - dsu.get_components_count()))