#!/usr/bin/env python3

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import bootstrap, setup_io, read_int
from collections import defaultdict

input = setup_io()
sys.setrecursionlimit(10**5)

@bootstrap
def dfs(u, i, p):
    global d
    global s
    s += -d[i-1]

    for j in val[u]:
        d[i+j[0]] += j[1]
        s += j[1]

    ans[u] = s
    for j in adj[u]:
        if j != p:
            yield dfs(j, i+1, u)
    for j in val[u]:
        d[i + j[0]] += -j[1]
        s += -j[1]
    s += d[i-1]

    yield

n = read_int()
adj = [[] for i in range(n+1)]
for j in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

val = [[] for i in range(n+1)]
m = read_int()
for j in range(m):
    v, d, va = map(int, input().split())
    val[v].append([d, va])

s = 0
d = defaultdict(lambda: 0)
ans = [0 for i in range(n+1)]
dfs(1, 0, 0)
print(*ans[1:])