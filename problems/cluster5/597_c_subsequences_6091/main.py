#!/usr/bin/env python3

from library import (
    read_int_tuple, setup_fast_io, 
    build_fenwick_tree, update_fenwick_tree, query_fenwick_tree
)

# Setup fast IO
input = setup_fast_io()

def main():
    n, k = read_int_tuple()
    arr = [int(input()) for _ in range(n)]
    
    # Initialize DP table
    dp = [[0] * n for _ in range(k + 1)]
    dp[0] = [1] * n  # Base case: 1 way to form a subsequence of length 0
    
    for i in range(1, k + 1):
        # Use a Fenwick tree for each level of DP
        fenwick = [0] * (n + 1)
        
        for j in range(n):
            # Query the Fenwick tree to get the sum of values less than current element
            dp[i][j] = query_fenwick_tree(fenwick, arr[j] - 1)
            
            # Update the Fenwick tree with the DP value from the previous level
            update_fenwick_tree(fenwick, arr[j], dp[i - 1][j])
    
    # Sum all values in the last row to get the total number of subsequences
    return sum(dp[k])

if __name__ == '__main__':
    print(main())