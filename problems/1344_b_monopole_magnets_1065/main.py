#!/usr/bin/env python3

# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/16

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def check(row):
    start, end = 0, len(row) - 1
    while start < len(row) and row[start] == 0:
        start += 1

    if start >= len(row):
        return True, True

    while end >= start and row[end] == 0:
        end -= 1

    for i in range(start, end):
        if row[i] == 0:
            return False, False

    return True, False


def solve(N, M, A):
    blankrow = []
    for r in range(N):
        row = A[r]
        a, b = check(row)
        if not a:
            return -1
        if b:
            blankrow.append(r)

    blankcol = []
    for c in range(M):
        col = [A[r][c] for r in range(N)]
        a, b = check(col)
        if not a:
            return -1
        if b:
            blankcol.append(c)

    if (len(blankcol) > 0 and len(blankrow) == 0) or (len(blankrow) > 0 and len(blankcol) == 0):
        return -1

    if len(blankcol) * len(blankrow) == N * M:
        return 0

    for r in blankrow:
        for c in blankcol:
            A[r][c] = 2

    idx = 2
    for r in range(N):
        for c in range(M):
            if A[r][c] == 1:
                idx += 1
                A[r][c] = idx
                q = [(r, c)]
                while q:
                    nq = []
                    for x, y in q:
                        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                            if 0 <= nx < N and 0 <= ny < M and A[nx][ny] == 1:
                                A[nx][ny] = idx
                                nq.append((nx, ny))
                    q = nq

    # for row in A:
    #     print(' '.join(map(str, row)))

    return idx - 2


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        row = [1 if v == '#' else 0 for v in list(input())]
        A.append(row)

    print(solve(N, M, A))
