#!/usr/bin/env python3

from library import read_ints, print_float, init_dp_dict, init_dp_table
from collections import defaultdict

# Read input
n, l, k = read_ints()  # n tours, l min tours to win, k - initial bag capacity
probabilities = read_ints()  # Probability of winning each tour (in %)
prizes = read_ints()  # Prize for each tour (-1: huge prize, otherwise: bag capacity)

# Count how many huge prizes we can win
huge_prizes_count = prizes.count(-1)

# Initialize DP state
# dp[(wins, capacity)] = probability of having 'wins' wins and 'capacity' bag capacity
dp = {(0, min(k, huge_prizes_count)): 1.0}

# For tours with huge prizes, track distribution of wins
# huge_prize_distribution[i] = probability of winning exactly i huge prizes
huge_prize_distribution = [1.0] + [0.0] * huge_prizes_count  # Initially, 0 huge prizes with 100% probability

# Process each tour
for tour_idx, (prob, prize) in enumerate(zip(probabilities, prizes)):
    prob /= 100.0  # Convert percentage to probability

    if prize > 0:  # If the prize is a bag (increases capacity)
        # Create a new DP state
        new_dp = init_dp_dict()

        for (wins, capacity), curr_prob in dp.items():
            # Case 1: Don't win this tour - keep same state with reduced probability
            new_dp[(wins, capacity)] += curr_prob * (1 - prob)

            # Case 2: Win this tour - increase wins and capacity
            new_wins = min(l, wins + 1)  # Cap at l since we only need l wins
            new_capacity = min(huge_prizes_count, capacity + prize)  # Cap at max possible huge prizes
            new_dp[(new_wins, new_capacity)] += curr_prob * prob

        dp = new_dp
    else:  # If the prize is a huge prize
        # Update huge prize distribution
        new_distribution = [0.0] * (huge_prizes_count + 1)

        # For each current number of huge prizes
        for i in range(huge_prizes_count + 1):
            if i < huge_prizes_count:
                # Win the tour and get a huge prize
                new_distribution[i+1] += huge_prize_distribution[i] * prob

            # Lose the tour, keep same number of huge prizes
            new_distribution[i] += huge_prize_distribution[i] * (1 - prob)

        huge_prize_distribution = new_distribution

# Calculate final answer
# For each dp state, check if we can fit all huge prizes and have enough wins
result_dp = init_dp_table([n - huge_prizes_count + 1, huge_prizes_count + 1], 0.0)

# Copy probabilities from dp dictionary to result_dp array
for (wins, capacity), prob in dp.items():
    if wins + capacity >= l:  # If we have enough wins (direct wins + capacity to store huge prizes)
        result_dp[wins][capacity] = prob

# Accumulate probabilities for capacity (having more capacity means we can handle fewer huge prizes too)
for wins in range(n - huge_prizes_count, -1, -1):
    for capacity in range(huge_prizes_count, 0, -1):
        result_dp[wins][capacity - 1] += result_dp[wins][capacity]

# Accumulate probabilities for wins (having more wins means we need fewer huge prizes)
for wins in range(n - huge_prizes_count, 0, -1):
    for capacity in range(huge_prizes_count, -1, -1):
        result_dp[wins - 1][capacity] += result_dp[wins][capacity]

# Combine with huge prize distribution to get final probability
final_probability = 0.0
for huge_prize_count, prob in enumerate(huge_prize_distribution):
    if huge_prize_count > 0 and l - huge_prize_count <= n - huge_prizes_count:
        # If we have huge_prize_count huge prizes, we need (l - huge_prize_count) normal wins
        final_probability += result_dp[max(0, l - huge_prize_count)][huge_prize_count] * prob
    elif huge_prize_count == 0 and l <= n - huge_prizes_count:
        # Special case for 0 huge prizes
        final_probability += result_dp[l][0] * prob

print_float(final_probability, 7)