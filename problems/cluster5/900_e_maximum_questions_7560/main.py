#!/usr/bin/env python3

from sys import path
path.append('..')
from library import read_int, read_str

def main():
    n = read_int()
    s = read_str()
    m = read_int()
    
    # Precompute counts for 'a', 'b', and '?' characters
    a_count = [0] * (n + 2)  # Count of 'a' characters at odd positions
    b_count = [0] * (n + 2)  # Count of 'b' characters at even positions
    q_count = [0] * (n + 1)  # Count of '?' characters
    
    # Calculate prefix sums
    for i in range(n):
        # Count 'b' at even positions (index%2 == 0)
        b_count[i] = b_count[i-2] + (1 if s[i] == 'b' else 0)
        # Count 'a' at odd positions (index%2 == 1)
        a_count[i] = a_count[i-2] + (1 if s[i] == 'a' else 0)
        # Count '?' characters
        q_count[i] = q_count[i-1] + (1 if s[i] == '?' else 0)
    
    # dp[i] = (most_segments, min_replacements) starting from position i
    dp = [(0, 0)] * (n + 2)
    
    # Bottom-up DP approach
    for i in range(n - m, -1, -1):
        # Default to the result of skipping this position
        dp[i] = dp[i + 1]
        
        # Indices for checking a/b based on parity of m
        i_b = 1 if m % 2 == 1 else 2  # Index offset for 'b' check
        i_a = 1 if m % 2 == 0 else 2  # Index offset for 'a' check
        
        # Check if we can form a valid substring of length m here
        # If there are no conflicting 'a' or 'b' characters
        if not (b_count[i + m - i_b] - b_count[i - 2] or a_count[i + m - i_a] - a_count[i - 1]):
            segments, replacements = dp[i + m]
            # Try to take this segment and update if better
            new_state = (segments + 1, replacements + q_count[i + m - 1] - q_count[i - 1])
            dp[i] = min(new_state, dp[i], key=lambda x: (-x[0], x[1]))
    
    # Return the minimum number of replacements needed
    print(dp[0][1])

if __name__ == "__main__":
    main()