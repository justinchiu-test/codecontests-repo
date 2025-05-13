#!/usr/bin/env python3

from sys import path
path.append('..')
from library import read_int, read_str, init_dp_2d, precompute_equal_words

N = 303
n = read_int()
input_str = read_str()
allsum = len(input_str)
words = input_str.split()

# Precompute equality of words
eq = precompute_equal_words(words)

# DP table where dp[i][j] is the number of consecutive equal words starting from i,j
dp = init_dp_2d(N, N)

# Compute DP table
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if eq[i][j]:
            if i < n - 1 and j < n - 1:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = 1

# Find minimum length after at most one abbreviation
ans = allsum
for i in range(n):
    su = 0  # Sum of lengths of words in the current segment
    for j in range(1, n - i + 1):  # Length of segment
        su += len(words[i + j - 1])
        cnt = 1  # Number of occurrences of the segment
        pos = i + j
        
        # Count occurrences of this segment
        while pos < n:
            if dp[i][pos] >= j:  # If there's a match of length at least j
                cnt += 1
                pos += j - 1
            pos += 1
            
        # Calculate new length after abbreviation
        cur = allsum - su * cnt + cnt
        if cnt > 1 and ans > cur:
            ans = cur

print(ans)