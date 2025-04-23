#!/usr/bin/env python3

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    v = [True] * (3 * n + 1)
    e = [0] * n
    ptr = 0
    for i in range(1, m + 1):
        a, b = map(int, input().split())
        if ptr < n and v[a] and v[b]:
            e[ptr] = i
            ptr += 1
            v[a] = False
            v[b] = False
    if ptr == n:
        print('Matching')
        print(*e)
    else:
        print('IndSet')
        cnt = 0
        for i in range(1, n * 3 + 1):
            if v[i]:
                print(i, end=' ')
                cnt += 1
            if cnt == n:
                print()
                break
