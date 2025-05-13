 # Plan for Shared Library (library.py)

 ## Goals
 - Centralize common utilities to reduce duplicate code across problem solutions.
 - Provide functions and classes for common patterns: input reading, DSU, DFS/BFS, graph construction, etc.
 - Keep the library minimal and focused: only include components used by multiple problems.
 - Iteratively refine the library while refactoring solutions.

 ## Initial Library Components

 1. Input Utilities
    - `inp()`: Read a stripped line from stdin.
    - `readint()`: Read a single integer.
    - `readints()`: Read a tuple of integers from a line.
    - `readlist()`: Read a list of integers from a line.

 2. Disjoint Set Union (DSU)
    - `class DSU` with:
      - `__init__(n)`: Initialize n elements (0..n-1).
      - `find(x)`: Find representative with path compression.
      - `union(a, b)`: Union two sets, return True if merged.
      - `count`: Track the number of disjoint sets.
      - `size(x)`: Return size of the set containing x.

 3. Graph Traversal
    - `dfs(adj, start, visited=None)`: Iterative DFS; return or update a visited set.
    - `bfs(adj, start, visited=None)`: BFS traversal; return or update a visited set.

 4. Graph Construction
    - `graph(n, edges, directed=False, one_indexed=False)`: Build adjacency list from edge list.

 5. Other Utilities (add later if patterns emerge)
    - Binary search, prefix sums, combination helpers, etc.

 ## Refactoring Workflow

 1. **Implement** the core components in `library.py`.
 2. For **each problem** directory:
    - Remove or replace custom input functions with `inp`, `readint`, etc.
    - Replace manual DSU code with `DSU` from the library.
    - Replace simple `def dfs`/`def bfs` with library functions where signature allows.
    - Use `graph` builder for adjacency list creation when helpful.
    - Run `bash run.sh` to ensure all tests pass.
 3. **Iterate**: as new common patterns are discovered, extend `library.py` and refactor accordingly.
 4. **Clean up**: remove unused functions from `library.py` once all solutions are refactored.

 ## Testing
 - After each refactor, execute:
   ```bash
   bash {problem}/run.sh
   ```
 - Maintain 100% passing tests across all problems.

 *Note:* The plan may evolve; document significant changes here.
