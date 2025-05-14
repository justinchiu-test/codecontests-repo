from library import readint, read_graph, complement_components

# Connected components in complement graph: output sorted sizes
n, m = readint(), readint()
edges = read_graph(n, m)
adj_sets = [set(neigh) for neigh in edges]
comps = complement_components(n, adj_sets)
comps.sort()
print(len(comps))
print(*comps)
