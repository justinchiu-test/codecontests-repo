#!/usr/bin/env python3

from library import read_int, read_str, create_bool_table, create_dp_table

N = 303
n = read_int()
text = read_str()
text_length = len(text)
words = text.split()

# Create boolean table to track equal words
eq = create_bool_table(N, N)
# Create dp table to track length of matching sequences
dp = create_dp_table(N, N)

# Precompute equality between words
for i in range(n):
    eq[i][i] = True
    for j in range(i):
        eq[i][j] = eq[j][i] = words[i] == words[j]

# Fill dynamic programming table for matching sequence lengths
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if eq[i][j]:
            if i < n - 1 and j < n - 1:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = 1

# Calculate minimum length of text after abbreviation
ans = text_length
for i in range(n):
    segment_length = 0
    for j in range(1, n - i + 1):
        # Add length of current word to segment length
        segment_length += len(words[i + j - 1])
        count = 1
        pos = i + j

        # Find non-overlapping identical segments
        while pos < n:
            if dp[i][pos] >= j:
                count += 1
                pos += j - 1
            pos += 1

        # Calculate new text length with abbreviation
        # Formula: total_length - (segment_length * count) + count
        # (remove all segments, add one letter for each)
        new_length = text_length - segment_length * count + count

        # Update answer if multiple segments found and length is shorter
        if count > 1 and ans > new_length:
            ans = new_length

print(ans)
