#!/usr/bin/env python3

from library import setup_io
from collections import deque

# Set up fast I/O
input = setup_io()

# Constants
MOD = 10**9 + 7

# Read input
n = int(input())
edges = []
for _ in range(n-1):
    x, y = map(int, input().split())
    x, y = x-1, y-1  # Convert to 0-indexed
    edges.append((x, y))

# Precompute pascal triangle for combinatorial calculations
pre = [1]
pascal = [pre]
for i in range(n + 2):
    ne = [0] * (i + 2)
    for j, a in enumerate(pre):
        ne[j] = (ne[j] + a) % MOD
        ne[j+1] = (ne[j+1] + a) % MOD
    pascal.append(ne)
    pre = ne

# Calculate cumulative sums for each row in the pascal triangle
for row in pascal:
    for i in range(len(row) - 1):
        row[i+1] = (row[i+1] + row[i]) % MOD

# Precompute powers of 1/2 modulo MOD
half = (MOD + 1) >> 1  # 1/2 modulo MOD
half_powers = [1]
for _ in range(n + 5):
    half_powers.append(half_powers[-1] * half % MOD)

# Precompute inverse of n modulo MOD
inverse_n = pow(n, MOD - 2, MOD)

# Calculate expected number of inversions
ans = 0

# Try each node as potential first marked node
for root in range(n):
    # Build adjacency list for this iteration
    adj = [[] for _ in range(n)]
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    # BFS from root
    parent = [-1] * n
    queue = deque([root])
    visit_order = []
    depth = [0] * n

    while queue:
        node = queue.popleft()
        visit_order.append(node)

        for neighbor in list(adj[node]):  # Use list to avoid modification issues
            if neighbor != parent[node]:
                parent[neighbor] = node
                adj[neighbor].remove(node)  # Remove parent edge
                queue.append(neighbor)
                depth[neighbor] = depth[node] + 1

    # Calculate subtree sizes
    subtree_size = [1] * n
    for node in visit_order[1:][::-1]:
        subtree_size[parent[node]] += subtree_size[node]

    # Calculate contribution to inversions
    for node in visit_order:
        if node <= root:
            continue

        d = depth[node]
        # Direct contribution from this node's subtree
        ans = (ans + subtree_size[node] * inverse_n) % MOD

        # Check all nodes on the path to root
        curr = node
        while parent[curr] != root:
            p = parent[curr]
            # Size of the rest of parent's subtree
            s = subtree_size[p] - subtree_size[curr]

            # Contribution from this subtree
            contribution = (s * pascal[d-1][depth[p]-1]) % MOD
            contribution = (contribution * inverse_n) % MOD
            contribution = (contribution * half_powers[d-1]) % MOD

            ans = (ans + contribution) % MOD
            curr = p

print(ans)

