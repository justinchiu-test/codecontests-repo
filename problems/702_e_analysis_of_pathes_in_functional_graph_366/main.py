#!/usr/bin/env python3

import sys
n, k = map(int, sys.stdin.buffer.readline().decode('utf-8').split())
a = list(map(int, sys.stdin.buffer.readline().decode('utf-8').split()))
b = list(map(int, sys.stdin.buffer.readline().decode('utf-8').split()))

logk = len(bin(k)) - 2
sum_w, sum_w_p = b[:], b[:]
min_w, min_w_p = b[:], b[:]
dest, dest_p = a[:], a[:]

ans_sum, ans_min, pos = [0]*n, b[:], list(range(n))
if k & 1:
    ans_sum = b[:]
    pos = [a[i] for i in range(n)]
k >>= 1

for j in range(1, logk):
    for i in range(n):
        d = dest[i]
        p = 0 if d > i else 1
        dest_p[i] = d
        dest[i] = (dest_p if p else dest)[d]
        sum_w_p[i] = sum_w[i]
        sum_w[i] += (sum_w_p if p else sum_w)[d]
        min_w_p[i] = min_w[i]
        if min_w[i] > (min_w_p if p else min_w)[d]:
            min_w[i] = (min_w_p if p else min_w)[d]

    if k & 1:
        for i in range(n):
            ans_sum[i] += sum_w[pos[i]]
            if ans_min[i] > min_w[pos[i]]:
                ans_min[i] = min_w[pos[i]]
            pos[i] = dest[pos[i]]
    k >>= 1


sys.stdout.buffer.write('\n'.join(
    (str(ans_sum[i]) + ' ' + str(ans_min[i]) for i in range(n))).encode('utf-8'))
