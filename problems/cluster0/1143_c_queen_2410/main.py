#!/usr/bin/env python3

from library import read_int, read_ints

def main():
    # Read number of nodes
    n = read_int()
    
    # Initialize arrays to track respect and child respect
    respect = [0] * n  # 1 if node disrespects, 0 if respects
    child_respect = [0] * n  # 1 if any child respects the node, 0 otherwise
    
    # Track root node
    root = -1
    
    # Read parent and respect information for each node
    for i in range(n):
        p, c = read_ints()
        if p == -1:
            # This is the root node
            root = i
            continue
        
        # Store whether this node disrespects its parent
        respect[i] = c
        
        # If a child respects its parent (c=0), mark the parent
        if not c:  # c=0 means the child respects the parent
            child_respect[p-1] = 1
    
    # Find nodes to remove (disrespectful nodes with no respectful children)
    to_remove = []
    for i in range(n):
        if i == root:
            continue
        
        if respect[i] and not child_respect[i]:
            # Node disrespects its parent and has no respectful children
            to_remove.append(i+1)  # Convert to 1-indexed
    
    # Output the result
    if to_remove:
        print(*to_remove)  # Unpacks the list as space-separated values
    else:
        print(-1)

if __name__ == "__main__":
    main()