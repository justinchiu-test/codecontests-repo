#!/usr/bin/env python3

from library import read_str, read_strs, read_int_tuple

def three_religions():
    # Read input
    n, q = read_int_tuple()
    universe = '!' + read_str()  # Add dummy character for 1-indexing

    # Precompute next occurrence positions for each character
    # nxt[c][i] = position of next occurrence of character c after position i
    alphabet_size = 26
    next_pos = [[n + 1] * (n + 2) for _ in range(alphabet_size)]

    # Fill next_pos table from right to left
    for i in range(n - 1, -1, -1):
        char_idx = ord(universe[i + 1]) - ord('a')
        for j in range(alphabet_size):
            next_pos[j][i] = next_pos[j][i + 1]
        next_pos[char_idx][i] = i + 1

    # Initialize religion descriptions with a dummy character
    religions = [[-1], [-1], [-1]]

    # Function to calculate unique index for 3D DP state
    # This is a space optimization technique to use a 1D array for 3D DP
    def get_index(i, j, k):
        return i * 65536 + j * 256 + k

    # Initialize DP array (flat representation of 3D DP)
    max_religion_len = 256
    dp_size = max_religion_len * max_religion_len * max_religion_len
    dp = [0] * dp_size

    # Update DP table after a religion change
    def update_dp(fixed_religion=None):
        # Determine ranges to process based on whether we're updating for a specific religion
        ranges = list(map(range, (len(religions[0]), len(religions[1]), len(religions[2]))))
        if fixed_religion is not None:
            # If we only need to update for one religion, limit the range to just the last entry
            ranges[fixed_religion] = range(len(religions[fixed_religion]) - 1, len(religions[fixed_religion]))

        # Update DP values
        for i in ranges[0]:
            for j in ranges[1]:
                for k in ranges[2]:
                    # Calculate next position for each religion
                    if i == j == k == 0:
                        dp[get_index(i, j, k)] = 0
                        continue

                    # Take the minimum next position for the three religions
                    dp[get_index(i, j, k)] = min(
                        next_pos[religions[0][i]][dp[get_index(i - 1, j, k)]] if i else n + 1,
                        next_pos[religions[1][j]][dp[get_index(i, j - 1, k)]] if j else n + 1,
                        next_pos[religions[2][k]][dp[get_index(i, j, k - 1)]] if k else n + 1
                    )

    # Process each evolution query
    results = []
    for _ in range(q):
        query = read_strs()
        operation = query[0]

        if operation == '+':
            # Add a character to a religion
            religion_idx = int(query[1]) - 1  # Convert to 0-indexed
            char_idx = ord(query[2]) - ord('a')
            religions[religion_idx].append(char_idx)
            # Update only the affected religion for efficiency
            update_dp(religion_idx)
        else:
            # Remove the last character from a religion
            religion_idx = int(query[1]) - 1  # Convert to 0-indexed
            religions[religion_idx].pop()

        # Check if the three religions can coexist
        # Get the final state of the DP
        final_state = dp[get_index(len(religions[0]) - 1, len(religions[1]) - 1, len(religions[2]) - 1)]
        results.append("YES" if final_state <= n else "NO")

    # Print results
    return '\n'.join(results)

print(three_religions())