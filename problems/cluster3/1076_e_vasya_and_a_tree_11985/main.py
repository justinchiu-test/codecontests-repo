#!/usr/bin/env python3
import sys
from collections import defaultdict, deque

def main():
    # Read input
    n = int(input())
    adj = [[] for _ in range(n+1)]
    
    for _ in range(n-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    m = int(input())
    queries = defaultdict(list)
    for _ in range(m):
        v, d, x = map(int, input().split())
        queries[v].append((d, x))
        
    # Calculate tree depths with BFS
    depths = [-1] * (n+1)
    depths[1] = 0  # Root has depth 0
    queue = deque([1])
    
    while queue:
        node = queue.popleft()
        for child in adj[node]:
            if depths[child] == -1:  # Not visited
                depths[child] = depths[node] + 1
                queue.append(child)
    
    # Build children list for each node
    children = [[] for _ in range(n+1)]
    for i in range(2, n+1):  # Start from node 2 (non-root)
        # Find parent (the node with smaller depth)
        for neighbor in adj[i]:
            if depths[neighbor] < depths[i]:
                children[neighbor].append(i)
                break
    
    # Create prefix sum array to process range updates efficiently
    values = [0] * (n+1)
    
    # Function to apply a query (add value to all nodes in d-subtree of v)
    def apply_query(v, d, x):
        # BFS from node v to process all nodes up to distance d
        queue = deque([(v, 0)])  # (node, distance from v)
        visited = [False] * (n+1)
        visited[v] = True
        
        while queue:
            node, dist = queue.popleft()
            
            if dist <= d:
                values[node] += x
                
                for neighbor in adj[node]:
                    if not visited[neighbor] and depths[neighbor] > depths[v]:  # Only descendants
                        visited[neighbor] = True
                        queue.append((neighbor, dist + 1))
    
    # Apply all queries
    for v in range(1, n+1):
        for d, x in queries[v]:
            apply_query(v, d, x)
    
    # Output the result
    print(*values[1:])

if __name__ == "__main__":
    main()