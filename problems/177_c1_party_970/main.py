#!/usr/bin/env python3

# maa chudaaye duniya
n = int(input())
parents = [i for i in range(n+1)]
ranks = [1 for i in range(n+1)]

def find(x):
	if parents[x] != x:
		parents[x] = find(parents[x])
	return parents[x]

def union(x, y):
	xs = find(x)
	ys = find(y)
	if xs == ys:
		return
	if ranks[xs] > ranks[ys]:
		parents[ys] = xs
	elif ranks[ys] > ranks[xs]:
		parents[xs] = ys
	else:
		parents[ys] = xs
		ranks[xs] += 1

for _ in range(int(input())):
	u, v = map(int, input().split())
	union(u, v)

# print(parents)
rejects = set([])
for _ in range(int(input())):
	p, q = map(int, input().split())
	ps = find(p)
	qs = find(q)
	if ps == qs:
		rejects.add(ps)
ps = {}
for i in range(1, n+1):
	p = find(i)
	if p not in rejects:
		if p in ps:
			ps[p] += 1
		else:
			ps[p] = 1
# print(ps)
ans = 0
for i in ps:
	ans = max(ans, ps[i])
print(ans)
