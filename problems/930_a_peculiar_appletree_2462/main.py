#!/usr/bin/env python3

from collections import  defaultdict,Counter,deque as dq
from sys import  stdin
input=stdin.readline

n=int(input())
g=defaultdict(list)
w=list(map(int,input().strip().split()))
for i in range(len(w)):
	g[w[i]-1].append(i+1)
	g[i+1].append(w[i]-1)
# print(g)
q=dq([0])
d=[-1]*(n)
d[0]=1
cnt=defaultdict(int)
cnt[1]+=1
while q:
	t=q.popleft()
	for i in g[t]:
		if d[i]==-1:
			d[i]=d[t]+1
			cnt[d[i]]+=1
			q.append(i)
ans=0
for i in cnt:
	if cnt[i]%2!=0:
		ans+=1
print(ans)
