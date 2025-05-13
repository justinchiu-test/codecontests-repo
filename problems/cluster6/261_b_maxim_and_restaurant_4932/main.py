#!/usr/bin/env python3

from library import read_int, read_ints
import math

n = read_int()
a = read_ints()
p = read_int()

# Calculate total time
total_time = sum(a)

# If the total time is less than or equal to p, Maxim can eat everything
if total_time <= p:
    print("{:.10f}".format(n))
else:
    ans = 0
    # Try each dish as the last one
    for i in range(n):
        # dp[j][k][z] = number of ways to choose k dishes from first j dishes with total time z
        dp = [[[0 for z in range(55)] for y in range(55)] for x in range(55)]
        dp[0][0][0] = 1
        
        for j in range(n):
            if j == i:
                # Skip the dish i (it will be the last one)
                for k in range(n):
                    for z in range(p+1):
                        dp[j+1][k][z] = dp[j][k][z]
                continue
            
            for k in range(n):
                for z in range(p+1):
                    # Skip current dish
                    dp[j+1][k][z] += dp[j][k][z]
                    
                    # Include current dish if it fits
                    if z + a[j] <= p:
                        dp[j+1][k+1][z+a[j]] += dp[j][k][z]
        
        # Calculate the number of ways Maxim is the last to finish
        for k in range(n):
            for z in range(p+1):
                if z + a[i] > p:
                    # Maxim can't add his dish, so k people are in the restaurant
                    ans += k * dp[n][k][z] * math.factorial(k) * math.factorial(n-k-1)
    
    # Calculate the probability and format with 10 decimal places
    print("{:.10f}".format(ans / math.factorial(n)))