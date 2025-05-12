#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_int, read_array, setup_io
from collections import deque

input = setup_io()

n = read_int()
l = read_array()
visited = set()
graph = {i: set() for i in range(1, n+1)}
d = {}
papa = [0 for i in range(n+1)]
level = [[] for i in range(n+1)]
z = [[0] for i in range(n+1)]

for i in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
    d[(a, b)] = c

stack = deque()
# Find leaf nodes
for i in graph:
    if len(graph[i]) == 1:
        stack.append([i, 0])

m = 0
while stack:
    x, y = stack.popleft()
    if len(graph[x]) >= 1:
        for i in graph[x]:
            t = i
            break
        if (t, x) in d:
            q = d[(t, x)]
        else:
            q = d[(x, t)]
        z[t].append(y + l[x-1] - q)
        graph[t].remove(x)
        if len(graph[t]) == 1:
            stack.append([t, max(z[t])])

for i in range(1, n+1):
    z[i].sort()
    if len(z[i]) >= 3:
        m = max(m, l[i-1] + z[i][-2] + z[i][-1])
    m = max(m, z[i][-1] + l[i-1])

print(m)