from library import readint, readints, DSU
from collections import Counter

# Bear Friendship Condition: each component must be complete graph
n, m = readints(2)
dsu = DSU(n + 1)
edges = []
for _ in range(m):
    u, v = readints(2)
    edges.append((u, v))
    dsu.union(u, v)
# count edges per component root
edge_count = Counter(dsu.find(u) for u, _ in edges)
# count nodes per component
node_count = Counter(dsu.find(i) for i in range(1, n + 1))
for r, cnt in node_count.items():
    # expected edges in complete graph
    if edge_count.get(r, 0) != cnt * (cnt - 1) // 2:
        print("NO")
        break
else:
    print("YES")
