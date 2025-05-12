#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_test_cases, read_ints, gcd, phi

for _ in range(read_test_cases()):
    a, m = read_ints()
    g = gcd(a, m)
    m = m // g
    print(phi(m))
