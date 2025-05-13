#!/usr/bin/env python3
from library import ints, identify_network_topology

n, m = ints()
degree = [0] * (n + 1)

# Count degrees of each node
for _ in range(m):
    a, b = ints()
    degree[a] += 1
    degree[b] += 1

# Identify and print the network topology
print(identify_network_topology(n, degree))