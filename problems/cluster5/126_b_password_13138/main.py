#!/usr/bin/env python3
"""
Solution for Codeforces 126B - Password.
"""
from library import read, z_function
from collections import Counter

def main():
    s = read()
    n = len(s)
    Z = z_function(s)
    third = [Z[i] for i in range(n) if i + Z[i] == n]
    if not third:
        print("Just a legend")
        return
    cnt = Counter(Z)
    if len(third) == 1:
        k = third[0]
        if cnt[k] >= 2 or max(Z) > k:
            print(s[:k])
        else:
            print("Just a legend")
    else:
        k = third[0]
        if cnt[k] >= 2 or max(Z) > k:
            print(s[:k])
        else:
            print(s[:third[1]])

if __name__ == "__main__":
    main()
