from library import readint, read_graph, DSU

# Count ways = 2^(n - number_of_components)
n = readint(); m = readint()
adj = read_graph(n, m)
dsu = DSU(n)
for u in range(n):
    for v in adj[u]:
        dsu.union(u, v)
# count distinct roots
components = {dsu.find(i) for i in range(n)}
print(1 << (n - len(components)))
