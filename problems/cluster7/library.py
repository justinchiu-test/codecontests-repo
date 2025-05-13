# Shared library for Cluster 7: common utilities for problem solutions.
import sys

_data = sys.stdin.buffer.read().split()
_it = iter(_data)

def ni():
    """Read next token as int"""
    return int(next(_it))

def nl(n):
    """Read next n tokens as list of ints"""
    return [int(next(_it)) for _ in range(n)]

def nxt():
    """Read next token as string"""
    return next(_it).decode()

def xor_to(n):
    """Return XOR of all integers from 0 to n inclusive"""
    # XOR pattern repeats every 4
    return [n, 1, n+1, 0][n & 3]

def xor_range(a, b):
    """Return XOR of all integers in [a, b] inclusive"""
    if a > 0:
        return xor_to(b) ^ xor_to(a-1)
    return xor_to(b)

def xor_list(arr):
    """Return XOR of all elements in the list"""
    r = 0
    for x in arr:
        r ^= x
    return r

def prefix_xor(arr):
    """Return list of prefix XORs: [0, a0, a0^a1, ...]"""
    res = [0]
    r = 0
    for x in arr:
        r ^= x
        res.append(r)
    return res

def bits_to_int(bits):
    """Convert list of bits (LSB first) to integer"""
    r = 0
    for i, b in enumerate(bits):
        if b:
            r |= 1 << i
    return r

def int_to_bits(x, length):
    """Convert integer to list of bits (LSB first) of given length"""
    return [(x >> i) & 1 for i in range(length)]
