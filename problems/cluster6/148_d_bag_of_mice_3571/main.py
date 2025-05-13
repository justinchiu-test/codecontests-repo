#!/usr/bin/env python3

from library import read_ints, DP

w, b = read_ints()

# Create a dp table for probabilities
p = DP.create_dp_table([w+1, b+1])

# Base case: if there are no black mice, princess always wins
for i in range(1, w+1):
    p[i][0] = 1

# Fill the dp table
for i in range(1, w+1):
    for j in range(1, b+1):
        # Probability of drawing a white mouse directly
        p[i][j] = i / (i + j)
        
        # Dragon draws, then princess draws
        if j >= 3:
            # Dragon draws black, another black, then princess draws white
            p[i][j] += (j/(i+j)) * ((j-1)/(i+j-1)) * ((j-2)/(i+j-2)) * p[i][j-3]
        
        if j >= 2:
            # Dragon draws black, another black, then princess draws white
            p[i][j] += (j/(i+j)) * ((j-1)/(i+j-1)) * ((i)/(i+j-2)) * p[i-1][j-2]

print("%.9f" % p[w][b])