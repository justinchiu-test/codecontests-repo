#!/usr/bin/env python3

from library import read_int, read_ints

n = read_int()
fcs = [0] + read_ints()  # Function codes
ps = [0, 0] + read_ints()  # Parent nodes
cs = [1] * (n + 1)  # Counter for each node

# Mark non-leaf nodes
for i in range(2, n + 1):
    cs[ps[i]] = 0

# Count leaf nodes
nc = sum(cs) - 1

# Process from leaves to root
for i in range(n, 1, -1):
    if fcs[ps[i]] == 0:  # Min operation
        cs[ps[i]] += cs[i]
    else:  # Max operation
        if not cs[ps[i]]:
            cs[ps[i]] = cs[i]
        else:
            cs[ps[i]] = min(cs[ps[i]], cs[i])

# Calculate and print the result
print(nc - cs[1] + 1)