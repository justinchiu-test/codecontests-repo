#!/usr/bin/env python3

from library import setup_io, min_max_soulmate_paths

# Set up fast I/O
input = setup_io()

def solve():
    k = int(input())
    n = 2*k

    # Build weighted adjacency list
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b, t = map(int, input().split())
        a -= 1  # Convert to 0-indexed
        b -= 1
        adj[a].append((b, t))
        adj[b].append((a, t))

    # Calculate minimum and maximum path sums
    min_sum, max_sum = min_max_soulmate_paths(adj, k)
    print(min_sum, max_sum)

for _ in range(int(input())):
    solve()
