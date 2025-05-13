#!/usr/bin/env python3

from library import read_int, read_ints, xor_range

def solve():
    n = read_int()
    arr = read_ints()
    
    # Calculate prefix XOR values
    # dp[i] represents XOR of numbers from 1 to i
    dp = [0]
    prefix = 0
    for i in range(1, n+1):
        prefix ^= i
        dp.append(prefix)
    
    result = 0
    for i in range(1, n+1):
        # Calculate p_i value according to the formula
        # p_i = a_i XOR (f(i) XOR f(2*i) XOR f(3*i) XOR ... XOR f(floor(n/i)*i))
        # For each multiple of i, the value is the same, so we need to count occurrences
        
        # For numbers 1*i, 2*i, 3*i, ..., (n/i)*i, we calculate their XOR
        # Note that we can use prefix XOR: XOR of [1..k*i] XOR XOR of [1..(k-1)*i]
        # But since we need f(i), f(2i), etc., we need the numbers themselves
        # If (n/i) is odd, then XOR of all these numbers is the same as dp[i-1]
        # If (n/i) is even, it's 0
        f_values_xor = dp[i-1] if (n // i) % 2 == 1 else 0
        
        # Remaining terms: f(n%i + 1) XOR f(n%i + 2) XOR ... XOR f(i)
        # This is just dp[n%i]
        remaining_values_xor = dp[n % i]
        
        # Calculate the final value for p_i and XOR with a_i
        p_i = arr[i-1] ^ f_values_xor ^ remaining_values_xor
        result ^= p_i
    
    print(result)

if __name__ == '__main__':
    solve()