#!/usr/bin/env python3

import sys
sys.path.append('..')
from library import rinput

def count_arrangements(n1, n2, k1, k2, modulo=100000000):
    """
    Count the number of beautiful arrangements of Caesar's legions.
    
    Args:
        n1: Number of footmen
        n2: Number of horsemen
        k1: Maximum consecutive footmen
        k2: Maximum consecutive horsemen
        modulo: Modulo value
        
    Returns:
        Number of beautiful arrangements modulo 10^8
    """
    k1 = min(k1, n1)
    k2 = min(k2, n2)
    
    # dp[i][j][0] = ways to arrange i footmen and j horsemen ending with a footman
    # dp[i][j][1] = ways to arrange i footmen and j horsemen ending with a horseman
    dp = [[[0] * 2 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    
    # Base cases: ways to arrange i footmen and 0 horsemen ending with a footman
    for i in range(1, k1 + 1):
        dp[i][0][0] = 1
    
    # Base cases: ways to arrange 0 footmen and j horsemen ending with a horseman
    for j in range(1, k2 + 1):
        dp[0][j][1] = 1
    
    # Fill the dp table
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            # Ways to end with a footman: combine with previous ways ending with a horseman
            dp[i][j][0] = sum(dp[k][j][1] for k in range(max(0, i - k1), i)) % modulo
            
            # Ways to end with a horseman: combine with previous ways ending with a footman
            dp[i][j][1] = sum(dp[i][k][0] for k in range(max(0, j - k2), j)) % modulo
    
    # Total ways is the sum of arrangements ending with either type
    return sum(dp[n1][n2]) % modulo

def main():
    n1, n2, k1, k2 = rinput()
    print(count_arrangements(n1, n2, k1, k2))

if __name__ == "__main__":
    main()