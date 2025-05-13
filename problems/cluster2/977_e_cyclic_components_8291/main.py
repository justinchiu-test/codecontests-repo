#!/usr/bin/env python3

from library import get_ints, count_cyclic_components

n, m = get_ints()
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(count_cyclic_components(graph))