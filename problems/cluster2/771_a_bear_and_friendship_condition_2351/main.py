#!/usr/bin/env python3

from library import get_ints, DSU, yes_no
from collections import defaultdict

def main():
    n, m = get_ints()
    dsu = DSU(n + 1)
    edges = []
    
    # Process all friend relationships
    for _ in range(m):
        p1, p2 = get_ints()
        edges.append((p1, p2))
        # Union the two friends
        dsu.union(p1, p2)
    
    # Get components from DSU
    components = dsu.get_components()
    
    # Count edges in each component
    component_edges = defaultdict(int)
    for p1, p2 in edges:
        root = dsu.get(p1)
        component_edges[root] += 1
    
    # Check condition: In a complete graph with k nodes, there should be k*(k-1)/2 edges
    for root, members in components.items():
        if root == 0:  # Skip the 0 index since we're using 1-indexed vertices
            continue
        
        size = len(members)
        expected_edges = (size * (size - 1)) // 2
        
        if component_edges[root] != expected_edges:
            print("NO")
            return
    
    print("YES")

if __name__ == "__main__":
    main()