#!/usr/bin/env python3

from math import gcd
from itertools import islice
def get_all(n):
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if gcd(i, j) == 1: yield i, j

def solve(n, m):
    x = list(islice(get_all(n), m))
    if len(x) == m >= n - 1:
        return x

res = solve(*map(int, input().split()))
if res is not None:
    print('Possible')
    for e in res: print(*e)
else:
    print('Impossible')
