#!/usr/bin/env python3

from library import get_int, is_prime, power_mod

n = get_int()

# Special cases
if n == 1:
    print('YES')
    print(1)
    exit(0)
if n == 4:
    print('YES')
    print(1)
    print(3)
    print(2)
    print(4)
    exit(0)

# Check if n is prime
if not is_prime(n):
    print('NO')
    exit(0)

# If n is prime, construct the sequence
print('YES')
print(1)  # First element is always 1
for j in range(2, n):
    # Calculate j * (j-1)^(n-2) mod n
    print(j * power_mod(j - 1, n - 2, n) % n)
print(n)  # Last element is always n