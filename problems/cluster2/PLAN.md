# Library Plan for Cluster 2

Based on the analysis of the problem solutions in cluster 2, this document outlines the design for the shared library. The problems in this cluster predominantly focus on graph algorithms, particularly DSU (Disjoint Set Union), DFS (Depth-First Search), and related operations.

## Core Components

### 1. Graph Representation

- **Graph**: A class to represent a graph with methods for adding edges and vertices
  - Support for both directed and undirected graphs
  - Support for weighted edges (optional)
  - Provide both adjacency list and adjacency matrix representations

### 2. DSU (Disjoint Set Union)

- **DSU**: A class implementing the Disjoint Set Union data structure
  - `find(x)`: Find the representative of the set containing x with path compression
  - `union(x, y)`: Union the sets containing x and y
  - `is_same_set(x, y)`: Check if x and y are in the same set
  - `count_sets()`: Count the number of distinct sets

### 3. Graph Traversal

- **DFS**: Depth-First Search implementations
  - Recursive DFS with customizable visit callbacks
  - Iterative DFS with stack for large graphs
  - Return visited nodes, paths, or other computed values

- **BFS**: Breadth-First Search implementations
  - Standard BFS with queue
  - Support for finding shortest paths

### 4. Graph Algorithms

- **Connected Components**: Find connected components in an undirected graph
- **Cycle Detection**: Detect cycles in directed and undirected graphs
- **Topological Sort**: For directed acyclic graphs
- **Shortest Path**: Implementations of algorithms like Dijkstra or BFS for unweighted graphs

### 5. Utility Functions

- **Input Parsing**: Common input parsing patterns for graph problems
- **Output Formatting**: Format output according to common requirements

## Implementation Approach

The library will be implemented in a modular fashion, allowing problem solutions to import only the components they need. Core functionality will be implemented first, followed by more specialized algorithms.

Each component will be thoroughly tested with unit tests and validated against problem solutions to ensure correctness.

## Usage Examples

```python
# Example: Using DSU to count connected components
from library import DSU

dsu = DSU(n)
for i in range(m):
    u, v = map(int, input().split())
    dsu.union(u, v)
print(dsu.count_sets())

# Example: Using Graph for DFS traversal
from library import Graph

g = Graph(n)
for i in range(m):
    u, v = map(int, input().split())
    g.add_edge(u, v)
visited = g.dfs(start_node)
```

## Refactoring Strategy

1. Implement the DSU class first, as it's used in many problems
2. Implement the Graph class with basic traversal methods
3. Add specialized algorithms as needed when refactoring solutions
4. Ensure backward compatibility as the library evolves
5. Refactor solutions using the highest-level abstractions possible while maintaining readability

## Performance Considerations

- Time and space complexity of all operations will be documented
- Optimize critical operations for performance
- Balance between abstraction and raw speed for competitive programming context