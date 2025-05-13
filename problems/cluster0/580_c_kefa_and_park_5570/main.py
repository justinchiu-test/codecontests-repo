#!/usr/bin/env python3

from library import read_int, read_ints, read_edges, adj_list

# Read input
n, m = read_ints()
c = read_ints()
# Build tree adjacency list
t = adj_list(n, read_edges(n-1))
v = [0] * n
a=i=0
q=[(0,0)]
while i<len(q):
    x,N=q[i]
    v[x]=1
    if c[x]+N<=m:
        L=1
        for y in t[x]:
            if not v[y]:
                L=0
                q.append((y,c[x]*(c[x]+N)))
        if L:
            a+=1
    i+=1
print(a)
