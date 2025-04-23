#!/usr/bin/env python3

from collections import deque
import sys
input = sys.stdin.readline


n, m, MOD = map(int, input().split())
u = list(map(int, input().split()))
info = [list(map(int, input().split())) for i in range(m)]

graph = [[] for i in range(n)]
rev_graph = [[] for i in range(n)]
set_ = set()
INF = 10 ** 9
for a, b in info:
    a -= 1
    b -= 1
    if (u[a] + 1) % MOD == u[b]:
        if a * INF + b not in set_:
            graph[a].append(b)
            rev_graph[b].append(a)
            set_.add(a * INF + b)
    if (u[b] + 1) % MOD == u[a]:
        if b * INF + a not in set_:
            graph[b].append(a)
            rev_graph[a].append(b)
            set_.add(b * INF + a)

def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
    def dfs(s):
        used[s] = 1
        q = deque([s])
        tmp = deque([s])
        while q:
            s = q.pop()
            for t in G[s]:
                if not used[t]:
                    used[t] = 1
                    q.append(t)
                    tmp.append(t)
        while tmp:
            order.append(tmp.pop())
    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        q = deque([s])
        while q:
            s = q.pop()
            for t in RG[s]:
                if not used[t]:
                    q.append(t)
                    used[t] = 1
                    group[t] = col
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group

def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v + 1)
    return G0, GP

min_ans = 10 ** 9
ind_ans = -1
label, group = scc(n, graph, rev_graph)
new_graph, element = construct(n, graph, label, group)
for i in range(len(new_graph)):
    if len(new_graph[i]) == 0 and min_ans > len(element[i]):
        min_ans = len(element[i])
        ind_ans = i

print(min_ans)
print(*element[ind_ans])
