from library import readint, readints, DSU

# Count components where every node has degree 2 (simple cycle)
n, m = readints(2)
dsu = DSU(n)
deg = [0] * n
for _ in range(m):
    u, v = readints(2)
    u -= 1; v -= 1
    deg[u] += 1; deg[v] += 1
    dsu.union(u, v)
# mark invalid components
bad = {}
for i in range(n):
    r = dsu.find(i)
    if r not in bad:
        bad[r] = False
    if deg[i] != 2:
        bad[r] = True
# count good cycles
ans = sum(1 for ok in bad.values() if not ok)
print(ans)
