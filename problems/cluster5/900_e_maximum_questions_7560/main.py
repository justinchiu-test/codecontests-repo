#!/usr/bin/env python3

from library import read_int, read_str

def main():
    # Read input
    n = read_int()
    s = read_str()
    m = read_int()
    
    # Initialize arrays to store counts of characters at even/odd positions
    # a[i] counts 'a's at odd positions up to index i
    # b[i] counts 'b's at even positions up to index i
    # q[i] counts '?' characters up to index i
    a = [0] * (n + 2)  # 'a' counts
    b = [0] * (n + 2)  # 'b' counts
    q = [0] * (n + 1)  # '?' counts
    
    # Dynamic programming state: (t, r) where
    # t is a parameter used for comparison (smaller is better)
    # r is the number of replacements needed
    dp = [(0, 0)] * (n + 2)
    
    # Precompute counts
    for i in range(0, n):
        # Count 'b's at even positions
        b[i] = b[i-2] + (s[i] == 'b')
        # Count 'a's at odd positions
        a[i] = a[i-2] + (s[i] == 'a')
        # Count '?' characters
        q[i] = q[i-1] + (s[i] == '?')
    
    # DP approach: start from the end and work backwards
    for i in range(n - m, -1, -1):
        # By default, no occurrence of t at position i
        dp[i] = dp[i+1]
        
        # Determine indices for checking depending on the parity of m
        i_b = 1 if m % 2 == 1 else 2  # Index offset for 'b'
        i_a = 1 if m % 2 == 0 else 2  # Index offset for 'a'
        
        # Check if there are no conflicting characters
        # This condition checks if we can make s[i:i+m] match pattern "abab..."
        if not (b[i+m-i_b] - b[i-2] or a[i+m-i_a] - a[i-1]):
            # If we can, calculate the new state
            t, r = dp[i+m]
            # Compare with current state and choose better one
            # (t-1) represents adding one more occurrence of t
            # r+q[i+m-1]-q[i-1] is the number of replacements needed for this segment
            dp[i] = min((t-1, r + q[i+m-1] - q[i-1]), dp[i])
    
    # Print the minimum number of replacements needed
    print(dp[0][1])

if __name__ == "__main__":
    main()