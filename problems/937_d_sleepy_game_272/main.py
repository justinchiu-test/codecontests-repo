#!/usr/bin/env python3

n,m = map(int, input().split())
g = [[] for i in range(n)]
fs = set()
for i in range(n):
    a = list(map(int , input().split()))
    c = a[0]
    if c == 0:
        fs.add(i)
        continue
    for j in range(1,c+1):
        g[i].append(a[j]-1)

s = int(input())-1
prev0 = [None for i in range(n)]
prev1=[None for i in range(n)]
vis0 = [0 for i in range(n)]
vis0[s]=1
vis1 = [0 for i in range(n)]
q = [(s, 0)]
ans = None
draw = False
while len(q) > 0:
    v, c = q[0]
    del q[0]
    for u in g[v]:
        if c == 0:
            if vis1[u] == 0:
                vis1[u] =1
                q.append((u, 1))
                prev1[u] =v
            if u in fs:
                    ans = u
                    break
        elif c == 1:
            if vis0[u] == 0:
                vis0[u] =1
                q.append((u, 0))
                prev0[u] =v
    if ans is not None:
        break

if ans is None:
    q = [s]
    vis=[0 for i in range(n)]
    vis[s]=1
    nxt = [0 for i in range(n)]
    while len(q) > 0:
        v = q[-1]
        if nxt[v] < len(g[v]):
            u = g[v][nxt[v]]
            if vis[u] == 1:
                print('Draw')
                exit()
            elif vis[u] == 0:
                vis[u]=1
                q.append(u)
            nxt[v] +=1
        else:
            vis[v] = 2
            del q[-1]

    print('Lose')
    exit()
arn = []
nxt = ans
while nxt is not None:
    arn.append(nxt)
    if len(arn) % 2 == 1:
        nxt = prev1[nxt]
    else:
        nxt = prev0[nxt]
print('Win')
arn = list(reversed(arn))
print(' '.join([str(i+1) for i in arn]))
