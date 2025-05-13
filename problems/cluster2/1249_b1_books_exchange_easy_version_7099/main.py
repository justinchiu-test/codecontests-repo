#!/usr/bin/env python3

from library import DSU

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    # Create a DSU to find cycles
    dsu = DSU(n)
    
    # Connect each index to its destination
    for i, x in enumerate(p):
        dsu.union(i, x - 1)  # Convert to 0-indexed
    
    # Size of the component is the number of days required
    return [dsu.size_of(i) for i in range(n)]

t = int(input())
for _ in range(t):
    print(*solve())