#!/usr/bin/env python3

from library import read_ints

# Read input
n, m = read_ints()

# Count node degrees (number of connections per node)
degrees = [0] * (n + 1)  # 1-indexed nodes

# Read edges and calculate node degrees
for _ in range(m):
    a, b = read_ints()
    degrees[a] += 1
    degrees[b] += 1

# Count occurrences of specific degree values
degree_1_count = 0  # Endpoints in bus topology
degree_2_count = 0  # Middle nodes in bus or all nodes in ring
degree_n_minus_1_count = 0  # Central node in star topology

for i in range(1, n + 1):
    if degrees[i] == 1:
        degree_1_count += 1
    if degrees[i] == 2:
        degree_2_count += 1
    if degrees[i] == n - 1:
        degree_n_minus_1_count += 1

# Determine topology
if degree_1_count == 2 and degree_2_count == n - 2:
    print("bus topology")
elif degree_2_count == n:
    print("ring topology")
elif degree_1_count == n - 1 and degree_n_minus_1_count == 1:
    print("star topology")
else:
    print("unknown topology")