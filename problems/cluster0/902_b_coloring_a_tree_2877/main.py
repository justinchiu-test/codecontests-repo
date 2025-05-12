#!/usr/bin/env python3

import sys
sys.path.append('/home/justinchiu_cohere_com/codecontests-repo/problems/cluster0')
from library import read_int, read_ints
from collections import deque

def solution():
    n = read_int()
    
    # Read parent relationships
    parents = read_ints()
    
    # Create adjacency list
    adj_list = [[] for _ in range(n+1)]
    child = {i: [] for i in range(1, n+1)}
    parent = {i: 0 for i in range(1, n+1)}
    
    for i in range(2, n+1):
        p = parents[i-2]
        parent[i] = p
        child[p].append(i)
    
    # Read colors
    colors = read_ints()
    color = {i: colors[i-1] for i in range(1, n+1)}
    
    # BFS to count color changes
    q = deque([1])
    ans = 0
    
    while q:
        node = q.popleft()
        p_color = 0 if node == 1 else color[parent[node]]
        
        if p_color != color[node]:
            ans += 1
            
        for child_node in child[node]:
            q.append(child_node)
    
    return ans

if __name__ == "__main__":
    print(solution())