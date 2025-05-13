#!/usr/bin/env python3

from sys import path
path.append('..')
from library import read_ints, read_str, z_algorithm, init_dp_1d

def main():
    n, a, b = read_ints()
    s = read_str()
    
    # Initialize DP array
    dp = init_dp_1d(n)
    
    # Base case
    dp[0] = a
    
    for i in range(1, n):
        # Compute Z-function for the reversed string up to the current position
        t = s[:i+1]
        dp[i] = dp[i-1] + a  # Default: encode the character with cost a
        
        # Use Z-algorithm to find common prefixes in reversed string
        q = z_algorithm(t[::-1])
        
        # Calculate max suffix matches for each position
        maxs = init_dp_1d(i+1)
        maxs[0] = q[i]
        
        for j in range(1, i):
            maxs[j] = max(maxs[j-1], q[i-j])
        
        # Try to encode using previously seen substrings
        for j in range(i):
            if maxs[j] >= i-j:  # If there's a substring match
                dp[i] = min(dp[i], dp[j] + b)
    
    print(dp[n-1])

if __name__ == "__main__":
    main()