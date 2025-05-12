#!/usr/bin/env python3

def debug_solve():
    n = 4
    edges = [(3, 4), (1, 4), (3, 4)]
    d = {}

    for u, v in edges:
        min_ = min(u, v)
        max_ = max(u, v)

        if max_ != n:
            return False, None

        if min_ not in d:
            d[min_] = 0
        d[min_] += 1

    print(f"d = {d}")
    if sum(list(d.values())) + 1 != n:
        return False, None

    edge = []
    used = {i:False for i in range(1, n+1)}

    for k in sorted(list(d.keys())):
        used[k] = True
        mid = [n]
        print(f"Processing k={k}, mid={mid}")

        for i in range(k-1, 0, -1): # k-1->1
            print(f"  i={i}, mid={mid}, used={used}")
            if len(mid) == d[k]:
                break

            if used[i] == False:
                used[i] = True
                mid.append(i)

        if len(mid) < d[k]:
            return False, None

        mid.append(k)
        print(f"Final mid for k={k}: {mid}")

        for u, v in zip(mid[:-1], mid[1:]):
            edge.append([u, v])

    return True, edge

ans, arr = debug_solve()

if ans == False:
    print('NO')
else:
    print('YES')
    for u, v in arr:
        print(str(u)+' '+str(v))