#!/usr/bin/env python3

from library import *
import heapq
from collections import deque

def main():
    n = read_int()
    p = list(read_ints())
    graph = [[] for _ in range(n+1)]
    root = 0
    for i in range(1, n+1):
        parent = p[i-1]
        if parent == 0:
            root = i
        else:
            graph[i].append(parent)
            graph[parent].append(i)
    if n % 2 == 0:
        print('NO')
        return
    # compute depths
    depth = [0] * (n+1)
    dq = deque([root])
    visited = [False] * (n+1)
    visited[root] = True
    while dq:
        u = dq.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                dq.append(v)
    # compute degrees
    deg = [len(graph[i]) for i in range(n+1)]
    # priority queue for candidates
    heap = []
    for i in range(1, n+1):
        if deg[i] % 2 == 0:
            heapq.heappush(heap, (-depth[i], i))
    ans = []
    deleted = [False] * (n+1)
    while heap:
        d, u = heapq.heappop(heap)
        if deleted[u] or deg[u] % 2 != 0:
            continue
        deleted[u] = True
        ans.append(u)
        for v in graph[u]:
            if not deleted[v]:
                deg[v] -= 1
                if deg[v] % 2 == 0:
                    heapq.heappush(heap, (-depth[v], v))
    if len(ans) != n:
        print('NO')
    else:
        print('YES')
        for u in ans:
            print(u)

if __name__ == '__main__':
    main()
