#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_test_cases, read_ints, find_max_divisible_x

for _ in range(read_test_cases()):
    p, q = read_ints()
    print(find_max_divisible_x(p, q))
