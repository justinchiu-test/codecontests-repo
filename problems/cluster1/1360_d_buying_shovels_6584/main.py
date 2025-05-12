#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_test_cases, read_ints, min_packages_for_n_items

for _ in range(read_test_cases()):
    n, k = read_ints()
    print(min_packages_for_n_items(n, k))
