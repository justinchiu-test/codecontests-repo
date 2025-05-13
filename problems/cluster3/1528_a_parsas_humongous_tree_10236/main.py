#!/usr/bin/env python3
from sys import path
path.append("/home/justinchiu_cohere_com/codecontests-repo/problems/cluster3")
from library import read_int, read_ints

def main():
    t = read_int()  # Number of test cases
    
    for _ in range(t):
        n = read_int()  # Number of nodes
        
        # Read limits for each node
        limits = []
        for _ in range(n):
            l, r = read_ints()
            limits.append((l, r))
        
        # Read tree edges
        adj = [[] for _ in range(n)]
        for _ in range(n-1):
            a, b = read_ints()
            a -= 1  # Convert to 0-indexed
            b -= 1
            adj[a].append(b)
            adj[b].append(a)
        
        # DP table: dp[node][val] = max beauty when node has value val
        # val = 0 means lower limit, val = 1 means upper limit
        dp = [[0, 0] for _ in range(n)]
        
        def dfs(node, parent):
            l, r = limits[node]
            
            # Initialize with 0 (no contribution from children yet)
            dp[node][0] = 0  # Using lower limit
            dp[node][1] = 0  # Using upper limit
            
            for child in adj[node]:
                if child == parent:
                    continue
                
                # Process child recursively
                dfs(child, node)
                
                cl, cr = limits[child]
                
                # When parent uses lower limit (l)
                dp[node][0] += max(
                    dp[child][0] + abs(l - cl),  # Child uses lower limit
                    dp[child][1] + abs(l - cr)   # Child uses upper limit
                )
                
                # When parent uses upper limit (r)
                dp[node][1] += max(
                    dp[child][0] + abs(r - cl),  # Child uses lower limit
                    dp[child][1] + abs(r - cr)   # Child uses upper limit
                )
        
        # Start DFS from node 0
        dfs(0, -1)
        
        # Maximum beauty is the max of using lower or upper limit for the root
        print(max(dp[0][0], dp[0][1]))

if __name__ == "__main__":
    main()