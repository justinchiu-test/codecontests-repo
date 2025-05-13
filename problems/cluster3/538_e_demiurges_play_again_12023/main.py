#!/usr/bin/env python3

from library import setup_io
from collections import deque

# Set up fast I/O
input = setup_io()

def solve():
    n = int(input())
    g = [[] for _ in range(n+1)]

    # Build adjacency list
    for _ in range(n-1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    # Calculate depths using BFS
    q = [1]
    d = [None] * (n+1)
    d[1] = 0
    i = 0

    # BFS to compute depth and remove parent edges
    while i < len(q):
        x = q[i]
        i += 1
        for v in list(g[x]):  # Use list to avoid modification during iteration
            if d[v] is None:
                q.append(v)
                d[v] = d[x] + 1
                g[v].remove(x)  # Remove parent edge

    # DP for min and max
    m = [0] * (n+1)  # min
    M = [0] * (n+1)  # max
    cnt = 0  # Count of leaf nodes

    # Process nodes in reverse order (bottom-up)
    for i in range(len(q)-1, -1, -1):
        x = q[i]
        if len(g[x]) == 0:  # Leaf node
            m[x] = 1
            M[x] = 1
            cnt += 1
        elif d[x] % 2 == 0:  # Max player (even depth)
            c = 0
            C = float('inf')
            for v in g[x]:
                c += m[v]  # Sum of min values
            for v in g[x]:
                C = min(C, M[v])  # Min of max values
            m[x] = c
            M[x] = C if C < float('inf') else 0
        else:  # Min player (odd depth)
            c = float('inf')
            C = 0
            for v in g[x]:
                c = min(c, m[v])  # Min of min values
            for v in g[x]:
                C += M[v]  # Sum of max values
            m[x] = c if c < float('inf') else 0
            M[x] = C

    # Adjust max value according to problem requirements
    print(cnt + 1 - M[1], m[1])

solve()
