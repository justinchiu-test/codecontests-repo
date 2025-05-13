#!/usr/bin/env python3

from library import read_ints, gcd

def factor_count(n, k):
    """Count how many times k divides n"""
    count = 0
    while n % k == 0:
        count += 1
        n //= k
    return count, n

a, b = read_ints()

if a == b:
    print(0)
    exit()

# Get GCD to check if they can be made equal
common = gcd(a, b)
a //= common
b //= common

# Check factors of 2, 3, 5
a_2, a = factor_count(a, 2)
a_3, a = factor_count(a, 3)
a_5, a = factor_count(a, 5)

b_2, b = factor_count(b, 2)
b_3, b = factor_count(b, 3)
b_5, b = factor_count(b, 5)

# If there are other factors, it's impossible
if a != 1 or b != 1:
    print(-1)
else:
    # Calculate total operations needed
    print(abs(a_2 - b_2) + abs(a_3 - b_3) + abs(a_5 - b_5))