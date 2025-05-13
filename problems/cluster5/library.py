"""
Library file for cluster5.
This contains shared code that can be imported by problems in this cluster.
"""
import sys

def input(prompt=None):
    """Read a line from stdin and strip the trailing newline."""
    line = sys.stdin.readline()
    return line[:-1] if line.endswith('\n') else line

def ni():
    """Read and return a single integer."""
    return int(input())

def na():
    """Read a line and return a list of integers."""
    return list(map(int, input().split()))

def ns():
    """Read and return a raw string line (no trailing newline)."""
    return input()

def zf(s):
    """Compute and return the Z-function array for sequence or string s."""
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

ALPH = 'abcdefghijklmnopqrstuvwxyz'
MAX_RUN = 10**9

def cnt(s):
    """Count the maximum consecutive runs of each lowercase letter in s."""
    c = {ch: 0 for ch in ALPH}
    i = 0
    n = len(s)
    while i < n:
        j = i + 1
        while j < n and s[j] == s[i]:
            j += 1
        c[s[i]] = max(c[s[i]], j - i)
        i = j
    return c

def nxt(cnt_dict, t):
    """Merge run counts for the string multiplication problem logic."""
    nc = cnt(t)
    # extend runs for letters seen previously but not in t
    for ch in ALPH:
        if cnt_dict.get(ch, 0) and not nc[ch]:
            nc[ch] = 1
    # prefix run length
    f = 0
    while f < len(t) and t[f] == t[0]:
        f += 1
    # suffix run length
    r = 0
    while r < len(t) and t[-1 - r] == t[-1]:
        r += 1
    if t[0] == t[-1]:
        if f == len(t):
            nc[t[0]] = min(MAX_RUN,
                            cnt_dict[t[0]] + (cnt_dict[t[0]] + 1) * len(t))
        elif cnt_dict[t[0]]:
            nc[t[0]] = min(MAX_RUN, max(nc[t[0]], f + 1 + r))
    else:
        if cnt_dict[t[0]]:
            nc[t[0]] = min(MAX_RUN, max(nc[t[0]], f + (cnt_dict[t[0]] > 0)))
        if cnt_dict[t[-1]]:
            nc[t[-1]] = min(MAX_RUN, max(nc[t[-1]], r + (cnt_dict[t[-1]] > 0)))
    return nc
