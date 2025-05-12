#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_ints, accumulate_prime_powers

x, n = read_ints()
print(accumulate_prime_powers(x, n))
