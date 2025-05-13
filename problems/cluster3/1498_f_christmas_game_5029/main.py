#!/usr/bin/env python3

from library import read_int_tuple, read_ints, rooted_tree_game_theory, enable_fast_io

def main():
    enable_fast_io()
    
    # Read input
    n, k = read_int_tuple()
    
    # Build the tree
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        x, y = read_int_tuple()
        x -= 1  # Convert to 0-indexed
        y -= 1
        graph[x].append(y)
        graph[y].append(x)
    
    # Read node values
    node_values = read_ints()
    
    # Calculate game results for each possible root
    results = rooted_tree_game_theory(graph, node_values, k)
    
    # Print results
    print(*results)

if __name__ == "__main__":
    main()