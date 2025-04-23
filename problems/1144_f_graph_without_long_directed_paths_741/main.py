#!/usr/bin/env python3

# lista doble enlazada o(1) en operaciones en los bordes
from collections import deque


def solve():
    global n, m
    n, m = map(lambda x: int(x), input().split())
    global maxValue
    maxValue = n**2
    graph = [[] for _ in range(0, n)]
    edges = []
    for _ in range(0, m):
        u, v = map(lambda x: int(x)-1, input().split())
        graph[u].append(v)
        graph[v].append(u)
        edges.append(v)

    distance = bfs_2k(graph, 0)
    if distance is None:
        print("NO")
    else:
        print("YES")
        print("".join(str(distance[e] % 2) for e in edges))


def bfs_2k(graph, initVertex):
    dist = [maxValue]*n
    queue = deque()
    queue.append(initVertex)
    dist[initVertex] = 0
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if(dist[v] == maxValue):
                dist[v] = dist[u] + 1
                queue.append(v)
            elif (dist[u] - dist[v]) % 2 == 0:
                return None
    return dist


solve()
