#!/usr/bin/env python3
from library import ii, mi

n = ii()
g = []  # [x, y, visited]
for _ in range(n):
    x, y = mi()
    g.append([x, y, False])

def visita(i):
    # DFS over points sharing row or column
    stack = [i]
    g[i][2] = True
    while stack:
        u = stack.pop()
        xu, yu, _ = g[u]
        for j in range(n):
            if not g[j][2] and (xu == g[j][0] or yu == g[j][1]):
                g[j][2] = True
                stack.append(j)

cnt = -1
for i in range(n):
    if g[i][2] == False:
        cnt += 1
        visita(i)

print(cnt)
