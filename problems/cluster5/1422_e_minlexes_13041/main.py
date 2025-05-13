#!/usr/bin/env python3

import sys

def main():
    s = input().strip()
    N = len(s)
    
    # Handle the single character case
    if N == 1:
        print(1, s[0])
        sys.exit()
    
    # X stores the minlex strings and Y stores their lengths
    X = [s[-1], s[-2] + s[-1] if s[-2] != s[-1] else ""]
    Y = [1, 2 if s[-2] != s[-1] else 0]
    
    # Process the string from right to left
    for i in range(N - 3, -1, -1):
        c = s[i]
        
        # Option 1: Add current character
        k1 = c + X[-1]
        ng = Y[-1] + 1
        
        # Truncate long strings for display
        if ng > 10:
            k1 = k1[:5] + "..." + k1[-2:]
        
        # Option 2: Remove a character if it's a duplicate and creates a lexicographically smaller string
        if c == s[i + 1] and k1 > X[-2]:
            k1 = X[-2]
            ng = Y[-2]
        
        X.append(k1)
        Y.append(ng)
    
    # Print the results in reverse order
    for i in range(N - 1, -1, -1):
        print(Y[i], X[i])

if __name__ == "__main__":
    main()