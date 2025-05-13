"""
Shared utility library for all problems in this cluster.
Provides fast I/O, readers, and common numeric helpers.
"""
import sys

# -- Fast input override
input = sys.stdin.readline

from functools import reduce
import operator

def read_int():
    """Read and return a single integer."""
    return int(input())

def read_ints():
    """Read a line of input and return a list of ints."""
    return list(map(int, input().split()))

def read_strs():
    """Read a line of input and return a list of strings."""
    return input().split()

def read_matrix(n, m, *, type=int):
    """Read an n x m matrix of items cast to `type`."""
    return [list(map(type, input().split())) for _ in range(n)]

def xor_list(it):
    """Compute the XOR of all elements in the iterable."""
    return reduce(operator.xor, it, 0)

def prefix_xor(lst):
    """Return list of prefix XORs of `lst` (same length)."""
    res = []
    acc = 0
    for x in lst:
        acc ^= x
        res.append(acc)
    return res

def prefix_sum(lst):
    """Return list of prefix sums of `lst` (same length)."""
    res = []
    acc = 0
    for x in lst:
        acc += x
        res.append(acc)
    return res

def popcount(x):
    """Return the number of set bits in integer x."""
    try:
        return x.bit_count()
    except AttributeError:
        return bin(x).count('1')

def print_list(lst, sep=' '):
    """Print elements of lst separated by sep."""
    print(*lst, sep=sep)

def setup_fast_io():
    """
    Placeholder for any fast I/O setup if needed.
    Currently input is already bound to sys.stdin.readline.
    """
    return
