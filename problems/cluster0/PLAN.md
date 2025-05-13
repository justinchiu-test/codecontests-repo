# Graph and Tree Problem Library Plan

After analyzing the solutions, I've identified common patterns and functionality that can be extracted into a reusable library. This document outlines the library design and refactoring plan.

## Library Structure

The library is organized into the following sections:

1. **Input/Output Utilities**
   - Reading integers, arrays, and graphs
   - Common input parsing shortcuts
   - Graph and tree input parsers

2. **Data Structures**
   - Graph representation (adjacency list)
   - Tree representation
   - Node class for tree problems

3. **Graph Algorithms**
   - BFS traversal
   - DFS traversal (recursive and iterative)
   - Connected components
   - Spanning tree construction
   - Bipartite checking and coloring

4. **Tree Algorithms**
   - Subtree size calculation
   - Tree depth/level calculation
   - Leaf node identification
   - Level counting
   - Parent array conversion

5. **Utility Functions**
   - Recursion limit adjustment
   - Thread stack size adjustment
   - 0/1-indexing conversion

## Implemented Library Components

### Input/Output Utilities
- `read_ints()`: Read multiple integers from a line
- `read_int()`: Read a single integer
- `read_int_list()`: Read integers as a list
- `read_graph()`: Read edges and construct a graph
- `read_tree()`: Read tree edges
- `read_node_values()`: Read values associated with nodes
- `read_parent_array()`: Read parent array for a tree

### Data Structures
- `Graph` class with:
  - Edge addition
  - Degree calculation
  - BFS/DFS traversal
  - Component counting
  - Spanning tree generation
- `Node` class for object-oriented tree representation

### Graph Algorithms
- `bfs()`: BFS traversal
- `dfs()`: Recursive DFS traversal
- `dfs_iterative()`: Non-recursive DFS using a stack
- `build_tree_from_parent_array()`: Convert parent array to adjacency list
- `is_bipartite()`: Check if a graph is bipartite
- `bipartite_sets()`: Split a graph into two vertex sets

### Tree Algorithms
- `calculate_subtree_sizes()`: Calculate size of subtrees
- `calculate_depths()`: Calculate depth of each node
- `find_leaf_nodes()`: Find all leaf nodes
- `count_nodes_by_level()`: Count nodes at each level
- `count_odd_level_nodes()`: Count levels with odd numbers of nodes

### Utility Functions
- `setup_large_recursion()`: Configure for large recursion
- `run_with_large_stack()`: Run a function with a large stack
- `to_zero_index()`: Convert 1-based index to 0-based
- `to_one_index()`: Convert 0-based index to 1-based

## Refactoring Checklist

Status of each problem's refactoring:

- [x] 982_c_cut_em_all_5275
- [x] 580_c_kefa_and_park_5570
- [x] 839_c_journey_2458
- [x] 1176_e_cover_it_10635
- [x] 246_d_colorful_graph_3682
- [x] 292_b_network_topology_9930
- [x] 931_d_peculiar_appletree_4441
- [x] 913_b_christmas_spruce_7977
- [x] 404_c_restore_graph_3793
- [x] 1133_f1_spanning_tree_with_maximum_degree_10945
- [x] 1086_b_minimum_diameter_tree_8860
- [x] 902_b_coloring_a_tree_2877
- [x] 116_c_party_7303
- [x] 981_c_useful_decomposition_4026
- [x] 1143_c_queen_2410

## Refactoring Outcomes

### Code Reduction
We have successfully refactored 15 problems to use the shared library, which has significantly reduced code duplication. Common operations like reading graph inputs, BFS/DFS traversal, and tree operations are now handled by the library, leading to more concise and focused solution code.

### Maintainability Improvements
- Consistent approach to graph and tree problems
- Well-documented utility functions
- Clear separation of concerns between I/O, algorithms, and data structures
- Improved readability through elimination of boilerplate code

### Notable Refactorings

1. **982_c_cut_em_all_5275**
   - Replaced custom DFS with library's subtree size calculation
   - Simplified main logic using library I/O functions

2. **580_c_kefa_and_park_5570**
   - Refactored BFS traversal to use library's tree reading function
   - Simplified core logic of tracking cats

3. **931_d_peculiar_appletree_4441**
   - Replaced custom Node class with library's tree depth calculation
   - Used Counter for level counting

4. **246_d_colorful_graph_3682**
   - Refactored graph reading and construction
   - Simplified color relationship tracking

5. **913_b_christmas_spruce_7977**
   - Used tree traversal and leaf node identification
   - Simplified spruce condition checking

6. **1086_b_minimum_diameter_tree_8860**
   - Simplified node degree calculation
   - Used library I/O functions for cleaner input handling
   - Proper output formatting with required precision

7. **902_b_coloring_a_tree_2877**
   - Used BFS traversal from library
   - Simplified parent-child relationship tracking
   - Cleaner tree coloring logic

8. **116_c_party_7303**
   - Implemented recursive tree depth calculation
   - Used library I/O functions for input handling

9. **981_c_useful_decomposition_4026**
   - Improved variable naming for better readability
   - Simplified node degree calculation
   - Used library I/O functions

10. **1143_c_queen_2410**
    - Improved code readability with clear comments
    - Enhanced variable naming for better understanding of the problem domain
    - Used library I/O functions for cleaner input handling

## Challenges Encountered

1. **Inconsistent Test Cases**
   - Some problems had test cases that didn't match the problem description
   - Required adapting solutions to match specific output formats

2. **Edge Cases**
   - Problems often had special handling for edge cases
   - Library needed to be flexible enough to accommodate these cases

3. **Performance Requirements**
   - Some problems required specific optimizations (large recursion limits)
   - Added utility functions to handle these cases

## Further Improvements

1. **More Problems**
   - Continue refactoring the remaining problems
   - Add more specialized algorithms for advanced graph problems

2. **Library Extensions**
   - Add more specialized graph algorithms (Dijkstra, MST, etc.)
   - Implement more tree-related algorithms
   - Add visualization utilities for debugging

3. **Performance Optimization**
   - Profile and optimize critical functions
   - Consider alternative data structures for specific use cases