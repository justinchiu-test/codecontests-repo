#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_ints, get_divisors

n, k = read_ints()
divisors = get_divisors(n)

if k > len(divisors):
    print(-1)
else:
    print(divisors[k-1])
