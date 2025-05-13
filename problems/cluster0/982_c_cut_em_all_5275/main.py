#!/usr/bin/env python3

from library import read_int, run_with_large_stack, setup_large_recursion

def dfs(node, g, par, sz):
    for i in g[node]:
        if i != par:
            sz[node] += dfs(i, g, node, sz)
    return sz[node] + 1

def main():
    n = read_int()
    if n % 2 != 0:
        print(-1)
        exit(0)
    
    # Read tree
    g = [[] for _ in range(n)]
    for i in range(n-1):
        x, y = map(int, input().split())
        g[x-1].append(y-1)
        g[y-1].append(x-1)
    
    # Calculate subtree sizes
    sz = [0] * n
    dfs(0, g, -1, sz)
    
    # Count edges to remove
    res = 0
    for i in range(1, n):
        if sz[i] % 2 != 0:
            res += 1
    print(res)

setup_large_recursion()
run_with_large_stack(main)