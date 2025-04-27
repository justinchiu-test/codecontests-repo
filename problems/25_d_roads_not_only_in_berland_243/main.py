#!/usr/bin/env python3

from library.io import read_int

def main():
    n = read_int()

    # Initialize DSU
    parent = list(range(n+1))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    # Read edges
    edges = []
    for _ in range(n-1):
        x, y = map(int, input().split())
        edges.append((x, y))

    # Find redundant edges
    erase = []
    for x, y in edges:
        if find(x) == find(y):
            erase.append((x, y))
        else:
            union(x, y)

    # Reset DSU for connecting components
    parent = list(range(n+1))

    # Apply all non-redundant edges
    for x, y in edges:
        if (x, y) not in erase and (y, x) not in erase:
            union(x, y)

    # Find disjoint components
    components = {}
    for i in range(1, n+1):
        root = find(i)
        if root not in components:
            components[root] = []
        components[root].append(i)

    # Add new edges to connect components
    roots = list(components.keys())
    add = []

    for i in range(1, len(roots)):
        # Connect a vertex from first component to a vertex from other component
        add.append((components[roots[0]][0], components[roots[i]][0]))

    # Print results
    print(len(erase))

    # For each redundant edge, output both the redundant edge and a new edge
    output_parts = []
    for i in range(len(erase)):
        output_parts.append(f"{erase[i][0]} {erase[i][1]} {add[i][0]} {add[i][1]}")

    print(" ".join(output_parts))

if __name__ == "__main__":
    main()
