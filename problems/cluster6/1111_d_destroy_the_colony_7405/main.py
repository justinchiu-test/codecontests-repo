#!/usr/bin/env python3

from library import read_str, read_int, read_ints, MOD, mod_pow, mod_inverse
s = read_str()
n = len(s)
buc = [0] * 101
fac = [0] * (n + 1)
inv = [0] * (n + 1)
dp = [0] * (n + 1)
# temp_dp = [0] * (n+1)
ans = [[0] * 55 for _ in range(55)]


def find(c: 'str') -> 'int':
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 26
    else:
        return ord(c) - ord('a')


def add(a: 'int', b: 'int') -> 'int':
    a += b
    if a >= MOD:
        a -= MOD
    return a


def sub(a: 'int', b: 'int') -> 'int':
    a -= b
    if a < 0:
        a += MOD
    return a


# c = Counter(s)

# # store frequency
# for k in c.keys():
#     buc[find(k)] = c[k]

for i in s:
    buc[find(i)] += 1  # naive count is fater than counter

# compute factorial and inv

fac[0] = 1
for i in range(1, n + 1):
    fac[i] = (fac[i - 1] * i) % MOD
inv[n] = mod_inverse(fac[n], MOD)
for i in range(n - 1, -1, -1):
    inv[i] = (inv[i + 1] * (i + 1)) % MOD

num = mod_pow(fac[n // 2], 2, MOD)
for i in range(0, 52):
    num = (num * inv[buc[i]]) % MOD

dp[0] = 1

for i in range(0, 52):
    if not buc[i]:
        continue
    for j in range(n, buc[i] - 1, -1):
        dp[j] = add(dp[j], dp[j - buc[i]])

for i in range(52):
    ans[i][i] = dp[n // 2]

for i in range(52):
    if not buc[i]:
        continue
    temp_dp = dp.copy()
    for k in range(buc[i], n + 1):
        temp_dp[k] = sub(temp_dp[k], temp_dp[k - buc[i]])

    for j in range(i + 1, 52):
        if not buc[j]:
            continue
        for k in range(buc[j], n + 1):
            temp_dp[k] = sub(temp_dp[k], temp_dp[k - buc[j]])

        ans[i][j] = (2 * temp_dp[n // 2]) % MOD

        for k in range(n, buc[j] - 1, -1):
            temp_dp[k] = add(temp_dp[k], temp_dp[k - buc[j]])

q = read_int()
for _ in range(q):
    x, y = read_ints()
    l_idx, r_idx = find(s[x - 1]), find(s[y - 1])
    if l_idx > r_idx:
        l_idx, r_idx = r_idx, l_idx
    print(num * ans[l_idx][r_idx] % MOD)
