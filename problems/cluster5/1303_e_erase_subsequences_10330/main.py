#!/usr/bin/env python3
from library import *
# by the authority of GOD     author: manhar singh sachdev #

from math import inf,isinf

def solve(s,t):
    if len(t) == 1:
        if s.count(t[0]):
            return 'YES'
        return 'NO'
    for i in range(1,len(t)):
        dp = [[-inf]*(i+1) for _ in range(len(s)+1)]
        dp[0][0] = 0
        for j in range(len(s)):
            dp[j+1] = dp[j][:]
            for k in range(i+1):
                if k != i and s[j] == t[k]:
                    dp[j+1][k+1] = max(dp[j+1][k+1],dp[j][k])
                if dp[j][k]+i != len(t) and not isinf(dp[j][k]) and s[j] == t[dp[j][k]+i]:
                    dp[j+1][k] = max(dp[j+1][k],dp[j][k]+1)
        # print(*dp,sep='\n')
        # print('-----')
        for l in range(len(s)+1):
            if dp[l][-1] == len(t)-i:
                return 'YES'
    return 'NO'

def main():
    for _ in range(int(input())):
        s = input().strip()
        t = input().strip()
        print(solve(s, t))

if __name__ == '__main__':
    main()
