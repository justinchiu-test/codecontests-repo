#!/usr/bin/env python3

import sys
from sys import stdin
import math
from collections import deque

import sys

class scc_graph:

    def __init__(self, N):
        self.N = N
        self.edges = []

    def csr(self):
        self.start = [0]*(self.N+1)
        self.elist = [0]*len(self.edges)
        for e in self.edges:
            self.start[e[0]+1] += 1
        for i in range(1, self.N+1):
            self.start[i] += self.start[i-1]
        counter = self.start[:]
        for e in self.edges:
            self.elist[counter[e[0]]] = e[1]
            counter[e[0]] += 1

    def add_edge(self, v, w):
        self.edges.append((v, w))

    def scc_ids(self):
        self.csr()
        N = self.N
        now_ord = group_num = 0
        visited = []
        low = [0]*N
        order = [-1]*N
        ids = [0]*N
        parent = [-1]*N
        stack = []
        for i in range(N):
            if order[i] == -1:
                stack.append(i)
                stack.append(i)
                while stack:
                    v = stack.pop()
                    if order[v] == -1:
                        low[v] = order[v] = now_ord
                        now_ord += 1
                        visited.append(v)
                        for i in range(self.start[v], self.start[v+1]):
                            to = self.elist[i]
                            if order[to] == -1:
                                stack.append(to)
                                stack.append(to)
                                parent[to] = v
                            else:
                                low[v] = min(low[v], order[to])
                    else:
                        if low[v] == order[v]:
                            while True:
                                u = visited.pop()
                                order[u] = N
                                ids[u] = group_num
                                if u == v:
                                    break
                            group_num += 1
                        if parent[v] != -1:
                            low[parent[v]] = min(low[parent[v]], low[v])
        for i, x in enumerate(ids):
            ids[i] = group_num-1-x

        return group_num, ids

    def scc(self):
        group_num, ids = self.scc_ids()
        groups = [[] for _ in range(group_num)]
        for i, x in enumerate(ids):
            groups[x].append(i)
        return groups

"""
def SCC(N,M,elis):

    lis = [ [] for i in range(N) ]
    rlis = [ [] for i in range(N)]

    for u,v in elis:
        lis[u].append(v)
        rlis[v].append(u)

    stk = []
    nind = [0] * N
    visit = [False] * N
    leave = [None] * N
    nl = 0

    for loop in range(N):

        if visit[loop] == False:
            visit[loop] = True
            stk.append(loop)

            while stk:
                if nind[stk[-1]] >= len(lis[stk[-1]]):
                    leave[stk[-1]] = nl
                    nl += 1
                    del stk[-1]

                else:
                    nexv = lis[stk[-1]][nind[stk[-1]]]
                    nind[stk[-1]] += 1
                    if not visit[nexv]:
                        stk.append(nexv)
                        visit[nexv] = True


    visit = [False] * N
    mv = [ (leave[i],i) for i in range(N) ]
    mv.sort()
    ret = []

    while mv:

        tmp,v = mv[-1]
        del mv[-1]

        if not visit[v]:

            visit[v] = True
            q = [v]
            nlinks = []

            while q:
                x = q[-1]
                del q[-1]
                nlinks.append(x)

                for nex in rlis[x]:
                    if not visit[nex]:
                        visit[nex] = True
                        q.append(nex)

            ret.append(nlinks)
    return ret
"""

n,m = map(int,stdin.readline().split())
N = n

sg = scc_graph(n)

lis = [ [] for i in range(n)]
elis = []
for i in range(m):
    a,b,l = map(int,stdin.readline().split())
    a -= 1
    b -= 1

    lis[a].append((b,l))
    sg.add_edge(a,b)

SC = sg.scc()
sclis = [None] * N
for i in range(len(SC)):
    for j in SC[i]:
        sclis[j] = i

scgcd = [None] * len(SC)
d = [None] * N

for i in range(N):

    if scgcd[sclis[i]] == None:

        ngcd = float("inf")
        q = deque([i])
        d[i] = 0

        while q:
            v = q.popleft()

            for nex,l in lis[v]:
                if sclis[nex] == sclis[v]:
                    if d[nex] == None:
                        d[nex] = d[v] + l
                        q.append(nex)
                    elif abs(d[nex]-d[v]-l) != 0:
                        if ngcd == float("inf"):
                            ngcd = abs(d[nex] - d[v]-l)
                        else:
                            ngcd = math.gcd(ngcd,abs(d[nex]-d[v]-l))

        scgcd[sclis[i]] = ngcd

q = int(stdin.readline())
ANS = []

#print (SC)
#print (scgcd)

for loop in range(q):

    vi,si,ti = map(int,stdin.readline().split())
    vi -= 1

    if scgcd[sclis[vi]] == float("inf"):
        if si == 0:
            ANS.append("YES")
        else:
            ANS.append("NO")
    else:
        if ((-1*si) % ti) % math.gcd(scgcd[sclis[vi]] , ti) == 0:
            ANS.append("YES")
        else:
            ANS.append("NO")

print ("\n".join(ANS))
