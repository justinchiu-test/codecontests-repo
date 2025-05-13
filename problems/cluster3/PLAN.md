# Library Plan for Cluster 3 (Tree-based Problems)

After examining the problems in cluster 3, it's clear they primarily deal with tree data structures and algorithms. The library should provide common functionality for:

1. **I/O Operations**
   - Fast input/output for competitive programming
   - Parsing common input formats (tree edges, values on nodes)

2. **Tree Representation**
   - Graph representation (adjacency list)
   - Rooted tree handling
   - Convenience functions for tree operations

3. **Tree Traversal**
   - DFS traversal (both recursive and iterative)
   - BFS traversal
   - Efficient non-recursive traversal for deep trees (trampoline/bootstrap)

4. **Tree Algorithms**
   - Subtree size calculation
   - Tree DP patterns
   - Tree re-rooting technique
   - LCA (Lowest Common Ancestor)
   - Tree diameter calculation
   - Other common tree operations

5. **Utility Functions**
   - Handling defaultdict and other collections
   - Memory-efficient data structures

## Implementation Plan

1. Create a modular library structure to avoid importing unnecessary components:
   - `io`: Fast I/O operations
   - `tree`: Tree representation and basic operations
   - `algorithms`: Advanced tree algorithms
   - `utils`: General utility functions

2. Focus on making the library components flexible enough to be used across different problems but specific enough to significantly reduce code duplication.

3. Ensure the library maintains good performance for competitive programming tasks.

4. Implement functions that can handle the common tree operations observed in the problems:
   - Tree construction from edges
   - Tree traversals (DFS/BFS)
   - Subtree calculations
   - Re-rooting algorithms
   - Dynamic programming on trees

5. Add specialized functions for common patterns seen in multiple problems.

The library will be continually updated as we refactor more solutions and identify additional patterns.