#!/usr/bin/env python3

from library import input, mi

n, m = mi()
non=[{i} for i in range(n)]
for _ in range(m):
    u, v = mi()
    u -= 1; v -= 1
    non[u].add(v)
    non[v].add(u)
vertex=set(range(n))
ans=[]
while(vertex):
    a=next(iter(vertex))
    vertex.remove(a)
    stk=[a]
    cou=1
    while(stk):
        v=stk.pop()
        s=vertex-non[v]
        cou+=len(s)
        stk.extend(s)
        vertex&=non[v]
    ans.append(cou)
ans.sort()
print(len(ans))
print(" ".join(map(str,ans)))
