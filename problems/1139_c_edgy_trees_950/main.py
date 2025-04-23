#!/usr/bin/env python3

kk=lambda:map(int,input().split())
ll=lambda:list(kk())
n, k = kk()
dsud = {i:{i} for i in range(n)}
dsup = {i:i for i in range(n)}
for _ in range(n-1):
	u, v, xi = kk()
	u,v = u-1,v-1
	if xi == 0:
		s1, s2 = dsud[dsup[u]], dsud[dsup[v]]
		if len(s1) > len(s2):
			s1 |= s2
			del dsud[dsup[v]]
			for el in s2:
				dsup[el] = dsup[u]
		else:
			s2 |= s1
			del dsud[dsup[u]]
			for el in s1:
				dsup[el] = dsup[v]
val = 0
for se in dsud:
	val += len(dsud[se])**k
print((n**k - val)%(7+10**9))
