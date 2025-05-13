#!/usr/bin/env python3

from library import read_ints, init_dp_table, print_float

# Read the number of white and black mice
w, b = read_ints()

# Initialize DP table
# p[i][j] = probability that Princess wins if there are i white mice and j black mice
p = init_dp_table([w+1, b+1], 0.0)

# Base cases
for i in range(1, w+1):
    p[i][0] = 1.0  # If there are only white mice, Princess wins with 100% probability

# DP recurrence
for i in range(1, w+1):
    for j in range(1, b+1):
        # Case 1: Princess draws a white mouse and wins immediately
        princess_draws_white_prob = i/(i+j)

        # Case 2: Princess draws a black mouse, then Dragon's turn
        princess_draws_black_prob = j/(i+j)

        # Initialize with probability from drawing white
        p[i][j] = princess_draws_white_prob

        # Sub-case 1: Dragon draws black, mouse jumps out black, Princess draws black
        if j >= 3:
            dragon_draws_black_prob = (j-1)/(i+j-1)
            mouse_jumps_black_prob = (j-2)/(i+j-2)
            p[i][j] += princess_draws_black_prob * dragon_draws_black_prob * mouse_jumps_black_prob * p[i][j-3]

        # Sub-case 2: Dragon draws black, mouse jumps out black, Princess draws white
        if j >= 2 and i >= 1:
            dragon_draws_black_prob = (j-1)/(i+j-1)
            mouse_jumps_white_prob = i/(i+j-2)
            p[i][j] += princess_draws_black_prob * dragon_draws_black_prob * mouse_jumps_white_prob * p[i-1][j-2]

# Output the probability of Princess winning
print_float(p[w][b], 9)