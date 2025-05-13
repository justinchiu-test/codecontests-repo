#!/usr/bin/env python3


from library import readints, dfs, graph

 n, m = readints()

if n >= 3 and n == m:

    edges = [tuple(readints()) for _ in range(m)]
    e = graph(n, edges, one_indexed=True)

    visited = dfs(e, 0)
    print('FHTAGN!' if len(visited) == n else 'NO')
else:
    print('NO')
