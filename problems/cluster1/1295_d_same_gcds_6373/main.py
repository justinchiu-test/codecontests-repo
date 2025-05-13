#!/usr/bin/env python3

from library import read_test_cases, read_ints, gcd, euler_totient

def solve():
    a, m = read_ints()
    g = gcd(a, m)
    m = m // g
    return euler_totient(m)

for result in read_test_cases(solve):
    print(result)