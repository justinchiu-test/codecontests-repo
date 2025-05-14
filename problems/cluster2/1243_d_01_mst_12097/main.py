from library import readint, read_graph, complement_components

# Number of additions = complement components - 1
n = readint(); m = readint()
edges = read_graph(n, m)
adj_sets = [set(neigh) for neigh in edges]
comps = complement_components(n, adj_sets)
print(len(comps) - 1)
