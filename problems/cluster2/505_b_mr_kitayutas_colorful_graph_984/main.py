#!/usr/bin/env python3

from library import get_ints, dfs

def main():
    n, m = get_ints()
    
    # Create a dictionary of colored graphs
    # For each color, we have an adjacency list
    colored_graphs = {}
    
    for _ in range(m):
        u, v, c = get_ints()
        if c not in colored_graphs:
            colored_graphs[c] = [[] for _ in range(n+1)]
        colored_graphs[c][u].append(v)
        colored_graphs[c][v].append(u)
    
    # Process queries
    q = get_ints()[0]
    for _ in range(q):
        u, v = get_ints()
        count = 0
        
        # Check each color
        for c in colored_graphs:
            # Check if u and v are connected using only edges of color c
            visited = set()
            dfs(colored_graphs[c], u, visited)
            if v in visited:
                count += 1
        
        print(count)

if __name__ == "__main__":
    main()