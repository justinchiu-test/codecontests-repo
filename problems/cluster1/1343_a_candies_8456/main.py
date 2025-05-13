#!/usr/bin/env python3

from library import read_int

t = read_int()
for _ in range(t):
    n = read_int()
    
    # Find the smallest k where n is divisible by (2^k - 1)
    for k in range(2, 31):  # 2^30 is around 10^9, sufficient for the constraints
        divisor = (1 << k) - 1  # 2^k - 1
        if n % divisor == 0:
            print(n // divisor)
            break