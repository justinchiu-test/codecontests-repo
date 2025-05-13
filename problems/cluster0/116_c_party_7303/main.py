#!/usr/bin/env python3

from library import read_int, make_graph, find_max_depth

def main():
    n = read_int()
    
    # Create graph
    graph = [[] for _ in range(n)]
    roots = []
    
    # Read parent-child relationships
    for i in range(n):
        parent = read_int()
        
        if parent > 0:
            # This employee has a manager
            graph[parent - 1].append(i)
        else:
            # This is a root employee (no manager)
            roots.append(i)
    
    # Find maximum depth across all root employees
    max_depth = max(find_max_depth(graph, root) for root in roots) + 1  # +1 because depth starts at 0
    print(max_depth)

if __name__ == "__main__":
    main()