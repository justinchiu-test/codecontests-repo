#!/usr/bin/env python3

from library import read_int, read_ints, xor_prefix_array

def solve():
    n = read_int()
    a = read_ints()
    
    # Calculate prefix XOR array
    pref = xor_prefix_array(a)
    
    # Using a dictionary to count occurrences for even and odd positions
    dp = [{}, {}]
    ans = 0
    
    for i in range(len(pref)):
        # Get the current XOR value and index parity
        current_xor = pref[i]
        parity = i % 2
        
        # Add to answer if we've seen this XOR with the same parity before
        if current_xor in dp[parity]:
            ans += dp[parity][current_xor]
        
        # Increment the count for this XOR value with current parity
        dp[parity][current_xor] = dp[parity].get(current_xor, 0) + 1
    
    print(ans)

if __name__ == '__main__':
    solve()