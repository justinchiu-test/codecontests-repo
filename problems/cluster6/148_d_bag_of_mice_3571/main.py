#!/usr/bin/env python3

from library import read_ints

# Read input
w, b = read_ints()

# Initialize DP table: p[i][j] = probability of princess winning with i white mice and j black mice
p = [[0] * (b + 1) for _ in range(w + 1)]

# Base cases:
# If there are white mice but no black mice, princess will always win
for i in range(1, w + 1):
    p[i][0] = 1

# Fill the DP table
for i in range(1, w + 1):
    for j in range(1, b + 1):
        # Princess draws white mouse - she wins
        p[i][j] = i / (i + j)
        
        # Princess draws black mouse, then dragon's turn
        # Case: Dragon draws black mouse, and a mouse jumps out
        if j >= 3:  # Need at least 3 black mice initially for this case
            # (j-1 black mice after princess draws a black one)
            prob_black_out = (j / (i + j)) * ((j - 1) / (i + j - 1)) * ((j - 2) / (i + j - 2))
            p[i][j] += prob_black_out * p[i][j - 3]
        
        # Case: Dragon draws black mouse, and a white mouse jumps out
        if j >= 2 and i >= 1:  # Need at least 2 black mice and 1 white mouse
            prob_white_out = (j / (i + j)) * ((j - 1) / (i + j - 1)) * ((i) / (i + j - 2))
            p[i][j] += prob_white_out * p[i - 1][j - 2]

# Print the result with 9 decimal places
print(f"{p[w][b]:.9f}")