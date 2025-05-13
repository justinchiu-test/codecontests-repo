"""
Library file for cluster7.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
from itertools import accumulate
from operator import xor

# I/O helpers
input = sys.stdin.readline
def read_int():
    return int(input())
def read_ints():
    return list(map(int, input().split()))
def read_str():
    return input().strip()
def read_strs():
    return input().split()

# Bit utilities
def xor_list(a):
    """Return XOR of all integers in the list a."""
    r = 0
    for x in a:
        r ^= x
    return r

def xor_upto(n):
    """Return XOR of all integers from 1 to n."""
    m = n & 3
    if m == 0:
        return n
    if m == 1:
        return 1
    if m == 2:
        return n + 1
    return 0

def prefix_xor(a):
    """Return list of prefix XORs: [0, a[0], a[0]^a[1], ...]."""
    res = [0]
    r = 0
    for x in a:
        r ^= x
        res.append(r)
    return res

def bits_to_int(bits):
    """Interpret LSB-first bit list as integer."""
    r = 0
    for i, b in enumerate(bits):
        if b:
            r |= (1 << i)
    return r

def bit_positions(n):
    """Return 1-based positions of set bits in n."""
    return [i+1 for i in range(n.bit_length()) if (n >> i) & 1]

# Problem-specific solvers
def solve_triple_flips(a):
    """
    Solve the 'triple flips' problem for a small binary list a.
    Return list of operations (each is a list of 1-based positions) or None.
    """
    l = len(a)
    d = bits_to_int(a)
    if d == 0:
        return []
    usable = []
    if l >= 3:
        usable += [0b111 << i for i in range(l-2)]
    if l >= 5:
        usable += [0b10101 << i for i in range(l-4)]
    if l >= 7:
        usable += [0b1001001 << i for i in range(l-6)]
    ul = len(usable)
    for mask in range(1 << ul):
        start = 0
        for j in range(ul):
            if (mask >> j) & 1:
                start ^= usable[j]
        if start == d:
            ops = []
            for j in range(ul):
                if (mask >> j) & 1:
                    ops.append(bit_positions(usable[j]))
            return ops
    return None

def count_xor_solutions(s, x):
    """
    Count pairs (u, v) such that u + v = s and u ^ v = x.
    """
    # sum and xor parity check
    if s < x or ((s - x) & 1):
        return 0
    m = (s - x) // 2
    # no overlapping bits
    if m & x:
        return 0
    # number of solutions = 2^{popcount(x)}
    cnt = x.bit_count() if hasattr(x, 'bit_count') else bin(x).count('1')
    res = 1 << cnt
    # exclude trivial u=v case if s==x
    if s == x:
        res -= 2
    return res
