#!/usr/bin/env python3

from library import read_str
from sys import setrecursionlimit

def main():
    # Increase recursion limit for deep recursion
    setrecursionlimit(200000)
    
    # Read input
    s = read_str() + ' '  # Add a space to avoid index out of bounds
    
    # Dictionary to store unique suffixes
    suffixes = {}
    
    # Set to track visited states (to avoid repeated calculations)
    visited = set()
    
    # Recursive function to generate suffixes
    def generate_suffixes(position, prev_pos):
        # If this state has been visited before, return early
        if (position, prev_pos) in visited:
            return
        
        # Mark this state as visited
        visited.add((position, prev_pos))
        
        # Only consider suffixes if the remaining root is long enough
        if position > 6:
            # Add suffix of length 2
            suffix_2 = s[position - 2:position]
            suffixes[suffix_2] = 1
            
            # If not the same as the previous suffix, continue recursively
            if suffix_2 != s[position:prev_pos]:
                generate_suffixes(position - 2, position)
        
        # For suffix of length 3
        if position > 7:
            # Add suffix of length 3
            suffix_3 = s[position - 3:position]
            suffixes[suffix_3] = 1
            
            # If not the same as the previous suffix, continue recursively
            if suffix_3 != s[position:prev_pos]:
                generate_suffixes(position - 3, position)
    
    # Start generating suffixes from the end of the string
    generate_suffixes(len(s) - 1, len(s))
    
    # Output the results
    print(len(suffixes))
    for suffix in sorted(suffixes):
        print(suffix)

if __name__ == "__main__":
    main()