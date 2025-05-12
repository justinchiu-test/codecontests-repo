#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_int, read_ints

n = read_int()
r = [[] for i in range(n + 1)]
r[1] = [0]
for i in range(n - 1):
    a, b = map(int, input().split())
    r[a].append(b)
    r[b].append(a)
t = read_ints()
u, v = [0] * (n + 1), [0] * (n + 1)
for i, j in enumerate(t, 1):
    if j < 0: u[i] = - j
    else: v[i] = j

# BFS to get parent pointers
t, p = [1], [0] * (n + 1)
while t:
    a = t.pop()
    for b in r[a]:
        if p[b]: continue
        p[b] = a
        t.append(b)

# Count degrees
k = [len(t) for t in r]

# Start with leaves
t = [a for a in range(2, n + 1) if k[a] == 1]
x, y = [0] * (n + 1), [0] * (n + 1)

# Process tree bottom-up
while t:
    a = t.pop()
    b = p[a]
    x[b] = max(x[b], u[a])
    y[b] = max(y[b], v[a])
    k[b] -= 1
    if k[b] == 1:
        t.append(b)
        if u[b] > 0:
            if x[b] - y[b] > u[b]:
                u[b], v[b] = x[b], x[b] - u[b]
            else: u[b], v[b] = y[b] + u[b], y[b]
        else:
            if y[b] - x[b] > v[b]:
                u[b], v[b] = y[b] - v[b], y[b]
            else: u[b], v[b] = x[b], x[b] + v[b]

print(u[1] + v[1])