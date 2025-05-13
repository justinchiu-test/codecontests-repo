# Library Design Plan for Graph Problems

This document outlines a plan for creating a shared library to reduce code duplication across the graph problems. The library will provide reusable components for common patterns identified in the solutions.

## Identified Common Patterns

After analyzing the solutions, these common patterns emerged:

1. **Input Parsing**
   - Reading single integers
   - Reading space-separated integers
   - Converting 1-indexed to 0-indexed
   - Fast I/O optimization

2. **Graph Representations**
   - Adjacency lists (directed and undirected)
   - Tree structures
   - Edge representation

3. **Graph Algorithms**
   - Depth-First Search (recursive and iterative)
   - Breadth-First Search
   - Tree traversal
   - Shortest paths (Dijkstra)
   - Connected components
   - Spanning trees

4. **Utilities**
   - Distance calculations
   - Node degree counting
   - Path finding
   - Tree properties (height, leaf counting)

## Library Structure

The library will be organized into the following modules:

### 1. Input/Output Module

```python
# Fast input reading functions
def read_int():
    """Read a single integer from input."""
    return int(input())

def read_ints():
    """Read space-separated integers from input."""
    return map(int, input().split())

def read_int_list():
    """Read space-separated integers from input and return as list."""
    return list(map(int, input().split()))

# Fast I/O setup
def setup_fast_io():
    """Set up fast I/O for competitive programming."""
    import io, os
    return io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
```

### 2. Graph Module

```python
# Graph creation
def create_graph(n, edges=None, directed=False, one_indexed=True):
    """
    Create a graph with n nodes and optional edges.

    Args:
        n: Number of nodes
        edges: List of (u, v) or (u, v, w) for weighted graphs
        directed: If True, create a directed graph
        one_indexed: If True, convert 1-indexed to 0-indexed

    Returns:
        Adjacency list representation of the graph
    """

# Graph algorithms
def dfs(graph, start, visited=None):
    """Recursive DFS implementation."""

def dfs_iterative(graph, start):
    """Iterative DFS implementation using a stack."""

def bfs(graph, start):
    """BFS implementation using a queue."""

def find_components(graph):
    """Find connected components in the graph."""

def shortest_path(graph, start, end, weighted=False):
    """Find shortest path between two nodes."""
```

### 3. Tree Module

```python
# Tree utilities
def is_tree(graph):
    """Check if a graph is a tree (connected, n-1 edges)."""

def tree_height(graph, root=0):
    """Calculate the height of a tree."""

def count_leaves(graph, root=0):
    """Count leaf nodes in a tree."""

def tree_diameter(graph):
    """Calculate the diameter of a tree."""

def lca(graph, root, a, b):
    """Find lowest common ancestor of two nodes."""
```

### 4. Utilities Module

```python
# General utilities
def mex(arr):
    """Find the minimum excluded non-negative integer."""

def convert_to_zero_indexed(arr):
    """Convert a 1-indexed array to 0-indexed."""

# Constants
INF = 10**18
```

## Implementation Approach

1. Start by implementing the input/output module, as this is used by virtually all problems.
2. Implement the graph module with core functionality for creating and traversing graphs.
3. Add tree-specific operations in the tree module.
4. Add general utilities as they are identified during refactoring.
5. Refactor each problem solution to use the library components.
6. Continuously update the library as new patterns emerge during refactoring.

## Refactoring Checklist

The following checklist will track the refactoring progress for each problem:

- [ ] 580_c_kefa_and_park_5570
- [ ] 913_b_christmas_spruce_7977
- [ ] 1176_e_cover_it_10635
- [ ] 1133_f1_spanning_tree_with_maximum_degree_10945
- [ ] 839_c_journey_2458
- [ ] 1041_e_tree_reconstruction_8858
- [ ] 1076_d_edge_deletion_9486
- [ ] 1086_b_minimum_diameter_tree_8860
- [ ] 110_e_lucky_tree_11049
- [ ] 1118_f1_tree_cutting_easy_version_12195
- [ ] 1143_c_queen_2410
- [ ] 116_c_party_7303
- [ ] 1286_b_numbers_on_tree_11475
- [ ] 1287_d_numbers_on_tree_1897
- [ ] 1325_c_ehab_and_pathetic_mexs_1064
- [ ] 1338_b_edge_weight_assignment_7623
- [ ] 1391_e_pairs_of_pairs_6690
- [ ] 246_d_colorful_graph_3682
- [ ] 292_b_network_topology_9930
- [ ] 319_b_psychos_in_a_line_454
- [ ] 404_c_restore_graph_3793
- [ ] 420_c_bug_in_code_5355
- [ ] 421_d_bug_in_code_563
- [ ] 747_e_comments_9533
- [ ] 796_c_bank_hacking_5163
- [ ] 902_b_coloring_a_tree_2877
- [ ] 931_d_peculiar_appletree_4441
- [ ] 963_b_destruction_of_a_tree_65
- [ ] 981_c_useful_decomposition_4026
- [ ] 982_c_cut_em_all_5275

## Evaluation Metrics

To evaluate the success of the refactoring:

1. Count the total number of lines in all original solutions
2. Count the total number of lines in all refactored solutions plus the library
3. Calculate the reduction in code size
4. Ensure all solutions still pass their original tests

The goal is to achieve a significant reduction in total code size while maintaining correctness.
