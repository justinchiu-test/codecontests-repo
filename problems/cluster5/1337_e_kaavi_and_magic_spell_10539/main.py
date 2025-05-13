#!/usr/bin/env python3

import sys
from library import mod_add

# Set recursion limit and use fast input
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

# Read input strings
s = input().strip()
t = input().strip()

# Custom modulus for this problem
MOD = 998244353
r_lim = len(t)
n = len(s)

# dp[l][r] = number of ways to construct the magic spell for substring s[0:length]
# where l is the number of characters already matched with t from the left
# and r-l is the length of the substring of s
dp = [[0] * (n + 1) for i in range(n + 1)]

# Fill DP table
for length in range(1, n + 1):
    for l in range(n + 1):
        r = l + length
        if r > n:
            break
        
        # Base case: length = 1 (single character)
        if length == 1:
            if l >= r_lim or s[0] == t[l]:
                dp[l][r] = 2  # Can add this character to either side
            else:
                dp[l][r] = 0  # Cannot form a valid spell
            continue

        # Recursive case: try adding character to left or right
        if l >= r_lim or s[length - 1] == t[l]:
            # Add to left side
            dp[l][r] = mod_add(dp[l][r], dp[l + 1][r], MOD)
            
        if r - 1 >= r_lim or s[length - 1] == t[r - 1]:
            # Add to right side
            dp[l][r] = mod_add(dp[l][r], dp[l][r - 1], MOD)

# Sum up all valid magic spells
ans = 0
for i in range(r_lim, n + 1):
    ans = mod_add(ans, dp[0][i], MOD)

print(ans)