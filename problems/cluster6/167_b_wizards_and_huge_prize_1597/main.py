#!/usr/bin/env python3

from collections import defaultdict
from library import read_ints

# Read input
n, l, initial_bags = read_ints()
probabilities = read_ints()
prizes = read_ints()

# Count the number of tours with huge prizes
huge_prizes_count = prizes.count(-1)

# Initialize DP state for tours with bags
# (k, a): q means having won k tours and having a capacity for a huge prizes with probability q
dp_bags = {(0, min(initial_bags, huge_prizes_count)): 1}

# Initialize DP state for tours with huge prizes
# r[i] is the probability of getting i huge prizes
dp_huge = [1]

# Process each tour
for p, s in zip(probabilities, prizes):
    p /= 100  # Convert percent to probability
    
    if s > 0:  # If prize is a bag
        new_dp = defaultdict(int)
        
        for (k, a), q in dp_bags.items():
            # Case: Don't win this tour
            new_dp[(k, a)] += q - q * p
            
            # Case: Win this tour
            new_capacity = min(huge_prizes_count, a + s)
            new_wins = min(l, k + 1)
            new_dp[(new_wins, new_capacity)] += q * p
        
        dp_bags = new_dp
    else:  # If prize is huge
        # Calculate new huge prize distribution
        win_probs = [0] + [q * p for q in dp_huge]
        lose_probs = [q - q * p for q in dp_huge] + [0]
        dp_huge = [a + b for a, b in zip(win_probs, lose_probs)]

# Calculate final probabilities
result_dp = [[0] * (huge_prizes_count + 1) for _ in range(n - huge_prizes_count + 1)]

# Initialize with valid states from dp_bags
for (k, a), q in dp_bags.items():
    if k + a >= l:  # If we win enough tours
        result_dp[k][a] = q

# Process the DP array
# Propagate probabilities up
for k in range(n - huge_prizes_count, -1, -1):
    for a in range(huge_prizes_count, 0, -1):
        result_dp[k][a - 1] += result_dp[k][a]

for k in range(n - huge_prizes_count, 0, -1):
    for a in range(huge_prizes_count, -1, -1):
        result_dp[k - 1][a] += result_dp[k][a]

# Calculate final answer
answer = 0
for k, p in enumerate(dp_huge):
    if l - k <= n - huge_prizes_count:
        answer += result_dp[max(0, l - k)][k] * p

# Format and print the answer with 7 decimal places
print(f"{answer:.7f}")