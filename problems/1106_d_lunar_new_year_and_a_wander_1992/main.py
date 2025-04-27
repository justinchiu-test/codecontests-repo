#!/usr/bin/env python3

from heapq import heappush, heappop
from library.io import read_int_pair
from library.graphs.graph import Graph

def main():
    n, m = read_int_pair()

    # Build graph
    g = Graph(n)

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1  # Convert to 0-indexed
        b -= 1
        g.add_edge(a, b)

    # Modified BFS with priority queue to visit vertices in ascending order
    visited = [False] * n
    pq = [0]  # Start from vertex 0
    ans = []

    visited[0] = True

    while pq:
        v = heappop(pq)
        ans.append(v)

        for neighbor in sorted(g.adj[v]):  # Sort neighbors to visit in ascending order
            if not visited[neighbor]:
                visited[neighbor] = True
                heappush(pq, neighbor)

    # Print result (convert back to 1-indexed)
    print(*[v + 1 for v in ans])

if __name__ == "__main__":
    main()
