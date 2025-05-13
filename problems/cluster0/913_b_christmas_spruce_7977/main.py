#!/usr/bin/env python3

from library import read_int

# Read number of nodes
n = read_int()
# Initialize arrays for nodes 1..n
nonleaf = [0] * (n + 1)
child = [[] for _ in range(n + 1)]
leaf = [0] * (n + 1)

def dfs(s):
    cnt = 0
    for chd in child[s]:
        cnt += dfs(chd)
    leaf[s] = cnt
    return 1 - nonleaf[s]

for i in range(2, n + 1):
    p = read_int()
    child[p].append(i)
    nonleaf[p] = 1

dfs(1)

# Check leaf condition
for i in range(1, n + 1):
    if nonleaf[i] and leaf[i] < 3:
        print("No")
        exit()

print("Yes")
