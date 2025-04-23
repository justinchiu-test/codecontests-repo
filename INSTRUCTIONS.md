# Instructions for Code Compression Task

This document provides instructions for agents to complete the code compression benchmark task.

## Objective

Your task is to minimize the total amount of code needed to solve all problems by:
1. Identifying common patterns across solutions
2. Creating a shared library of reusable components
3. Refactoring each problem solution to use this library

## Rules and Constraints
You are free to use any bash commands to navigate the repo, such as grep or find.
You are allowed to create files in `library/`, to be used in `problems/*/main.py`.
However, those are the only files you can edit.

### What You Can Modify
- **Library Directory (`library/`)**: You can create, modify, or delete any files in this directory.
- **Problem Solutions (`problems/*/main.py`)**: You can modify the main.py file in each problem directory to utilize your library.

### What You Cannot Modify
- **Problem Descriptions (`problems/*/PROBLEM.md`)**: These files describe the problems and must not be changed.
- **Test Files (`problems/*/tests/`)**: All test files are considered ground truth and must not be modified.
- **Test Scripts (`problems/*/run.sh`)**: These scripts are used to test solutions and must not be changed.
- **Problem Tags (`problems/*/tags.txt`)**: These files contain problem categorization and must not be changed.

## Task Steps

### 1. Analyze Problems

Begin by examining the problems to identify common patterns:
- Look for similar data structures (graphs, trees, etc.)
- Identify recurring algorithms (BFS, DFS, shortest path, etc.)
- Note common input/output patterns
- Find repeated utility functions or helpers

Suggested approach:
```bash
# Get a count of problems
ls -l problems/ | wc -l

# Check common tags
cat problems/*/tags.txt | sort | uniq -c | sort -nr

# Look at a few problem descriptions
cat problems/problem_id/PROBLEM.md

# Examine some solutions
cat problems/problem_id/main.py
```

### 2. Design Library Structure

Based on your analysis, design a modular library with components like:

```
library/
├── __init__.py
├── io/              # Input/output utilities
│   ├── __init__.py
│   ├── parser.py    # Functions to parse common input formats
│   └── formatter.py # Functions to format output
│
├── ds/              # Data structures
│   ├── __init__.py
│   ├── graph.py     # Graph representations
│   └── ...
│
├── algo/            # Algorithms
│   ├── __init__.py
│   ├── search.py    # Search algorithms (BFS, DFS)
│   ├── path.py      # Path-finding algorithms
│   └── ...
│
└── utils/           # Utility functions
    ├── __init__.py
    └── ...
```

### 3. Implement Library Components

Create reusable components in the library directory. Focus on:

- **Input/Output Utilities**:
  - Functions to parse integers, arrays, matrices
  - Functions to parse graph representations
  - Output formatting helpers

- **Data Structures**:
  - Graph representations (adjacency list, matrix)
  - Tree structures
  - Union-find / Disjoint-set
  - Priority queues / Heaps

- **Algorithms**:
  - Graph traversals (BFS, DFS)
  - Shortest path algorithms (Dijkstra's, Bellman-Ford)
  - Minimum spanning tree algorithms
  - Topological sorting
  - Connected components

- **Math Utilities**:
  - Number theory functions
  - Combinatorial calculations
  - Modular arithmetic

### 4. Refactor Problem Solutions

For each problem in the `problems/` directory:

1. Read and understand the original solution in `main.py`
2. Identify which library components can replace parts of the solution
3. Refactor the solution to use your library components
4. Test the refactored solution to ensure it still passes all tests

Example of a refactored solution:

```python
#!/usr/bin/env python3

from library.io.parser import read_graph
from library.ds.graph import AdjacencyList
from library.algo.search import bfs

# Original solution had its own graph parsing, representation, and BFS
# Now we just use the library components

def solve():
    # Parse the input using library function
    n, m, edges = read_graph()

    # Create graph using library data structure
    graph = AdjacencyList(n, directed=False)
    for u, v in edges:
        graph.add_edge(u, v)

    # Run BFS using library algorithm
    distances = bfs(graph, start=0)

    # Output result
    print(max(distances))

if __name__ == "__main__":
    solve()
```

### 5. Test Your Refactored Solutions

For each problem, ensure your refactored solution still passes all tests:

```bash
bash problems/problem_id/run.sh
```

If a solution fails, debug and fix it while still using the library components.

### 6. Evaluate Your Compression

Use the provided evaluation tools to measure your compression success:

```bash
# Count logical lines of code (LLOC)
uv run -m tools.eval.loc problems/*/main.py library/**/*.py

# Calculate log probability (requires TogetherAI API key)
TOGETHER_API_KEY=your_api_key uv run -m tools.eval.log_prob problems/*/main.py
```

## Tips for Success

1. **Start Small**: Begin by implementing a few core components and refactoring a small set of related problems.

2. **Be Consistent**: Use consistent naming conventions and function signatures across your library.

3. **Design for Flexibility**: Make your components adaptable to different problem variations.

4. **Balance Abstraction**: Find the right level of abstraction - too generic may be complex, too specific may not reduce code.

5. **Document Your Library**: Add docstrings explaining parameters, return values, and examples.

6. **Import Efficiently**: Import only what you need in each problem solution.

7. **Preserve Functionality**: Ensure refactored solutions maintain the exact same functionality and output format.

8. **Focus on Common Patterns**: Prioritize implementing components that can be used across many problems.

## Evaluation Criteria

Your solution will be evaluated based on:

1. **Code Reduction**: Total reduction in logical lines of code across all problems
2. **Correctness**: All refactored solutions must pass their original tests
3. **Reusability**: How well library components are reused across different problems
4. **Readability**: Clarity and maintainability of both library and refactored solutions
5. **Log Probability**: How "predictable" the code is from a language model perspective

## Remember

- The goal is to minimize the total code required to solve all problems
- Each solution must still pass all its original tests
- Only modify `library/` and `problems/*/main.py` files
- Never modify problem descriptions, tests, or run scripts
