#!/usr/bin/env python3

from library import read_int, read_ints, make_graph, calculate_subtree_sizes
import sys

def main():
    n = read_int()
    if n % 2 != 0:
        print(-1)
        sys.exit(0)
    
    # Build the graph
    graph = make_graph(n)
    for _ in range(n - 1):
        x, y = read_ints()
        x -= 1  # Convert to 0-indexed
        y -= 1
        graph[x].append(y)
        graph[y].append(x)
    
    # Calculate subtree sizes
    subtree_sizes = calculate_subtree_sizes(graph, 0)
    
    # Count edges to remove
    result = 0
    for i in range(1, n):  # Skip the root
        # If the subtree has an even number of nodes, 
        # removing the edge to its parent would create
        # two even-sized components
        if subtree_sizes[i] % 2 == 0:
            result += 1
    
    print(result)

if __name__ == "__main__":
    main()