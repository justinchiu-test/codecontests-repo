#!/usr/bin/env python3

dfs(1)
#!/usr/bin/env python3
from library import read_ints, UndirectedGraph, count_connected_components, dfs_cycle_detection

def main():
    n, m = read_ints()
    if m != n:
        print("NO")
        return
    g = UndirectedGraph()
    for i in range(n):
        g.add_vertex(i)
    for _ in range(m):
        u, v = read_ints()
        u -= 1; v -= 1
        g.add_edge(u, v)
    if count_connected_components(g) == 1 and dfs_cycle_detection(g):
        print("FHTAGN!")
    else:
        print("NO")

if __name__ == "__main__":
    main()
