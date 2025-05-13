#!/usr/bin/env python3

from library import read_int_tuple, read_ints, create_dp_table, mod_add, MOD_998_244_353

def array_beauty():
    # Read input
    n, k = read_int_tuple()
    arr = read_ints()

    # Sort the array and add a dummy element at index 0 for 1-indexing
    arr = [0] + sorted(arr)

    # Initialize answer
    total_beauty = 0

    # Create DP table
    # f[i][j] = number of ways to choose i elements with the last element being arr[j]
    # with minimum difference between elements being at least x
    dp = create_dp_table(k + 10, n + 10)

    # We iterate through all possible beauty values
    # The maximum possible beauty is (A[n] - A[1]) / (k - 1)
    max_possible_beauty = (arr[n] - arr[1]) // (k - 1) + 1

    for x in range(1, max_possible_beauty):
        # Base case: for subsequences of length 1, we can choose any single element
        for i in range(1, n + 1):
            dp[1][i] = 1

        # Fill DP table for subsequences of length 2 to k
        for seq_len in range(2, k + 1):
            current_sum = 0
            prefix = 1  # Keep track of the index of the previous element

            for current_idx in range(1, n + 1):
                # Find all previous elements that can be paired with the current element
                # while maintaining the beauty requirement (minimum difference ≥ x)
                while prefix <= n and arr[prefix] + x <= arr[current_idx]:
                    current_sum = mod_add(current_sum, dp[seq_len - 1][prefix], MOD_998_244_353)
                    prefix += 1

                # Update DP state
                dp[seq_len][current_idx] = current_sum

        # Sum up the contribution of this beauty value
        for i in range(1, n + 1):
            total_beauty = mod_add(total_beauty, dp[k][i], MOD_998_244_353)

    return total_beauty

print(array_beauty())
