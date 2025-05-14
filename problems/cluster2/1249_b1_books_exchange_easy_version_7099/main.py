from library import readint, readints, DSU

def solve():
    n = readint()
    p = readints(n)
    dsu = DSU(n)
    for i, x in enumerate(p):
        dsu.union(i, x-1)
    return [dsu.size(i) for i in range(n)]

t = readint()
for _ in range(t):
    print(*solve())
