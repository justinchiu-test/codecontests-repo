#!/usr/bin/env python3

from library import read_int_tuple

def main():
    n, k = read_int_tuple()
    s = input().strip()
    
    # Initialize DP table: dp[i][j] is the number of subsequences of length i ending with letter j
    dp = [[0] * 26 for i in range(n + 1)]
    dp[0][0] = 1
    
    for ch in s:
        j = ord(ch) - ord('a')
        for i in range(n, 0, -1):
            dp[i][j] = sum(dp[i - 1])
    
    # Calculate the result
    x = 0  # Total count of distinct subsequences seen so far
    y = 0  # Total cost of distinct subsequences seen so far
    
    for i in range(n, -1, -1):
        if x + sum(dp[i]) >= k:
            print(k * n - y - (k - x) * i)
            break
        x += sum(dp[i])
        y += i * sum(dp[i])
    else:
        print(-1)

if __name__ == '__main__':
    main()