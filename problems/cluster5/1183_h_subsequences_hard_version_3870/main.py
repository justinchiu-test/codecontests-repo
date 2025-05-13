#!/usr/bin/env python3

from sys import path
path.append('..')
from library import read_ints, read_str, setup_fast_io

setup_fast_io()

def main():
    n, k = read_ints()
    s = read_str()
    
    # dp[i][j] stores the count of subsequences of length i+1 ending with letter j
    dp = [[0] * 26 for i in range(n + 1)]
    
    # Base case: empty string has 1 subsequence
    dp[0][0] = 1
    
    # Fill DP table
    for ch in s:
        j = ord(ch) - ord('a')
        for i in range(n, 0, -1):
            dp[i][j] = sum(dp[i - 1])
    
    # Calculate answer
    total_subseqs = 0
    total_cost = 0
    
    for i in range(n, -1, -1):
        current_subseqs = sum(dp[i])
        if total_subseqs + current_subseqs >= k:
            # We have enough subsequences now
            print((k - total_subseqs) * (n - i) + total_cost)
            break
        total_subseqs += current_subseqs
        total_cost += (n - i) * current_subseqs
    else:
        # Couldn't get enough subsequences
        print(-1)

if __name__ == "__main__":
    main()