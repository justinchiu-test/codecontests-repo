#!/usr/bin/env python3

from library import read_int_tuple, read_str

def main():
    # Read input
    n, k = read_int_tuple()
    s = read_str()
    
    # Dynamic programming approach to count unique subsequences
    # dp[i][j] = number of unique subsequences of length i ending with character j
    dp = [[0] * 26 for _ in range(n + 1)]
    
    # Base case: empty string is a valid subsequence with length 0
    dp[0][0] = 1
    
    # Fill the DP table
    for ch in s:
        # Convert character to 0-25 index
        j = ord(ch) - ord('a')
        
        # Process from longest to shortest to avoid counting a subsequence multiple times
        for i in range(n, 0, -1):
            # Count of unique subsequences of length i ending with character j
            # is the sum of all unique subsequences of length i-1
            dp[i][j] = sum(dp[i - 1])
    
    # Calculate minimum cost
    total_unique_subseqs = 0  # Number of unique subsequences accumulated so far
    total_cost = 0           # Total cost accumulated so far
    
    # Process from longest to shortest subsequences to minimize cost
    for i in range(n, -1, -1):
        unique_subseqs_length_i = sum(dp[i])  # Number of unique subsequences of length i
        
        # If adding all subsequences of length i would exceed k
        if total_unique_subseqs + unique_subseqs_length_i >= k:
            # Calculate remaining subsequences needed
            remaining = k - total_unique_subseqs
            
            # Cost for each subsequence of length i is (n - i)
            # Add cost for remaining subsequences
            print(total_cost + remaining * (n - i))
            break
        
        # Add all subsequences of length i
        total_unique_subseqs += unique_subseqs_length_i
        # Add cost for all subsequences of length i
        total_cost += unique_subseqs_length_i * (n - i)
    else:
        # If we can't reach k unique subsequences
        print(-1)

if __name__ == "__main__":
    main()