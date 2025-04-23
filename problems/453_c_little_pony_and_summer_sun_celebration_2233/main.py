#!/usr/bin/env python3

import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, readline().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
    Edge[v].append(u)
Pr = list(map(int, readline().split()))
Po = Pr[:]

if sum(Pr) == 0:
    print(0)
else:
    st = Pr.index(1)
    stack = [~st, st]
    used = set([st])
    ans = []
    P = [None]*N
    pre = None
    while stack:
        vn = stack.pop()
        if vn >= 0:
            Pr[vn] ^= 1
            ans.append(vn)
            for vf in Edge[vn]:
                if vf in used:
                    continue
                P[vf] = vn
                stack.append(~vf)
                stack.append(vf)
                used.add(vf)
        else:
            vn = ~vn
            if pre != vn:
                Pr[vn] ^= 1
                ans.append(vn)
            if vn == st:
                if Pr[vn]:
                    ans.pop()
                    Pr[vn] ^= 1
                break
            if Pr[vn]:
                ans.append(P[vn])
                ans.append(vn)
                Pr[vn] ^= 1
                Pr[P[vn]] ^= 1
            if stack and stack[-1] >= 0:
                ans.append(P[vn])
                Pr[P[vn]] ^= 1
        pre = vn

    for a in ans:
        Po[a] ^= 1
    for a, b in zip(ans, ans[1:]):
        assert a != b
    if sum(Po):
        print(-1)
    else:
        print(len(ans))
        assert len(ans) <= 4*N
        print(*[a+1 for a in ans])
