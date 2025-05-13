#!/usr/bin/env python3

from library import read_int, is_prime, mod_pow

n = read_int()

# Special cases
if n == 1:
    print('YES')
    print('1')
    exit(0)
    
if n == 4:
    print('YES')
    print('1')
    print('3')
    print('2')
    print('4')
    exit(0)

# Check if n is prime
if not is_prime(n):
    print('NO')
    exit(0)

# Generate the sequence for prime n
print('YES')
print(1)  # First element is always 1

# Generate the rest of the sequence
for j in range(2, n):
    # Calculate j * (j-1)^(n-2) % n
    result = (j * mod_pow(j - 1, n - 2, n)) % n
    print(result)

print(n)  # Last element is always n