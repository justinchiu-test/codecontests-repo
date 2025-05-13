#!/usr/bin/env python3
from sys import path
path.append("/home/justinchiu_cohere_com/codecontests-repo/problems/cluster3")
from library import read_int, read_ints, tree_dp_bottom_up

def main():
    n = read_int()
    if n == 1:
        print(1)
        return
        
    parents = [0, 0] + read_ints()  # 1-indexed
    
    # Create adjacency list from parent array
    adj = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        adj[parents[i]].append(i)
    
    # Process function for tree DP - count leaves in subtree
    def process_node(node, parent, child_results):
        if not child_results:  # Leaf node
            return 1
        return sum(child_results)
    
    # Calculate colors needed (leaf count in each subtree)
    colors = tree_dp_bottom_up(adj, process_node, 1)
    
    # Sort and output colors
    result = sorted(colors[1:])
    print(*result)

if __name__ == "__main__":
    main()