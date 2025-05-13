#!/usr/bin/env python3


#!/usr/bin/env python3
from library import read_ints, UndirectedGraph, dfs

def main():
    n, m = read_ints()
    if n < 3 or m != n:
        print("NO")
        return
    g = UndirectedGraph()
    for i in range(n):
        g.add_vertex(i)
    for _ in range(m):
        u, v = read_ints()
        u -= 1; v -= 1
        g.add_edge(u, v)
    visited = dfs(g, 0)
    print("FHTAGN!" if len(visited) == n else "NO")

if __name__ == "__main__":
    main()
