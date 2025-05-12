#!/usr/bin/env python3

import sys
sys.path.append('/home/justinchiu_cohere_com/codecontests-repo/problems/cluster2')
from library import create_graph, read_ints
from collections import deque

def solve_test():
    n, m, a, b = read_ints()
    a -= 1  # Convert to 0-indexed
    b -= 1
    
    edges = []
    for _ in range(m):
        u, v = read_ints()
        edges.append((u, v))
    
    graph = create_graph(n, edges, directed=False, one_indexed=True)
    
    # Count vertices that can reach a but not b
    def count_reachable_except(start, exclude):
        """Count vertices reachable from start if we remove exclude."""
        visited = [False] * n
        visited[exclude] = True  # Mark the excluded vertex as visited to avoid traversing through it
        
        queue = deque([start])
        visited[start] = True
        count = 0
        
        while queue:
            node = queue.popleft()
            count += 1
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return count
    
    # Vertices reachable from a if we remove b
    count_a = count_reachable_except(a, b)
    # Vertices reachable from b if we remove a
    count_b = count_reachable_except(b, a)
    
    # Answer is (vertices only reachable from a) * (vertices only reachable from b)
    return str((n - count_b - 1) * (n - count_a - 1))

# Solve all test cases
t = read_ints()[0]
answers = []

for _ in range(t):
    answers.append(solve_test())

print("\n".join(answers))