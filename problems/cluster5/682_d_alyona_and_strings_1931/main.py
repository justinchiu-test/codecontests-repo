#!/usr/bin/env python3

from library import read_int_tuple, read_str

def main():
    # Read input
    n, m, k = read_int_tuple()
    s = read_str()
    t = read_str()
    
    # Adjust indexing (make it 1-indexed for ease of DP)
    n += 1
    m += 1
    
    # Create a list of indices for iteration
    # p represents the indices in the DP array in a specific order
    # These indices represent positions in the 2D array flattened to 1D
    # Skip the indices that would be on the boundaries
    p = [i for i in range(n * m - n) if (i + 1) % n]
    r = p[::-1]  # Reversed order for second pass
    
    # Initialize DP tables
    # d[i] stores the length of the longest common substring ending at position i
    d = [0] * (n * m)
    
    # Calculate longest common substrings at each position
    for i in p:
        # Check if characters match
        if s[i % n] == t[i // n]:
            # If they match, extend the previous diagonal substring
            d[i] = d[i - n - 1] + 1
    
    # f[i] stores the maximum sum of lengths of at most k disjoint substrings
    f = d[:]  # Start with the same values as d
    
    # For each allowed substring (up to k-1 more after the first one)
    for y in range(k - 1):
        # First pass: propagate maximum values horizontally and vertically
        for i in p:
            f[i] = max(f[i], f[i - 1], f[i - n])
        
        # Second pass: update with the contribution of a new substring
        for i in r:
            # If there's a substring of length d[i] ending at position i,
            # consider adding it to the solution by jumping back d[i] positions
            # diagonally and adding d[i] to the result
            f[i] = f[i - d[i] * (n + 1)] + d[i]
    
    # Output the maximum possible sum of substring lengths
    print(max(f))

if __name__ == "__main__":
    main()