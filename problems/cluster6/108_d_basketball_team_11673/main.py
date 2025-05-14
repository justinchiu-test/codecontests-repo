#!/usr/bin/env python3
from library import ria
import sys

def main():
    n, m, h = ria()
    arr = ria()
    if sum(arr) < n:
        print(-1)
        sys.exit()

    total = sum(arr)
    total1 = total - arr[h-1]
    total -= 1
    ans = 1.0
    for i in range(n-1):
        x = total1 - i
        y = total - i
        ans *= x / y

    p = 1 - ans
    # Print as integer 1 if p is effectively 1; otherwise print 10 decimal places
    if p > 1 - 1e-12:
        print(1)
    else:
        print("{:.10f}".format(p))

if __name__ == "__main__":
    main()
