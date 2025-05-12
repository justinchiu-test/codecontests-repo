#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_test_cases, read_int, find_three_factors

for _ in range(read_test_cases()):
    n = read_int()
    factors = find_three_factors(n)

    if factors:
        print("YES")
        print(factors[0], factors[1], factors[2])
    else:
        print("NO")
