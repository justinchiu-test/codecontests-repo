#!/usr/bin/env python3

n, m, k = map(int, input().split())
d = {}
for _ in range(m):
    u, v = map(int, input().split())
    if u not in d:
        d[u] = [v]
    else:
        d[u].append(v)
    if v not in d:
        d[v] = [u]
    else:
        d[v].append(u)


# print(d)
stack = []
not_visited = set(range(1, n+1))

while not_visited:
    if not stack:
        stack.append((not_visited.pop(), 1, 0))
        path = []
        visited = {}
        c = 0
    p, l, parent = stack.pop()

    path.append(p)
    visited[p] = c
    c += 1
    if p in not_visited:
        not_visited.remove(p)
    f = False
    for x in d[p]:
        if x not in visited:
            stack.append((x, l+1, p))
        else:

            if c - visited[x] > k:
                path = path[visited[x]:]
                f = True
                break
    if f:
        break
print(len(path))
print(*path)
