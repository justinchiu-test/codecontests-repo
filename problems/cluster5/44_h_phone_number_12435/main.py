#!/usr/bin/env python3

from library import read_str, create_dp_table

def phone_number():
    """
    Solution for the Phone Number problem.

    We use dynamic programming to count all possible phone numbers that
    can be derived using Masha's arithmancy rules.
    """
    # Read Masha's phone number
    masha_number = read_str()
    n = len(masha_number)

    # Create a DP table where:
    # dp[i][j] = number of ways to construct first i+1 digits
    # with the last digit being j
    dp = create_dp_table(n, 10)

    # For the first position, all digits from 0-9 are possible as starting digit
    for digit in range(10):
        dp[0][digit] = 1

    # Fill the DP table for each position
    for i in range(n - 1):
        for current_digit in range(10):
            if dp[i][current_digit] > 0:
                # Calculate possible values for the next digit
                # These are the two possible roundings of the half sum
                next_digit_floor = (int(masha_number[i + 1]) + current_digit) // 2
                next_digit_ceil = (int(masha_number[i + 1]) + current_digit + 1) // 2

                # Add the contribution from current state to next states
                if next_digit_floor != next_digit_ceil:
                    # Both roundings are different, so we have two choices
                    dp[i + 1][next_digit_floor] += dp[i][current_digit]
                    dp[i + 1][next_digit_ceil] += dp[i][current_digit]
                else:
                    # Only one possible value
                    dp[i + 1][next_digit_floor] += dp[i][current_digit]

    # Sum up all possible ways to form the complete number
    total_phone_numbers = sum(dp[n - 1])

    # Check if Masha's own number is among the possibilities
    is_self_number = False
    current_digit = int(masha_number[0])
    formed_number = [masha_number[0]]

    # Try to reconstruct Masha's number using the rules
    for i in range(1, n):
        next_digit_floor = (current_digit + int(masha_number[i])) // 2
        next_digit_ceil = (current_digit + int(masha_number[i]) + 1) // 2

        # Check if Masha's digit at position i matches one of the possible roundings
        if int(masha_number[i]) == next_digit_floor:
            formed_number.append(masha_number[i])
            current_digit = next_digit_floor
        elif int(masha_number[i]) == next_digit_ceil:
            formed_number.append(masha_number[i])
            current_digit = next_digit_ceil
        else:
            # Not possible to form Masha's number
            break

    # Check if we fully reconstructed Masha's number
    if "".join(formed_number) == masha_number:
        is_self_number = True

    # Subtract 1 if Masha's own number is among the possibilities
    return total_phone_numbers - (1 if is_self_number else 0)

print(phone_number())