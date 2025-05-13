#!/usr/bin/env python3
"""
Solution for Codeforces 1129C - Morse Code.
"""
from library import read_all_ints, z_function, MOD

def main():
    nums = read_all_ints()
    n = nums[0]
    s = nums[1:n+1]
    sm = 0
    ans = []
    BAD = {(0, 0, 1, 1), (0, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)}
    for i in range(1, n + 1):
        arr = s[:i]
        f = [0] * (i + 1)
        f[i] = 1
        for j in range(i - 1, -1, -1):
            for k in range(j, min(j + 4, i)):
                if tuple(arr[j:k + 1]) not in BAD:
                    f[j] = (f[j] + f[k + 1]) % MOD
        z = z_function(arr[::-1])
        new = i - max(z)
        for x in f[:new]:
            sm = (sm + x) % MOD
        ans.append(str(sm))
    print("\n".join(ans))

if __name__ == "__main__":
    main()
