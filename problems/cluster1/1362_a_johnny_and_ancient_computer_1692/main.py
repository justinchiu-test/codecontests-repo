#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_test_cases, read_ints, min_operations_power_of_two

for _ in range(read_test_cases()):
    a, b = read_ints()
    print(min_operations_power_of_two(a, b))
