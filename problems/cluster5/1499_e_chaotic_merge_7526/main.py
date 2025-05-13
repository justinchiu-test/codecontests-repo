#!/usr/bin/env python3

from library import setup_fast_io, mod_add

# Setup fast IO
input = setup_fast_io()

# Prime modulus for this problem (different from standard MOD)
MOD = 998244353

def main():
    x = input()
    x = list(x)
    y = input()
    y = list(y)
    
    # Convert to integers (0-25 for a-z)
    x = list(map(lambda ch: ord(ch) - 97, x))
    y = list(map(lambda ch: ord(ch) - 97, y))
    
    ans = 0
    m, n = len(x), len(y)
    
    # Calculate consecutive distinct characters
    v1 = [1] * (m + 1)
    v2 = [1] * (n + 1)
    
    for i in range(m - 2, -1, -1):
        if x[i] != x[i + 1]:
            v1[i] += v1[i + 1]
    
    for i in range(n - 2, -1, -1):
        if y[i] != y[i + 1]:
            v2[i] += v2[i + 1]
    
    # DP[i][j][k] = number of beautiful strings starting with x[i] from x and y[j] from y
    # with previous character k
    dp = [[[0] * 27 for j in range(n + 1)] for i in range(m + 1)]
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            for k in range(27):
                if x[i] == k:
                    if y[j] != k:
                        dp[i][j][k] = (dp[i][j + 1][y[j]] + v1[i]) % MOD
                elif y[j] == k:
                    dp[i][j][k] = (dp[i + 1][j][x[i]] + v2[j]) % MOD
                else:
                    # Use mod_add for cleaner code
                    temp = mod_add(dp[i + 1][j][x[i]], dp[i][j + 1][y[j]], MOD)
                    if x[i] != y[j]:
                        temp = mod_add(temp, v2[j] + v1[i], MOD)
                    dp[i][j][k] = temp
    
    # Sum up all possibilities
    for i in range(m):
        for j in range(n):
            ans = mod_add(ans, dp[i][j][26], MOD)
    
    print(ans)

if __name__ == '__main__':
    main()