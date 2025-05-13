#!/usr/bin/env python3

from library import read_int_tuple

def main():
    # Read input
    n, m, k = read_int_tuple()
    s = input().strip()
    t = input().strip()
    
    # Adjust indices for 1-indexing in strings
    n += 1
    m += 1
    
    # Create lists of indices for traversing the DP table
    # p contains indices in the DP table for forward traversal
    # r contains indices in the DP table for backward traversal
    p = [i for i in range(n * m - n) if (i + 1) % n]
    r = p[::-1]
    
    # d[i] will store the length of the common substring ending at position i
    d = [0] * (n * m)
    
    # Calculate the lengths of common substrings
    for i in p:
        if s[i % n] == t[i // n]:
            d[i] = d[i - n - 1] + 1
    
    # f[i] will store the maximum number of characters in k common substrings
    # ending at position i
    f = d[:]
    
    # Calculate f for k-1 more common substrings
    for y in range(k - 1):
        # Update f with maximum values from previous positions
        for i in p:
            f[i] = max(f[i], f[i - 1], f[i - n])
        
        # Update f for positions ending common substrings
        for i in r:
            f[i] = f[i - d[i] * (n + 1)] + d[i]
    
    # Find the maximum value in f
    print(max(f))

if __name__ == "__main__":
    main()