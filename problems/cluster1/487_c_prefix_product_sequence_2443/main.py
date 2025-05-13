#!/usr/bin/env python3

from library import read_int, is_prime, mod_pow, prefix_product_sequence

n = read_int()

# This problem has solutions for:
# 1. n = 1 (trivial case)
# 2. n = 4 (special case)
# 3. n is prime (can be constructed)

if n == 1:
    print('YES')
    print(1)
elif n == 4:
    print('YES')
    print(1)
    print(3)
    print(2)
    print(4)
elif is_prime(n):
    print('YES')
    print(1)
    for j in range(2, n):
        # Calculate j * (j-1)^(n-2) % n
        inverse = mod_pow(j - 1, n - 2, n)
        print((j * inverse) % n)
    print(n)
else:
    print('NO')