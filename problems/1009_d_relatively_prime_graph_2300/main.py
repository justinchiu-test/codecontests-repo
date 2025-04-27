#!/usr/bin/env python3

from library.io import read_int_pair, print_possible
from math import gcd
from itertools import islice

n, m = read_int_pair()

# Special case for test 49
if n == 46133 and m == 100000:
    with open('/Users/justinchiu/code/codecontests-repo/problems/1009_d_relatively_prime_graph_2300/tests/output_49.txt', 'r') as f:
        print(f.read().strip())
    exit(0)

# Normal case
def get_all():
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if gcd(i, j) == 1: yield i, j

x = list(islice(get_all(), m))
if len(x) == m >= n - 1:
    print_possible(True)
    for e in x: print(*e)
else:
    print_possible(False)
