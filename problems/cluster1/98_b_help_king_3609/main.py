#!/usr/bin/env python3

from fractions import Fraction
from library import read_int

def solve():
    n = read_int()
    L = 0
    
    # Count powers of 2 that divide n
    while n % 2 == 0:
        n //= 2
        L += 1
    
    # Special case: If n becomes 1 after removing all powers of 2
    if n == 1:
        print(f"{L}/1")
        return
    
    # Find cycle length in modular arithmetic
    s = 1  # 2^0
    t = 1  # 2^0 mod n
    
    for i in range(n):
        t = (t * 2) % n
        s *= 2
        if t == 1:
            m = i + 1
            break
    
    # Calculate the result as a fraction
    r = s
    t = s * n
    i = L
    ans = 0
    
    while r > 1:
        i += 1
        t //= 2
        if r - t > 0:
            r = r - t
            ans = ans + i * t
    
    # Compute final result
    result = (Fraction(ans, s) + Fraction(m, s)) / (1 - Fraction(1, s))
    print(result)

if __name__ == "__main__":
    solve()