#!/usr/bin/env python3

from library import read_int

n = read_int()
result = n + 1  # Start with n + 1 (accounting for divisor 1)

i = 2
sqrt_n = int(n**0.5)
while i <= sqrt_n:
    if n % i == 0:
        result += n // i  # Add the divisor
        n //= i  # Reduce n
        sqrt_n = int(n**0.5)  # Recalculate sqrt
        i = 1  # Reset i to try the same factor again
    i += 1

print(result)