#!/usr/bin/env python3

import sys
sys.path.append('..')
from library import ALPHABET, iinput, max_consecutive_chars

MAX = 10 ** 9

def nxt(c, t):
    nc = max_consecutive_chars(t)
    for ch in ALPHABET:
        if c.get(ch, 0) and ch not in nc:
            nc[ch] = 1
    
    # Find consecutive characters at start and end
    f = 0
    while f < len(t) and t[f] == t[0]:
        f += 1
    r = 0
    while r < len(t) and t[-1 - r] == t[-1]:
        r += 1
    
    if t[0] == t[-1]:
        if f == len(t):  # All characters are the same
            nc[t[0]] = max(nc[t[0]], c.get(t[0], 0) + (c.get(t[0], 0) + 1) * len(t))
        elif c.get(t[0], 0):
            nc[t[0]] = max(nc[t[0]], f + 1 + r)
    else:
        nc[t[0]] = max(nc[t[0]], f + (c.get(t[0], 0) > 0))
        nc[t[-1]] = max(nc[t[-1]], r + (c.get(t[-1], 0) > 0))
    
    return {x: min(MAX, y) for x, y in nc.items()}

n = iinput()
c = max_consecutive_chars(input())

for i in range(n - 1):
    c = nxt(c, input())

print(max(c.values()))