#!/usr/bin/env python3

from heapq import heappush, heappop
n,m = map(int,input().split())

adj = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    adj[a].append(b)
    adj[b].append(a)

st = set()
hp = []
v = [False for _ in range(n)]
heappush(hp,0)
v[0] = True
ans = []

while hp:
    x = heappop(hp)
    ans += [x]
    for i in adj[x]:
        if v[i]:
            continue
        v[i] = True
        heappush(hp,i)

print(*[i+1 for i in ans])
