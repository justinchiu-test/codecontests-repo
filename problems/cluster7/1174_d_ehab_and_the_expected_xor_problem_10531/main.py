#!/usr/bin/env python3

from library import fast_ints

n, x = fast_ints()
ans = []
vis = [0] * ((2 ** 18) + 1)
lmt = 2 ** n
xor_val = 0

# Mark initial values as visited
vis[0], vis[x] = 1, 1

for i in range(1, lmt):
    if vis[i]:
        continue
    ans.append(xor_val ^ i)
    xor_val = i
    vis[i] = 1
    vis[i ^ x] = 1

print(len(ans))
if ans:
    print(*ans)