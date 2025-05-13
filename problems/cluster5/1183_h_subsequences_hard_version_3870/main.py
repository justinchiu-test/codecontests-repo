#!/usr/bin/env python3

import sys
sys.path.append('..')
from library import char_to_idx, rinput

def solve_subsequences(n, k, s):
    """
    Solve the subsequences problem.
    
    Args:
        n: Length of the string
        k: Number of subsequences required
        s: The input string
        
    Returns:
        Minimum number of characters to delete, or -1 if impossible
    """
    # dp[i][j] will store the number of subsequences of length i ending with character j
    dp = [[0] * 26 for i in range(n + 1)]
    
    # Base case: there's one empty subsequence
    dp[0][0] = 1
    
    # Fill the dp table
    for ch in s:
        j = char_to_idx(ch)
        for i in range(n, 0, -1):
            # The number of subsequences of length i ending with ch is equal to
            # the sum of all subsequences of length i-1
            dp[i][j] = sum(dp[i - 1])
    
    # Compute the answer
    subsequences_count = 0
    subsequences_length_sum = 0
    
    # Iterate from longest to shortest subsequences
    for i in range(n, -1, -1):
        current_count = sum(dp[i])
        
        # If adding these subsequences would exceed k, we've found our answer
        if subsequences_count + current_count >= k:
            # Calculate total deletions needed:
            # k*n - subsequences_length_sum - (k - subsequences_count) * i
            return k * n - subsequences_length_sum - (k - subsequences_count) * i
        
        subsequences_count += current_count
        subsequences_length_sum += i * current_count
    
    # If we can't find k distinct subsequences
    return -1

def main():
    n, k = rinput()
    s = input().strip()
    print(solve_subsequences(n, k, s))

if __name__ == "__main__":
    main()