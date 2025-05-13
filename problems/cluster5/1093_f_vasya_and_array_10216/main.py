#!/usr/bin/env python3

from library import read_int_tuple, read_ints, create_dp_table, create_array, mod_add, mod_sub, MOD_998_244_353

def vasya_and_array():
    # Read input
    n, k, length = read_int_tuple()

    # Edge case: if length is 1, no sequence can be good (always len consecutive equal numbers)
    if length == 1:
        return 0

    # Read the array and add a dummy element at index 0 to use 1-indexing
    arr = read_ints()
    arr.insert(0, 0)

    # Create DP tables
    dp = create_dp_table(n + 1, k + 1)
    sum_dp = create_array(n + 1)
    count = create_array(k + 1)

    # Initialize base case
    sum_dp[0] = 1

    # Fill DP tables
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # We can replace with j only if arr[i] is -1 or already j
            if arr[i] == -1 or arr[i] == j:
                # Ways to reach here with j = ways to reach previous position with any value
                dp[i][j] = sum_dp[i - 1]

                # Increment count of consecutive j's
                count[j] += 1

                # If we have 'length' or more consecutive j's, subtract invalid combinations
                if count[j] >= length:
                    # Subtract ways that would lead to 'length' consecutive j's
                    dp[i][j] = mod_sub(dp[i][j], mod_sub(sum_dp[i - length], dp[i - length][j], MOD_998_244_353), MOD_998_244_353)

                # Update dp and sum_dp with modular arithmetic
                dp[i][j] %= MOD_998_244_353
                sum_dp[i] = mod_add(sum_dp[i], dp[i][j], MOD_998_244_353)
            else:
                # Reset count for this value if we can't use j here
                count[j] = 0

    # Return total ways
    return sum_dp[n]

print(vasya_and_array())