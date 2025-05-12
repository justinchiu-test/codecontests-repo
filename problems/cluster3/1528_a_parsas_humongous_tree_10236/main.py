#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_int, setup_io

input = setup_io()

def main():
    t = read_int()
    INF = float("inf")
    for _ in range(t):
        n = read_int()
        L = []
        R = []
        for i in range(n):
            l, r = map(int, input().split())
            L.append(l)
            R.append(r)
        G = [[] for _ in range(n)]
        for i in range(n-1):
            a, b = map(int, input().split())
            a -= 1
            b -= 1  # 0-index
            G[a].append(b)
            G[b].append(a)

        root = 0
        par = [-1]*n
        stack = []
        stack.append(~0)
        stack.append(0)
        dp = [[0, 0] for _ in range(n)]
        
        while stack:
            v = stack.pop()
            if v >= 0:
                for u in G[v]:
                    if u == par[v]:
                        continue
                    par[u] = v
                    stack.append(~u)
                    stack.append(u)
            else:
                u = ~v  # child
                v = par[u]  # parent
                if v == -1:
                    continue
                zero = max(dp[u][0] + abs(L[v] - L[u]), dp[u][1] + abs(L[v] - R[u]))
                one = max(dp[u][0] + abs(R[v] - L[u]), dp[u][1] + abs(R[v] - R[u]))
                dp[v][0] += zero
                dp[v][1] += one
        ans = max(dp[0])
        print(ans)

if __name__ == "__main__":
    main()