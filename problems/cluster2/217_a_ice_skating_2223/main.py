from library import readint, readints, DSU

# Ice Skating: connect drifts sharing x or y coordinate
n = readint()
coords = [tuple(readints(2)) for _ in range(n)]
dsu = DSU(n)
for i in range(n):
    xi, yi = coords[i]
    for j in range(i+1, n):
        xj, yj = coords[j]
        if xi == xj or yi == yj:
            dsu.union(i, j)
roots = set(dsu.find(i) for i in range(n))
print(len(roots) - 1)
