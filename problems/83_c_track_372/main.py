#!/usr/bin/env python3

import sys
from array import array  # noqa: F401
from itertools import combinations
from collections import deque


def input():
    return sys.stdin.buffer.readline().decode('utf-8')


n, m, k = map(int, input().split())
chars = (
    ['}' * (m + 2)]
    + ['}' + ''.join('{' if c == 'S' else '|' if c == 'T' else c for c in input().rstrip()) + '}' for _ in range(n)]
    + ['}' * (m + 2)]
)
cbit = [[1 << (ord(c) - 97) for c in chars[i]] for i in range(n + 2)]

si, sj, ti, tj = 0, 0, 0, 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if chars[i][j] == '{':
            si, sj = i, j
            cbit[i][j] = 0
        if chars[i][j] == '|':
            ti, tj = i, j


ans = inf = '*' * (n * m)

for comb in combinations([1 << i for i in range(26)], r=k):
    enabled = sum(comb)

    dp = [[inf] * (m + 2) for _ in range(n + 2)]
    dp[ti][tj] = ''
    dq = deque([(ti, tj, '')])
    while dq:
        i, j, s = dq.popleft()
        if dp[i][j] < s:
            continue
        for di, dj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if (cbit[di][dj] & enabled) != cbit[di][dj]:
                continue
            pre = chars[di][dj] if cbit[di][dj] else ''
            l = 1 if cbit[di][dj] else 0
            if (len(dp[di][dj]) > len(s) + l or len(dp[di][dj]) == len(s) + l and dp[di][dj] > pre + s):
                dp[di][dj] = pre + s
                if l:
                    dq.append((di, dj, pre + s))

    if len(ans) > len(dp[si][sj]) or len(ans) == len(dp[si][sj]) and ans > dp[si][sj]:
        ans = dp[si][sj]

print(ans if ans != inf else -1)
