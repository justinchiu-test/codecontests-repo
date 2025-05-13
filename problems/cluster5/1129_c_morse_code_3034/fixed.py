#!/usr/bin/env python3

import os, sys
sys.path.append("/home/justinchiu_cohere_com/codecontests-repo/problems/cluster5")
from library import z_function

def main():
    # Parse input
    nums = list(map(int, input().split()))
    
    MOD = 10 ** 9 + 7
    # The four patterns that don't correspond to any English letter
    BAD_TUPLES = {(0, 0, 1, 1), (0, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)}
    
    n = nums[0]
    s = []
    ans = []
    
    for i in range(1, n + 1):
        s.append(nums[i])
        
        # Initialize DP array where f[j] = number of valid Morse code sequences ending at position j
        f = [0] * (i + 1)
        f[i] = 1  # Base case: empty string at position i
        
        # Fill the DP array from right to left
        for j in range(i - 1, -1, -1):
            # Try all possible Morse code lengths (1 to 4)
            for k in range(j, min(j + 4, i)):
                # Check if current substring is a valid Morse code (not in BAD set)
                if tuple(s[j:k + 1]) not in BAD_TUPLES:
                    f[j] = (f[j] + f[k + 1]) % MOD
        
        # Calculate Z-function on the reversed string to find longest suffix that's also a prefix
        z = z_function(s[::-1])
        
        # Determine how many positions to consider for the sum
        # If there's a suffix that's also a prefix, we've counted those sequences before
        new = i + 1
        if len(z) > 0:
            new = i - max(z)
        
        # Calculate sum of valid sequences
        sm = 0
        for j in range(new):
            sm = (sm + f[j]) % MOD
        
        ans.append(sm)
    
    # Print results
    print(*ans, sep='\n')

if __name__ == "__main__":
    main()