#!/usr/bin/env python3

from library import read_str, create_dp_table
import math

def main():
    a = read_str()  # The newspaper headline
    b = read_str()  # Target text to form
    na = len(a)
    nb = len(b)
    
    # dp[i][j] stores the next position of character 'a'-'z' starting from position i
    dp = [[-1 for _ in range(26)] for _ in range(na+1)]
    
    # Precompute the next occurrence of each character
    for i in range(na - 1, -1, -1):
        # Copy previous positions
        for j in range(26):
            dp[i][j] = dp[i+1][j]
        # Update with current character position
        dp[i][ord(a[i]) - 97] = i
    
    cp = 0  # Current position in headline
    ans = 1  # Number of times we need to use the headline
    i = 0    # Current position in target text
    
    while i < nb:
        # If we've reached the end of the headline, we need to start over
        if cp == na:
            ans += 1
            cp = 0
        
        # Find next occurrence of the current character
        char_idx = ord(b[i]) - 97
        if dp[cp][char_idx] == -1:  # Character not found in remaining headline
            ans += 1  # Start over with a new headline
            cp = 0
            # If still not found after restarting, it's impossible
            if dp[cp][char_idx] == -1:
                ans = math.inf
                break
        
        # Move to the next position after the found character
        cp = dp[cp][char_idx] + 1
        i += 1
    
    print(ans if ans != math.inf else -1)

if __name__ == "__main__":
    main()