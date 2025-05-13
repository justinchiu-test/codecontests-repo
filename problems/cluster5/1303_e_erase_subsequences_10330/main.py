#!/usr/bin/env python3

from library import read_int, read_str
from math import inf, isinf

def solve(s: str, t: str) -> str:
    """
    Check if string t can be built from string s by erasing at most two subsequences.
    
    Args:
        s: The source string
        t: The target string to build
        
    Returns:
        'YES' if t can be built from s, 'NO' otherwise
    """
    # Special case: if t has only one character
    if len(t) == 1:
        return 'YES' if t[0] in s else 'NO'
    
    # For each possible split of t into two parts
    for i in range(1, len(t)):
        # dp[j][k] = how many characters from the second part of t we've matched
        # after processing j characters from s and k characters from the first part of t
        dp = [[-inf] * (i + 1) for _ in range(len(s) + 1)]
        dp[0][0] = 0  # Base case: no characters processed
        
        # Fill the DP table
        for j in range(len(s)):
            # Copy the previous state
            dp[j + 1] = dp[j][:]
            
            for k in range(i + 1):
                # If current character matches with next character in first part of t
                if k != i and s[j] == t[k]:
                    dp[j + 1][k + 1] = max(dp[j + 1][k + 1], dp[j][k])
                
                # If current character matches with next character in second part of t
                if dp[j][k] + i != len(t) and not isinf(dp[j][k]) and s[j] == t[dp[j][k] + i]:
                    dp[j + 1][k] = max(dp[j + 1][k], dp[j][k] + 1)
        
        # Check if we can match all characters from both parts
        for l in range(len(s) + 1):
            if dp[l][-1] == len(t) - i:
                return 'YES'
    
    return 'NO'

def main():
    # Process each test case
    for _ in range(read_int()):
        s = read_str()
        t = read_str()
        print(solve(s, t))

if __name__ == '__main__':
    main()