# Library Development Plan for Graph Problem Cluster

## Overview

Based on analysis of the problem solutions in this cluster, we can identify common patterns and components that can be abstracted into a shared library. This library will focus on graph algorithms, data structures, and utility functions that appear frequently across the solutions.

## Library Components

### 1. Input/Output Utilities

```python
# Standard input readers
def read_int():
    """Read a single integer from standard input."""

def read_ints():
    """Read space-separated integers from standard input as a list."""

def read_int_tuple():
    """Read space-separated integers from standard input as a tuple."""

def read_int_grid(rows, cols=None):
    """Read a grid of integers from standard input."""

def read_char_grid(rows, cols=None):
    """Read a grid of characters from standard input."""

def read_weighted_edges(m, one_indexed=True):
    """Read m edges with weights from standard input."""

def read_edges(m, one_indexed=True):
    """Read m edges without weights from standard input."""

# Standard output writers
def write_ints(ints, sep=' '):
    """Write integers to standard output separated by sep."""

def write_grid(grid):
    """Write a grid to standard output."""
```

### 2. Graph Representations

```python
class Graph:
    """
    A directed graph representation using adjacency lists.

    Supports both weighted and unweighted edges.
    """

class UndirectedGraph(Graph):
    """
    An undirected graph representation using adjacency lists.

    Inherits from Graph class and ensures edges are added in both directions.
    """

def grid_to_graph(grid, diagonals=False):
    """
    Convert a 2D grid to a graph representation.

    Args:
        grid: 2D grid of values
        diagonals: Whether to connect diagonal cells

    Returns:
        A Graph object
    """
```

### 3. Disjoint Set Union (DSU) / Union-Find

```python
class DisjointSet:
    """
    Efficient implementation of disjoint-set data structure with:
    - Path compression
    - Union by rank
    - Component counting
    - Size tracking

    Supports both integer and non-integer elements.
    """
```

### 4. Graph Algorithms

```python
# DFS related functions
def dfs(graph, start, visited=None):
    """Basic DFS traversal returning visited nodes."""

def dfs_with_path(graph, start, end):
    """DFS finding a path from start to end."""

def dfs_cycle_detection(graph, start=None):
    """Detect if the graph has a cycle using DFS."""

def dfs_component(graph, start, visited=None):
    """Find the connected component containing the start node."""

# BFS related functions
def bfs(graph, start, visited=None):
    """Basic BFS traversal returning visited nodes and distances."""

def bfs_shortest_path(graph, start, end):
    """Find shortest path from start to end using BFS."""

def bfs_component(graph, start, visited=None):
    """Find the connected component containing the start node using BFS."""

# Connected component functions
def count_components(graph):
    """Count connected components in a graph."""

def find_components(graph):
    """Return list of connected components in a graph."""

def check_component_property(graph, property_checker):
    """Check if components in a graph satisfy a given property."""

def count_components_with_property(graph, property_checker):
    """Count components in a graph that satisfy a given property."""

# Cycle detection and analysis
def is_cyclic(graph):
    """Check if a graph contains cycles."""

def find_cycles(graph):
    """Find all cycles in a graph."""

def is_tree(graph):
    """Determine if a graph forms a tree (connected and acyclic)."""
```

### 5. Grid-based Algorithms

```python
def flood_fill(grid, start_row, start_col, new_value):
    """Fill connected cells with new_value in a grid."""

def count_grid_components(grid, is_valid_cell):
    """Count connected components in a grid."""

def find_grid_cycles(grid, is_valid_cell):
    """Find cycles in a grid-based representation."""

def grid_neighbors(grid, row, col, diagonals=False):
    """Get valid neighbors of a cell in a grid."""
```

## Implementation Strategy

1. Start with the core components that appear most frequently:
   - DisjointSet (DSU/Union-Find)
   - Basic Graph representation
   - Core DFS/BFS implementations
   - Input/Output utilities

2. Implement these components with thorough testing to ensure they work correctly across different problems.

3. As we refactor solutions, add more specialized functions as patterns emerge.

4. Ensure consistent naming conventions, typing, and documentation.

## Refactoring Checklist

We'll use this section to track which problems have been refactored to use the library:

| Problem ID | Refactored | Components Used | Notes |
|------------|------------|-----------------|-------|
| 103_b_cthulhu_4280 | ❌ | | |
| 104_c_cthulhu_10214 | ❌ | | |
| 1169_b_pairs_11885 | ❌ | | |
| 1217_d_coloring_edges_7410 | ❌ | | |
| 1242_b_01_mst_10223 | ❌ | | |
| 1243_d_01_mst_12097 | ❌ | | |
| 1249_b1_books_exchange_easy_version_7099 | ❌ | | |
| 1263_d_secret_passwords_6164 | ❌ | | |
| 1277_e_two_fairs_122 | ❌ | | |
| 1521_d_nastia_plays_with_a_tree_11693 | ❌ | | |
| 1534_f1_falling_sand_easy_version_9507 | ❌ | | |
| 156_d_clues_3678 | ❌ | | |
| 216_b_forming_teams_6387 | ❌ | | |
| 217_a_ice_skating_2223 | ❌ | | |
| 27_b_tournament_1914 | ❌ | | |
| 445_b_dzy_loves_chemistry_1921 | ❌ | | |
| 45_h_road_problem_460 | ❌ | | |
| 505_b_mr_kitayutas_colorful_graph_984 | ❌ | | |
| 505_d_mr_kitayutas_technology_879 | ❌ | | |
| 510_b_fox_and_two_dots_2444 | ❌ | | |
| 653_e_bear_and_forgotten_tree_2_10362 | ❌ | | |
| 659_e_new_reform_13276 | ❌ | | |
| 690_c1_brain_network_easy_6407 | ❌ | | |
| 745_c_hongcow_builds_a_nation_7762 | ❌ | | |
| 771_a_bear_and_friendship_condition_2351 | ❌ | | |
| 791_b_bear_and_friendship_condition_8388 | ❌ | | |
| 920_e_connected_components_167 | ❌ | | |
| 977_e_cyclic_components_8291 | ❌ | | |
| 9_e_interesting_graph_and_apples_483 | ❌ | | |
| 1000_e_we_need_more_bosses_8440 | ❌ | | |

## Update Strategy

As we progress with refactoring, we will:

1. Update this plan with any new patterns we discover
2. Add new library components as needed
3. Track which solutions have been refactored
4. Optimize existing components for maximum code reduction

## Next Steps

1. Implement base library components
2. Begin refactoring simpler problems first to test the library
3. Add more specialized components as needed
4. Continue until all problems are refactored
