#!/usr/bin/env python3

n=int(input())
d={}
for i in range(n):
    a,b=map(int,input().split())
    if a in d:
        d[a].append(b)
    else:
        d[a]=[b]
    if b in d:
        d[b].append(a)
    else:
        d[b]=[a]
ans=[]
for el in d:
    if len(d[el])==1:
        ans.append(el)
        root=el
        break
cur=root
while True:
    for el in d[cur]:
        if el==ans[-1]:continue
        if cur!=root:ans.append(cur)
        cur=el
        break
    if len(d[cur])==1:
        ans.append(cur)
        break
print(*ans)
