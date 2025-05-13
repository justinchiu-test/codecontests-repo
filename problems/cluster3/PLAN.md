# Library Plan for Cluster3 (Tree-focused Problems)

Based on the analysis of the problems in this cluster, we can identify several common patterns and components that should be part of our shared library. This cluster primarily focuses on tree-based problems with various algorithms like DFS, BFS, and dynamic programming on trees.

## 1. Library Structure

The library will be organized into the following modules:

1. **Input/Output Utils** - Fast I/O handling and common input parsing
2. **Tree/Graph Construction** - Utilities for building adjacency lists and parsing tree inputs
3. **Tree Traversal** - DFS, BFS, and related algorithms for tree exploration
4. **Dynamic Programming on Trees** - Functions for common tree DP patterns
5. **Utility Functions** - General utilities like recursion handling, custom decorators

## 2. Detailed Components

### 2.1 Input/Output Utils

```python
# Fast I/O implementation
def setup_fast_io():
    """Set up fast I/O for competitive programming."""
    # Implementation based on FastIO classes found in solutions

# Input parsing functions
def read_int():
    """Read a single integer from input."""
    return int(input())

def read_ints():
    """Read multiple integers from a single line."""
    return list(map(int, input().split()))

def read_int_pair():
    """Read two integers from a single line."""
    return map(int, input().split())

def read_tree_edges(n, indexed_from=1):
    """Read n-1 edges of a tree and return adjacency list."""
    # Implementation for reading tree edges and constructing adjacency list
```

### 2.2 Tree/Graph Construction

```python
def build_adjacency_list(n, edges, directed=False, indexed_from=1):
    """Build adjacency list from edges."""
    # Implementation to create an adjacency list

def read_tree(n, indexed_from=1):
    """Read a tree with n nodes and return adjacency list."""
    # Implementation to read and build a tree

def parent_array_to_adjacency_list(parents, indexed_from=1):
    """Convert parent array to adjacency list."""
    # Implementation to convert parent array representation to adjacency list
```

### 2.3 Tree Traversal

```python
def dfs(graph, start=0, visited=None):
    """Iterative DFS implementation."""
    # Implementation for iterative DFS

def dfs_recursive(graph, node, visited=None, parent=None):
    """Recursive DFS implementation."""
    # Implementation for recursive DFS

def dfs_with_stack(graph, start=0):
    """DFS using explicit stack with pre/post visit handling."""
    # Implementation for stack-based DFS with pre/post visit markers

def bfs(graph, start=0):
    """BFS implementation."""
    # Implementation for BFS

def calculate_depths(graph, root=0):
    """Calculate depth of each node in a tree."""
    # Implementation to calculate depths from root

def calculate_subtree_sizes(graph, root=0):
    """Calculate subtree size for each node."""
    # Implementation to calculate subtree sizes
```

### 2.4 Dynamic Programming on Trees

```python
def tree_dp_bottom_up(graph, values, combine_func, leaf_value=0, root=0):
    """Generic bottom-up DP on a tree."""
    # Implementation for bottom-up tree DP

def tree_dp_top_down(graph, values, update_func, root=0):
    """Generic top-down DP on a tree."""
    # Implementation for top-down tree DP

def reroot_dp(graph, calculate_subtree, calculate_reroot):
    """Implement the tree rerooting technique."""
    # Implementation for the rerooting technique
```

### 2.5 Utility Functions

```python
def bootstrap(f):
    """Decorator to convert recursive function to iterative to avoid stack overflow."""
    # Implementation of bootstrap decorator

def increase_recursion_limit():
    """Increase Python's recursion limit for tree problems."""
    # Implementation to increase recursion limit

def thread_with_large_stack(func):
    """Run function in a thread with a large stack size."""
    # Implementation for threading with large stack
```

## 3. Implementation Strategy

1. Start with core functionality that appears most frequently (tree construction, DFS/BFS)
2. Implement utility functions to handle recursion limits and stack issues
3. Add the input/output utilities
4. Implement DP on trees functions
5. Add more specialized functions as needed when refactoring individual problems

## 4. Refactoring Plan

The refactoring process will follow these steps for each problem:

1. Identify the core functionality used in the problem
2. Replace custom implementations with library functions
3. Ensure the solution still passes all tests
4. Update the library if any missing functionality is identified

## 5. Refactoring Checklist

As problems are refactored, they will be added to this checklist:

- [ ] 1056_d_decorate_apple_tree_1782
- [ ] 1076_e_vasya_and_a_tree_11985
- [ ] 1083_a_the_fair_nut_and_the_best_path_12817
- [ ] 1084_d_the_fair_nut_and_the_best_path_3448
- [ ] 1092_f_tree_with_maximum_cost_8028
- [ ] 1153_d_serval_and_rooted_tree_2202
- [ ] 1187_e_tree_painting_12718
- [ ] 1280_c_jeremy_bearimy_11057
- [ ] 1281_e_jeremy_bearimy_9704
- [ ] 1324_f_maximum_white_subtree_3668
- [ ] 1332_f_independent_set_12309
- [ ] 1336_a_linova_and_kingdom_8768
- [ ] 1436_d_bandit_in_a_city_4611
- [ ] 1453_e_dog_snacks_5757
- [ ] 1498_f_christmas_game_5029
- [ ] 1499_f_diameter_cuts_11692
- [ ] 1528_a_parsas_humongous_tree_10236
- [ ] 1540_b_tree_array_3053
- [ ] 23_e_tree_4723
- [ ] 274_b_zero_tree_3163
- [ ] 275_d_zero_tree_12948
- [ ] 461_b_appleman_and_tree_11604
- [ ] 538_e_demiurges_play_again_12023
- [ ] 543_d_road_improvement_5673
- [ ] 696_b_puzzles_9008
- [ ] 697_d_puzzles_7551
- [ ] 700_b_connecting_universities_5263
- [ ] 735_e_ostap_and_tree_2037
- [ ] 80_e_beavermuncher0xff_11410
- [ ] 846_e_chemistry_in_berland_60
- [ ] 913_b_christmas_spruce_7977 (from cluster0, may need to check if it's relevant)

## 6. Benefits of the Library

1. **Code Reduction**: By centralizing common functionality, we eliminate duplicated code across problems.
2. **Standardization**: Consistent interfaces for tree operations make code more readable.
3. **Reliability**: Well-tested library functions reduce the chance of bugs in individual solutions.
4. **Maintainability**: Changes to algorithms or data structures can be made in one place.

## 7. Challenges and Considerations

1. **Flexibility vs. Specificity**: The library needs to be general enough to be useful across problems but specific enough to meaningfully reduce code.
2. **Performance**: Competitive programming often requires optimized code; the library shouldn't add significant overhead.
3. **Backward Compatibility**: As we update the library, we need to ensure previously refactored solutions still work.
4. **Edge Cases**: The library must handle various input formats and edge cases across different problems.

This plan will evolve as we implement the library and refactor solutions, but it provides a starting framework for the task.
