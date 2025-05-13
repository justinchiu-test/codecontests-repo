#!/usr/bin/env python3

from library import read_int_tuple, read_int, update, query

def main():
    n, k = read_int_tuple()
    arr = [read_int() for _ in range(n)]
    
    # Calculate the size needed for our segment tree (power of 2)
    si = 1 << (n.bit_length() - (not n & (n - 1)))
    
    # Initialize DP table
    # dp[i][j] = count of subsequences of length i+1 ending at position j
    dp = [[0] * n for _ in range(k + 1)]
    dp[0] = [1] * n  # Base case: subsequences of length 1
    
    # Fill the DP table using segment tree for each length
    for i in range(1, k + 1):
        tree = [0] * (si << 1)  # Initialize segment tree for this length
        
        for j in range(n):
            # Query: How many subsequences of length i end before arr[j]
            dp[i][j] = query(tree, 1, arr[j], si)
            
            # Update: Add this subsequence of length i-1 ending at position j
            update(tree, arr[j], dp[i - 1][j], si)
    
    # Sum up all subsequences of length k+1
    print(sum(dp[k]))

if __name__ == "__main__":
    main()