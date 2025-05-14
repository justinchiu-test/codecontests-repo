from library import readint, read_graph, complement_components

# Compute number of edges to add = number of complement components - 1
n = readint(); m = readint()
edges = read_graph(n, m)
# convert adjacency lists to sets for complement
adj_sets = [set(neigh) for neigh in edges]
comps = complement_components(n, adj_sets)
print(len(comps) - 1)
