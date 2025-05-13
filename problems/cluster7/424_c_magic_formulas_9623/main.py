#!/usr/bin/env python3

from library import fast_int, fast_int_list, xor_list

n = fast_int()
arr = fast_int_list()

# Calculate prefix XOR values
dp = [0]
prefix_xor = 0
for i in range(1, n+1):
    prefix_xor ^= i
    dp.append(prefix_xor)

ans = 0
for i in range(1, n+1):
    # Calculate the XOR based on the formula
    value = arr[i-1] ^ (dp[i-1] * ((n//i) % 2)) ^ dp[n % i]
    ans ^= value

print(ans)