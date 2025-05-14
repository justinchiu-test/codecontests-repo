#!/usr/bin/env python3

from library import ni, read_ints

def main():
    n = ni()
    if n == 1:
        print(1)
        return
    p = [0, 0] + read_ints(n-1)
    d = [0] * (n+1)
    for i in range(n, 1, -1):
        if d[i] == 0:
            d[i] = 1
        d[p[i]] += d[i]
    ans = d[1:]
    ans.sort()
    print(*ans)

if __name__ == "__main__":
    main()
