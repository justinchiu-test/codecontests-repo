# PLAN for cluster3 library

This document outlines the design of the shared library for cluster3 and the refactoring plan for the problem solutions.

## Goals
- Provide fast and consistent I/O utilities to replace per-solution boilerplate
- Offer common tree and graph algorithms used across the problems:
  - Reading trees (1-indexed or 0-indexed, directed or undirected)
  - BFS and DFS traversals with parent, order, and distance computations
  - Parent-order and children list generation
  - Lowest Common Ancestor (LCA) initialization and distance queries
  - Recursion bootstrap decorator for deep recursion without threading hacks
- Supply simple integer and list parsing helpers

## Library API
1. I/O:
   - `input`: fast line reader (`sys.stdin.readline`)
   - `read_int() -> int`
   - `read_ints() -> List[int]`
   - `read_strs() -> List[str]`
2. Tree/Graph Construction:
   - `read_tree(n, base=1, directed=False) -> List[List[int]]`
3. Traversals & Orders:
   - `bfs(adj, src=0) -> (parent, order, dist)`
   - `par_order(adj, root=0) -> (parent, dfs_order)`
   - `get_children(parent) -> children_list`
4. LCA & Distances:
   - `lca_init(adj, root=0) -> (lca, dist, depth, parent0)`
5. Recursion Helper:
   - `bootstrap(f)`: decorator to convert recursive generators into iterative calls

## Refactoring Strategy
1. **Implement** the above API in `library.py`.
2. **For each** problem directory:
   - Remove custom I/O boilerplate (FastIO, IOWrapper)
   - Remove duplicated traversal or helper functions available in the library
   - Add `from library import *` at the top of `main.py`
   - Replace inline code with calls to the library (e.g. use `read_tree`, `par_order`, `bootstrap`)
   - Ensure that all indexing (0-based vs 1-based) matches the problem requirements
   - Run `run.sh` to verify all tests pass

This plan will consolidate common code into a single, maintainable module and make each solution more concise.
