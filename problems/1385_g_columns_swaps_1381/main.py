#!/usr/bin/env python3

for t in range(int(input())):
    n = int(input())
    aa = [
        [int(s)-1 for s in input().split(' ')]
        for _ in [0, 1]
    ]
    maxv = max(max(aa[0]), max(aa[1]))
    minv = min(min(aa[0]), min(aa[1]))
    if minv != 0 or maxv != n - 1:
        print(-1)
        continue
    counts = [0] * n
    index = [[] for _ in range(n)]
    for row in aa:
        for x, a in enumerate(row):
            counts[a] += 1
            index[a] += [x]
    if not min(counts) == 2 == max(counts):
        print(-1)
        continue

    proc = [False] * n
    ans = []
    for i in range(n):
        if proc[i]:
            continue

        swapped = set()
        used = set()

        curcol = i
        curval = aa[0][i]
        while True:
            proc[curcol] = True
            used.add(curcol)
            if aa[0][curcol] == curval:
                nexval = aa[1][curcol]
            else:
                nexval = aa[0][curcol]
                swapped.add(curcol)

            nexcol = index[nexval][1] if index[nexval][0] == curcol else index[nexval][0]

            curcol = nexcol
            curval = nexval

            if curcol == i:
                break

        part = swapped if 2 * len(swapped) <= len(used) else used.difference(swapped)
        ans += part

    print(len(ans))
    print(' '.join(str(v + 1) for v in ans))
