from library import readint, readints, DSU

# Preprocess DSU per color for connectivity
n, m = readints(2)
color_dsus = {}
for _ in range(m):
    u, v, c = readints(3)
    if c not in color_dsus:
        color_dsus[c] = DSU(n + 1)
    color_dsus[c].union(u, v)
q = readint()
for _ in range(q):
    u, v = readints(2)
    cnt = 0
    for dsu in color_dsus.values():
        if dsu.find(u) == dsu.find(v):
            cnt += 1
    print(cnt)
