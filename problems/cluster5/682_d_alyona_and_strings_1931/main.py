#!/usr/bin/env python3

from sys import path
path.append('..')
from library import read_ints, read_str, init_dp_1d

# Read input
n, m, k = read_ints()
s = read_str()
t = read_str()

# Add 1 to account for 1-indexing
n += 1
m += 1

# Generate indices for flattened matrix
p = [i for i in range(n * m - n) if (i + 1) % n]
r = p[::-1]  # Reversed indices

# Initialize DP arrays
# d[i] = length of common substring ending at position i
d = init_dp_1d(n * m)

# Compute lengths of common substrings
for i in p:
    if s[i % n] == t[i // n]:
        d[i] = d[i - n - 1] + 1

# f[i] = maximum length of k disjoint common substrings ending at position i
f = d[:]

# For each allowed number of segments
for y in range(k - 1):
    # Try to extend existing solutions
    for i in p:
        f[i] = max(f[i], f[i - 1], f[i - n])
    
    # Try to start a new segment
    for i in r:
        f[i] = f[i - d[i] * (n + 1)] + d[i]

print(max(f))