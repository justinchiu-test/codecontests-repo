#!/usr/bin/env python3

from library import read_mixed_types, init_dp_table, print_float, expected_value

# Read input: n (number of people), p (probability of moving), t (time limit)
n, p, t = read_mixed_types([int, float, int])

# Handle special cases for optimization
if p == 0:
    # If probability is 0, no one will move to the escalator
    print_float(0, 12)
    exit()
if p == 1:
    # If probability is 1, everyone will move (up to time limit)
    print_float(min(n, t), 12)
    exit()

# Initialize Dynamic Programming table
# dp[i][j] = probability of having j people on the escalator after i seconds
dp = init_dp_table([t+1, n+1], 0.0)
dp[0][0] = 1.0  # Initially, 0 people on the escalator with 100% probability

# Fill the DP table
for i in range(1, t+1):
    for j in range(n+1):
        if j == 0:
            # Case: No one on the escalator - the next person didn't move
            dp[i][j] = dp[i-1][j] * (1-p)
        elif j == n:
            # Case: Escalator is full (reached capacity n)
            # This happens if either:
            # 1. It was already full (n people)
            # 2. It had n-1 people and one more moved
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1] * p
        else:
            # General case:
            # 1. Had j people and next person didn't move
            stay_prob = dp[i-1][j] * (1-p)
            # 2. Had j-1 people and next person moved
            move_prob = dp[i-1][j-1] * p
            dp[i][j] = stay_prob + move_prob

# Calculate expected value (the average number of people on the escalator)
result = sum(j * dp[t][j] for j in range(n+1))

# Output result with required precision
print_float(result, 12)