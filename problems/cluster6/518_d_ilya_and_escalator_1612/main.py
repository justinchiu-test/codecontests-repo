#!/usr/bin/env python3

from library import read_floats

# Read the input
n, p, t = read_floats()
n = int(n)
t = int(t)

# Special cases for efficiency
if p == 0:
    print("0.000000000000")
    exit()
elif p == 1:
    print(f"{min(n, t):.12f}")
    exit()

# Define DP array: dp[i][j] = probability that j people are on escalator after i seconds
dp = [[0] * (n + 1) for _ in range(t + 1)]

# Base case: initially 0 people on escalator with probability 1
dp[0][0] = 1

# Fill the DP table using recurrence relation
for i in range(1, t + 1):  # For each second
    for j in range(n + 1):  # For each possible number of people on escalator
        if j == 0:  # No person entered yet
            dp[i][0] = dp[i-1][0] * (1 - p)  # No one entered in this second
        elif j == n:  # Maximum people reached
            dp[i][n] = dp[i-1][n-1] * p + dp[i-1][n]  # Last person entered or no one entered
        else:  # 0 < j < n
            dp[i][j] = dp[i-1][j-1] * p + dp[i-1][j] * (1 - p)  # New person entered or no one entered

# Calculate expected value: ∑(j * Probability of j people on escalator after t seconds)
expected_people = sum(j * dp[t][j] for j in range(n + 1))

# Print the result with the expected format (12 decimal places)
print(f"{expected_people:.12f}")