#!/usr/bin/env python3

"""
Count pairs of persons making eye contact during a full turn.
"""
from library import getint, getints
from collections import Counter
from math import gcd

def main():
    t = getint()
    for _ in range(t):
        dic = Counter()
        n = getint()
        for _ in range(n):
            x, y, u, v = getints()
            dx, dy = u - x, v - y
            if dx == 0:
                dic[(0, 1 if dy > 0 else -1)] += 1
            elif dy == 0:
                dic[(1 if dx > 0 else -1, 0)] += 1
            else:
                g = gcd(dx, dy)
                dic[(dx // g, dy // g)] += 1
        res = sum(cnt * dic[(-x, -y)] for (x, y), cnt in dic.items()) >> 1
        print(res)

if __name__ == "__main__":
    main()
