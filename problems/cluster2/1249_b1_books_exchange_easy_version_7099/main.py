#!/usr/bin/env python3

import sys
sys.path.append('/home/justinchiu_cohere_com/codecontests-repo/problems/cluster2')
from library import DSU, read_int, read_ints

def solve_test():
    n = read_int()
    p = read_ints()
    
    dsu = DSU(n)
    for i, book in enumerate(p):
        dsu.union(i, book - 1)
    
    return [dsu.get_size(i) for i in range(n)]

t = read_int()
for _ in range(t):
    print(*solve_test())