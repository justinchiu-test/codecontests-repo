#!/usr/bin/env python3

from library import initialize_dp_table

def main():
    # Read the input phone number
    phone_number = input().strip()
    n = len(phone_number)
    
    # Initialize DP table: dp[i][j] is the number of ways to reach 
    # the ith digit with last digit j
    dp = initialize_dp_table([n, 10], 0)
    
    # Base case: all digits are possible for the first position
    for i in range(10):
        dp[0][i] = 1
    
    # Fill the DP table
    for i in range(n - 1):
        for j in range(10):
            if dp[i][j] != 0:
                # The next digit is determined by rounding (j + a[i+1])/2
                # either down or up
                c = (int(phone_number[i + 1]) + j) // 2
                d = (int(phone_number[i + 1]) + j + 1) // 2
                
                if c != d:
                    # Both roundings lead to different digits
                    dp[i + 1][c] += dp[i][j]
                    dp[i + 1][d] += dp[i][j]
                else:
                    # Both roundings lead to the same digit
                    dp[i + 1][c] += dp[i][j]
    
    # Sum all ways to generate the phone number
    total_ways = sum(dp[n - 1])
    
    # Check if the original phone number is a valid case
    # We need to subtract it from the count if it is
    is_original_valid = 1
    
    # Check the original number by simulating the process
    c = int(phone_number[0])
    reconstructed = [phone_number[0]]
    
    for i in range(1, n):
        # Calculate the two possible next digits
        d = (c + int(phone_number[i])) // 2
        e = (c + int(phone_number[i]) + 1) // 2
        
        # If current digit in original number matches either option, continue
        if int(phone_number[i]) == d:
            reconstructed.append(phone_number[i])
            c = d
        elif int(phone_number[i]) == e:
            reconstructed.append(phone_number[i])
            c = e
        else:
            # Original number is not a valid sequence
            is_original_valid = 0
            break
    
    # Check if we reconstructed the entire number
    if "".join(reconstructed) != phone_number:
        is_original_valid = 0
    
    # Print the result (total ways minus the original if it's valid)
    print(total_ways - is_original_valid)

if __name__ == "__main__":
    main()