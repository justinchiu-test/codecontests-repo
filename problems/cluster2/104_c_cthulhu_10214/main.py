from library import readint, DSU

# Cthulhu: graph connected with exactly one cycle
n = readint(); m = readint()
if n < 3 or m != n:
    print("NO")
else:
    dsu = DSU(n)
    cycles = 0
    for _ in range(m):
        u = readint() - 1
        v = readint() - 1
        if not dsu.union(u, v):
            cycles += 1
    roots = {dsu.find(i) for i in range(n)}
    print("FHTAGN!" if cycles == 1 and len(roots) == 1 else "NO")
