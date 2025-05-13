#!/usr/bin/env python3

from library import read_ints, read_int_list, gcd, get_all_divisors

def solve_three_horses():
    n, m = read_ints()
    a = read_int_list()
    
    # Calculate the GCD of (a_i - 1) for all a_i
    g = 0
    for x in a:
        g = gcd(g, x - 1)
    
    answer = 0
    
    # Process divisors of g
    def process(x):
        nonlocal answer
        if x % 2 == 0:  # Skip even divisors
            return
        
        # Calculate contribution of powers of 2 multiplied by x
        for i in range(30):
            v = (2 ** i) * x
            if v > m:
                break
            answer += m - v
    
    # Get all divisors of g and process them
    divisors = get_all_divisors(g)
    for div in divisors:
        process(div)
    
    return answer

print(solve_three_horses())