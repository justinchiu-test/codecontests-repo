#!/usr/bin/env python3

import sys
sys.path.append('..')
from library import update, query, setup_fast_io, multi_input

input = setup_fast_io()

def main():
    n, k = map(int, input().split())
    arr = multi_input(n)
    
    # Compute the power of 2 greater than or equal to n
    si = 1 << (n.bit_length() - (not n & (n - 1)))
    
    # dp[i][j] = number of increasing subsequences of length i ending at index j
    dp = [[0] * n for _ in range(k + 1)]
    dp[0] = [1] * n  # Base case: subsequence of length 0 is always 1 way
    
    for i in range(1, k + 1):
        tree = [0] * (si << 1)  # Create segment tree for each level
        for j in range(n):
            # Query the segment tree for sum of dp[i-1][j] where arr[j] < arr[current]
            dp[i][j] = query(tree, 1, arr[j], si)
            # Update the segment tree at arr[j] with the value dp[i-1][j]
            update(tree, arr[j], dp[i - 1][j], si)
    
    print(sum(dp[-1]))

if __name__ == '__main__':
    main()