#!/usr/bin/env python3

from library import read_ints, comb

def main():
    n, m = read_ints()
    a = read_ints()
    # maximum possible queue size
    i_max = max((n + x - 1) // x for x in a)
    total = m ** n
    upto_prev = 0
    ans = 0
    for i in range(1, i_max + 1):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for j in range(m):
            aj = a[j]
            for l in range(n + 1):
                v = dp[j][l]
                if not v:
                    continue
                maxk = min(n - l, i * aj)
                for k in range(maxk + 1):
                    dp[j + 1][l + k] += v * comb(n - l, k)
        upto = dp[m][n]
        ans += (upto - upto_prev) * i
        upto_prev = upto
    print(f"{ans/total:.15f}")

if __name__ == '__main__':
    main()
