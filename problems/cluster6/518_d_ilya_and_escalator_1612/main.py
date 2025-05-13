#!/usr/bin/env python3

import sys
import os

# Add parent directory to path to import library
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_strs, print_float_exact, dp_array_2d, expected_value

# Read input
n, p, t = read_strs()
n = int(n)   # Number of people
p = float(p) # Probability of moving forward
t = int(t)   # Time limit

# Simple case: p = 0 or p = 1
if p == 0:
    print_float_exact(0)
    exit()
if p == 1:
    print_float_exact(min(n, t))
    exit()

# Dynamic programming approach
# dp[i][j] = probability that after i time units, j people have reached the end
dp = dp_array_2d(t + 1, n + 1, 0.0)
dp[0][0] = 1.0  # At time 0, probability of 0 people at end is 1

# Fill DP table
for time in range(t):
    for people in range(n):
        # Probability that a person moves
        dp[time + 1][people + 1] += dp[time][people] * p
        # Probability that a person doesn't move
        dp[time + 1][people] += dp[time][people] * (1 - p)
    # If n people are already at the end, they stay there
    dp[time + 1][n] += dp[time][n]

# Calculate expected value - probability of j people at the escalator's end * j
probabilities = dp[t]
values = list(range(n + 1))  # 0, 1, 2, ..., n
expected = expected_value(probabilities, values)

print_float_exact(expected)