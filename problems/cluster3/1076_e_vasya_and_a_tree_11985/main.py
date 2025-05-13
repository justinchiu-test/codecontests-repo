#!/usr/bin/env python3

from library import enable_fast_io, bootstrap, read_int, read_int_tuple
from collections import defaultdict

enable_fast_io()

@bootstrap
def dfs(u, i, p):
    global d, s
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
adj = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = read_int_tuple()
    adj[u].append(v)
    adj[v].append(u)

val = [[] for _ in range(n+1)]
m = read_int()

for _ in range(m):
    v, d, va = read_int_tuple()
    val[v].append([d, va])

s = 0
d = defaultdict(lambda: 0)
ans = [0 for _ in range(n+1)]
dfs(1, 0, 0)
print(*ans[1:])