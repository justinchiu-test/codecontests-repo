#!/usr/bin/env python3

from library import read_int, gcd

def print_fraction(a, b):
    """Print a fraction in the format 'a/b'"""
    print(f"{int(a)}/{int(b)}")

def solve(n):
    # Count powers of 2 in n
    pre = 0
    while n > 1 and (n % 2 == 0):
        pre += 1
        n //= 2
    
    # Special case: If n becomes 1 after removing all powers of 2
    if n == 1:
        print_fraction(pre, 1)
        return
    
    # Find the binary representation of 1/n and the cycle length
    arr = []
    rem = 1
    
    while True:
        rem = rem * 2
        arr.append(int(rem // n))
        rem = rem % n
        if rem == 1:
            break
    
    # Calculate the result using the cycle of binary representation
    k = len(arr)
    ans = 0
    
    for i in range(k):
        if arr[i] == 1:
            ans = ans + (2 ** (k - 1 - i)) * (i + 1)
    
    ans = ans * n + k
    
    # Convert to a proper fraction
    numerator = ans
    denominator = (2**k) - 1
    
    # Reduce the fraction
    g = gcd(numerator, denominator)
    numerator //= g
    denominator //= g
    
    # Add the powers of 2 to the final result
    print_fraction(numerator + denominator * pre, denominator)

if __name__ == "__main__":
    n = read_int()
    solve(n)