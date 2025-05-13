#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

def main():
    n, k = map(int, input().split())
    
    # Build adjacency list
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # DFS to compute subtree sizes and depths
    subtree_size = [0] * (n+1)
    depth = [0] * (n+1)
    
    def dfs(node, parent, d):
        depth[node] = d
        size = 1  # Count the node itself
        
        for child in adj[node]:
            if child != parent:
                size += dfs(child, node, d+1)
        
        subtree_size[node] = size
        return size
    
    # Start DFS from node 1 (root)
    dfs(1, -1, 0)
    
    # Calculate the "profit" of making each city an industrial city
    # For each node, profit = depth - (subtree_size - 1)
    profit = []
    for i in range(1, n+1):
        # Subtract 1 from subtree size to exclude the node itself
        profit.append((depth[i] - (subtree_size[i] - 1), i))
    
    # Sort by profit in descending order
    profit.sort(reverse=True)
    
    # Take the k cities with highest profit for industrial cities
    total_happiness = 0
    for i in range(k):
        node_profit, city = profit[i]
        total_happiness += node_profit
    
    print(total_happiness)

if __name__ == "__main__":
    main()