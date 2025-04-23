# Agent Plan for Code Compression Challenge

This document outlines the plan to prepare a dedicated repository for Claude Code to work on compressing competitive programming solutions using a shared library approach.

## Objective

Create a streamlined repository with selected competitive programming problems and minimal infrastructure to allow Claude Code to:
1. Analyze solution patterns across problems
2. Create a shared library of reusable components
3. Refactor solutions to use the library
4. Measure the code reduction achieved

## Repository Structure

```
codecontests-agent/
├── problems/                # Selected problems (organized by category)
│   ├── graph/               # Graph algorithm problems
│   │   ├── problem_id_1/    # Individual problem directories
│   │   │   ├── PROBLEM.md   # Problem description
│   │   │   ├── main.py      # Original solution
│   │   │   ├── run.sh       # Test script
│   │   │   └── tests/       # Test cases
│   │   └── ...
│   │
│   ├── dp/                  # Dynamic programming problems (if needed)
│   └── ...
│
├── library/                 # Shared library (initially empty)
│   ├── __init__.py
│   ├── graph/               # For graph algorithms
│   │   └── __init__.py
│   ├── io/                  # For input/output handling
│   │   └── __init__.py
│   └── README.md            # Instructions for library development
│
├── utils/                   # Utility scripts
│   ├── metrics.py           # For measuring compression
│   ├── run_tests.py         # For running tests
│   └── compare.py           # For comparing original vs compressed
│
├── README.md                # Main instructions for Claude Code
└── TASKS.md                 # Specific tasks broken down by phase
```

## Implementation Plan

### Phase 1: Repository Preparation

1. **Create New Repository**
   ```bash
   mkdir -p codecontests-claude
   cd codecontests-claude
   git init
   ```

2. **Create Directory Structure**
   ```bash
   mkdir -p problems/{graph,dp,math,strings,implementation}
   mkdir -p library/{graph,io,ds,algo,math,utils}
   mkdir -p examples/{original,compressed}
   mkdir -p utils
   ```

3. **Prepare Library Infrastructure**
   ```bash
   # Create __init__.py files for proper imports
   touch library/__init__.py
   touch library/graph/__init__.py
   touch library/io/__init__.py
   # ... for other library directories
   ```

### Phase 2: Problem Selection and Preparation

1. **Select Representative Problems**
   - Choose ~20-30 problems that cover common graph algorithm patterns
   - Focus on problems with clearly identifiable patterns that can benefit from shared code
   - Ensure a mix of difficulty levels and algorithm types

2. **Copy Problem Files**
   ```bash
   # For each selected problem
   cp -r /Users/justinchiu/code/codecontests-repo/problems/PROBLEM_ID codecontests-claude/problems/graph/
   ```

3. **Organize by Category**
   - Graph traversal (DFS, BFS)
   - Shortest paths (Dijkstra, Floyd-Warshall)
   - Minimum spanning trees
   - Connected components
   - Topological sorting
   - Flow networks (if available)

### Phase 3: Utility Scripts Development

1. **Metrics Utility**
   Create `utils/metrics.py` with:
   - LLOC (Logical Lines of Code) counter
   - Compression ratio calculator
   - Summary statistics generator

```python
import ast
import os
import glob
from typing import Dict, List, Tuple, Any

def count_lloc(file_path: str) -> int:
    """Count logical lines of code in a Python file using AST."""
    with open(file_path, 'r') as f:
        try:
            tree = ast.parse(f.read())
            return sum(isinstance(node, (ast.stmt)) for node in ast.walk(tree))
        except SyntaxError:
            print(f"Syntax error in {file_path}")
            return 0

def measure_compression(original_dir: str, compressed_dir: str) -> Dict[str, Any]:
    """Measure compression between original and compressed solutions."""
    original_files = glob.glob(os.path.join(original_dir, "**/*.py"), recursive=True)
    compressed_files = glob.glob(os.path.join(compressed_dir, "**/*.py"), recursive=True)

    original_lloc = sum(count_lloc(f) for f in original_files)
    compressed_lloc = sum(count_lloc(f) for f in compressed_files)
    library_lloc = sum(count_lloc(f) for f in glob.glob("library/**/*.py", recursive=True))

    total_compressed = compressed_lloc + library_lloc
    compression_ratio = (original_lloc - total_compressed) / original_lloc * 100 if original_lloc > 0 else 0

    return {
        "original_lloc": original_lloc,
        "compressed_lloc": compressed_lloc,
        "library_lloc": library_lloc,
        "total_compressed": total_compressed,
        "compression_ratio": compression_ratio,
        "num_original_files": len(original_files),
        "num_compressed_files": len(compressed_files)
    }

def print_compression_report(results: Dict[str, Any]) -> None:
    """Print a formatted compression report."""
    print("\n=== COMPRESSION REPORT ===")
    print(f"Original LLOC: {results['original_lloc']}")
    print(f"Compressed solution LLOC: {results['compressed_lloc']}")
    print(f"Library LLOC: {results['library_lloc']}")
    print(f"Total compressed LLOC: {results['total_compressed']}")
    print(f"Compression ratio: {results['compression_ratio']:.2f}%")
    print(f"Files analyzed: {results['num_original_files']} original, {results['num_compressed_files']} compressed")
    print("==========================\n")

if __name__ == "__main__":
    # Example usage
    results = measure_compression("problems", "compressed_solutions")
    print_compression_report(results)
```

2. **Test Runner**
   Create `utils/run_tests.py` for validating solutions:

```python
import os
import subprocess
import glob
import sys
from typing import Dict, List, Any

def run_test(problem_dir: str, solution_file: str) -> List[Dict[str, Any]]:
    """Run tests for a given problem and solution file."""
    results = []
    test_dir = os.path.join(problem_dir, "tests")

    if not os.path.exists(test_dir):
        print(f"Error: Test directory not found for {problem_dir}")
        return results

    input_files = sorted(glob.glob(os.path.join(test_dir, "input_*.txt")))

    for input_file in input_files:
        basename = os.path.basename(input_file)
        test_num = basename.split("_")[1].split(".")[0]
        output_file = os.path.join(test_dir, f"output_{test_num}.txt")

        if not os.path.exists(output_file):
            print(f"Warning: Missing output file for test {test_num}")
            continue

        with open(input_file, "r") as f:
            input_data = f.read()
        with open(output_file, "r") as f:
            expected_output = f.read().strip()

        try:
            process = subprocess.run(
                [sys.executable, solution_file],
                input=input_data,
                text=True,
                capture_output=True,
                timeout=5  # 5 second timeout
            )
            actual_output = process.stdout.strip()
            stderr = process.stderr.strip()

            passed = actual_output == expected_output

            results.append({
                "test": test_num,
                "passed": passed,
                "expected": expected_output,
                "actual": actual_output,
                "stderr": stderr if stderr else None
            })
        except subprocess.TimeoutExpired:
            results.append({
                "test": test_num,
                "passed": False,
                "error": "Timeout expired"
            })
        except Exception as e:
            results.append({
                "test": test_num,
                "passed": False,
                "error": str(e)
            })

    return results

def run_all_tests(solution_dir: str, pattern: str = "main.py") -> Dict[str, Any]:
    """Run tests for all solutions matching a pattern."""
    summary = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "problem_results": {}
    }

    problems = [d for d in os.listdir(solution_dir) if os.path.isdir(os.path.join(solution_dir, d))]

    for problem in problems:
        problem_dir = os.path.join(solution_dir, problem)
        solution_file = os.path.join(problem_dir, pattern)

        if not os.path.exists(solution_file):
            print(f"Skipping {problem}: No solution file {pattern} found")
            continue

        print(f"Testing {problem}...")
        test_results = run_test(problem_dir, solution_file)

        if not test_results:
            print(f"No tests run for {problem}")
            continue

        total_tests = len(test_results)
        passed_tests = sum(1 for r in test_results if r.get("passed", False))

        summary["total"] += total_tests
        summary["passed"] += passed_tests
        summary["failed"] += (total_tests - passed_tests)

        problem_status = "PASSED" if passed_tests == total_tests else "FAILED"
        print(f"{problem}: {passed_tests}/{total_tests} tests passed - {problem_status}")

        summary["problem_results"][problem] = {
            "total": total_tests,
            "passed": passed_tests,
            "status": problem_status,
            "details": test_results
        }

    return summary

def print_test_summary(summary: Dict[str, Any]) -> None:
    """Print a formatted test summary."""
    print("\n=== TEST SUMMARY ===")
    print(f"Total tests: {summary['total']}")
    print(f"Passed tests: {summary['passed']}")
    print(f"Failed tests: {summary['failed']}")
    pass_rate = summary['passed'] / summary['total'] * 100 if summary['total'] > 0 else 0
    print(f"Pass rate: {pass_rate:.2f}%")

    print("\nProblem Status:")
    for problem, result in summary["problem_results"].items():
        status = "✅" if result["status"] == "PASSED" else "❌"
        print(f"{status} {problem}: {result['passed']}/{result['total']} tests passed")
    print("===================\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        solution_dir = sys.argv[1]
        pattern = sys.argv[2] if len(sys.argv) > 2 else "main.py"
    else:
        solution_dir = "problems"
        pattern = "main.py"

    summary = run_all_tests(solution_dir, pattern)
    print_test_summary(summary)
```

3. **Comparison Utility**
   Create `utils/compare.py` for comparing original and compressed solutions:

```python
import os
import sys
from typing import Dict, List, Any
import difflib
from metrics import count_lloc
import glob

def compare_solutions(original_file: str, compressed_file: str) -> Dict[str, Any]:
    """Compare original and compressed solutions."""
    if not os.path.exists(original_file) or not os.path.exists(compressed_file):
        return {"error": "One or both files do not exist"}

    with open(original_file, 'r') as f:
        original_code = f.readlines()

    with open(compressed_file, 'r') as f:
        compressed_code = f.readlines()

    diff = list(difflib.unified_diff(
        original_code,
        compressed_code,
        fromfile='original',
        tofile='compressed',
        lineterm=''
    ))

    original_lloc = count_lloc(original_file)
    compressed_lloc = count_lloc(compressed_file)

    reduction = (original_lloc - compressed_lloc) / original_lloc * 100 if original_lloc > 0 else 0

    return {
        "original_lloc": original_lloc,
        "compressed_lloc": compressed_lloc,
        "reduction_percentage": reduction,
        "diff": diff
    }

def find_solution_pairs(original_dir: str, compressed_dir: str) -> List[Dict[str, str]]:
    """Find matching solution files between original and compressed directories."""
    pairs = []

    original_files = glob.glob(os.path.join(original_dir, "**", "main.py"), recursive=True)

    for original_file in original_files:
        # Extract relative path
        rel_path = os.path.relpath(original_file, original_dir)
        compressed_file = os.path.join(compressed_dir, rel_path)

        if os.path.exists(compressed_file):
            pairs.append({
                "problem": os.path.dirname(rel_path),
                "original": original_file,
                "compressed": compressed_file
            })

    return pairs

def print_comparison_report(pairs: List[Dict[str, str]]) -> None:
    """Print comparison report for all solution pairs."""
    print("\n=== SOLUTION COMPARISON REPORT ===")

    total_original_lloc = 0
    total_compressed_lloc = 0

    for pair in pairs:
        problem = pair["problem"]
        result = compare_solutions(pair["original"], pair["compressed"])

        if "error" in result:
            print(f"{problem}: Error - {result['error']}")
            continue

        total_original_lloc += result["original_lloc"]
        total_compressed_lloc += result["compressed_lloc"]

        print(f"{problem}:")
        print(f"  Original LLOC: {result['original_lloc']}")
        print(f"  Compressed LLOC: {result['compressed_lloc']}")
        print(f"  Reduction: {result['reduction_percentage']:.2f}%")

    if total_original_lloc > 0:
        overall_reduction = (total_original_lloc - total_compressed_lloc) / total_original_lloc * 100
        print("\nOverall:")
        print(f"  Total Original LLOC: {total_original_lloc}")
        print(f"  Total Compressed LLOC: {total_compressed_lloc}")
        print(f"  Overall Reduction: {overall_reduction:.2f}%")

    print("==================================\n")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        original_dir = sys.argv[1]
        compressed_dir = sys.argv[2]
    else:
        original_dir = "problems"
        compressed_dir = "compressed_solutions"

    pairs = find_solution_pairs(original_dir, compressed_dir)
    print(f"Found {len(pairs)} solution pairs")
    print_comparison_report(pairs)
```

### Phase 4: Instruction Documentation

1. **Main README.md**
   Create clear instructions for Claude Code:

```markdown
# Code Contests Compression Challenge

This repository contains competitive programming solutions from the DeepMind Code Contests dataset. Your task is to compress these solutions by creating a shared library of reusable components.

## Goal

Reduce the total lines of code across all problem solutions while maintaining correctness and readability. You should:

1. Identify common patterns and algorithms across multiple problems
2. Create a shared library with reusable components
3. Refactor the original solutions to use your library
4. Measure the code reduction achieved

## Repository Structure

- `problems/` - Original problem solutions organized by category
- `library/` - Shared code library (your main development area)
- `examples/` - Examples of successful compression (for reference)
- `utils/` - Utility scripts for testing and measuring

## Getting Started

1. **Analyze the Problems**:
   - Explore problems in the `problems/` directory
   - Look for common patterns in problem-solving approaches
   - Identify recurring algorithms, data structures, and I/O patterns

2. **Plan Your Library**:
   - Design a modular structure for your shared library
   - Determine the right level of abstraction for components
   - Focus on flexibility and reusability

3. **Implement the Library**:
   - Create reusable components in the `library/` directory
   - Implement common graph algorithms, data structures, and utilities
   - Add clear documentation and type hints

4. **Refactor Solutions**:
   - Create compressed versions of the original solutions using your library
   - Follow a consistent pattern for imports and usage
   - Maintain correctness - all test cases must still pass!

5. **Measure Your Progress**:
   - Use the utility scripts to measure code reduction
   - Run tests to ensure solutions still work correctly
   - Compare your results with the original code

## Evaluation

Your work will be evaluated based on:

- Total reduction in logical lines of code (LLOC)
- Correctness (all test cases must pass)
- Library design and organization
- Code readability and documentation

## Working with the Utilities

### Running Tests

To test a solution against its test cases:

```bash
python utils/run_tests.py problems/graph/problem_id
```

To test all solutions:

```bash
python utils/run_tests.py problems
```

### Measuring Compression

To measure the compression achieved:

```bash
python utils/metrics.py
```

### Comparing Solutions

To compare original and compressed solutions:

```bash
python utils/compare.py problems compressed_solutions
```

## Tips for Success

- Start by focusing on core graph algorithms that appear frequently
- Create utilities for common input/output patterns
- Use consistent naming and organization in your library
- Prioritize problems by how much they could benefit from shared code
- Test frequently to ensure solutions remain correct
```

2. **Library README.md**
   Provide guidance for building the library:

```markdown
# Library Development Guide

This directory is where you'll implement your shared code library. The goal is to create reusable components that can be used across multiple problem solutions.

## Suggested Organization

- `graph/` - Graph algorithms and data structures
  - `traversal.py` - DFS, BFS, and related algorithms
  - `shortest_path.py` - Dijkstra, Floyd-Warshall, etc.
  - `mst.py` - Minimum spanning tree algorithms
  - `components.py` - Connected components, strongly connected components
  - `topo_sort.py` - Topological sorting algorithms

- `io/` - Input/output utilities
  - `parser.py` - Functions for parsing common input formats
  - `formatter.py` - Functions for formatting output

- `ds/` - General data structures
  - `union_find.py` - Union-Find (Disjoint Set) implementation
  - `heap.py` - Priority queue implementations
  - `tree.py` - Tree representations

- `utils/` - General utilities
  - `decorators.py` - Useful decorators (timing, memoization, etc.)
  - `generators.py` - Generator functions

## Implementation Guidelines

1. **Modularity**:
   - Keep components focused on specific functionality
   - Design for composition rather than inheritance
   - Use intuitive interfaces that hide implementation details

2. **Documentation**:
   - Add clear docstrings explaining purpose and usage
   - Include type hints for better IDE support
   - Add examples for non-trivial functions

3. **Performance**:
   - Consider time and space complexity
   - Use appropriate data structures for the problem
   - Balance abstraction with performance

4. **Flexibility**:
   - Parameterize functions to handle variations
   - Allow for customization where appropriate
   - Design for reuse across multiple problem types

## Example Component

Here's an example of how a well-designed component might look:

```python
from typing import Dict, List, Set, TypeVar, Generic, Optional, Callable

T = TypeVar('T')

class Graph(Generic[T]):
    """
    A generic graph representation using adjacency lists.

    This class provides a flexible graph implementation that supports
    both directed and undirected graphs, with or without weights.

    Examples:
        # Create an undirected graph
        g = Graph(directed=False)
        g.add_edge(1, 2)
        g.add_edge(2, 3)

        # Create a weighted directed graph
        g = Graph(directed=True, weighted=True)
        g.add_edge(1, 2, 5)
        g.add_edge(2, 3, 7)
    """

    def __init__(self, directed: bool = False, weighted: bool = False):
        """
        Initialize a new graph.

        Args:
            directed: Whether the graph is directed
            weighted: Whether the graph has weights on edges
        """
        self.directed = directed
        self.weighted = weighted
        self.adj: Dict[T, List] = {}

    def add_vertex(self, v: T) -> None:
        """
        Add a vertex to the graph if it doesn't already exist.

        Args:
            v: The vertex to add
        """
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u: T, v: T, weight: float = 1.0) -> None:
        """
        Add an edge between vertices u and v.

        Args:
            u: The first vertex
            v: The second vertex
            weight: The edge weight (only used if the graph is weighted)
        """
        self.add_vertex(u)
        self.add_vertex(v)

        if self.weighted:
            self.adj[u].append((v, weight))
            if not self.directed:
                self.adj[v].append((u, weight))
        else:
            self.adj[u].append(v)
            if not self.directed:
                self.adj[v].append(u)

    def neighbors(self, v: T) -> List:
        """
        Get all neighbors of vertex v.

        Args:
            v: The vertex to get neighbors for

        Returns:
            A list of neighbors (or (neighbor, weight) tuples if weighted)
        """
        return self.adj.get(v, [])

    def vertices(self) -> Set[T]:
        """
        Get all vertices in the graph.

        Returns:
            A set of all vertices
        """
        return set(self.adj.keys())

    def bfs(self, start: T, visit_fn: Optional[Callable[[T], None]] = None) -> Set[T]:
        """
        Perform breadth-first search starting from vertex.

        Args:
            start: The starting vertex
            visit_fn: Optional function to call on each visited vertex

        Returns:
            Set of vertices reachable from the start vertex
        """
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            if visit_fn:
                visit_fn(vertex)

            for neighbor in self.neighbors(vertex):
                neighbor_node = neighbor if not self.weighted else neighbor[0]
                if neighbor_node not in visited:
                    visited.add(neighbor_node)
                    queue.append(neighbor_node)

        return visited
```
```

3. **TASKS.md**
   Break down the work into specific tasks:

```markdown
# Tasks for Code Compression

This document outlines the specific tasks for creating a code compression library.

## Phase 1: Analysis

1. **Inventory Problems**
   - Review all problems in the `problems/` directory
   - Categorize them by algorithm type and pattern
   - Identify the most common operations and structures

2. **Pattern Identification**
   - Look for recurring code patterns like:
     - Graph representation (adjacency list, matrix)
     - Graph traversal (DFS, BFS)
     - Shortest path algorithms
     - Common input parsing patterns
     - Standard output formatting

3. **Prioritization**
   - Rank patterns by frequency and potential for compression
   - Identify "quick wins" vs. more complex abstractions

## Phase 2: Library Design

1. **Core Components**
   - Design a graph representation class
   - Create basic traversal algorithms (DFS, BFS)
   - Implement shortest path algorithms (Dijkstra, Floyd-Warshall)
   - Add connected components algorithms

2. **I/O Utilities**
   - Create parsers for common input formats
   - Implement formatters for standard output patterns
   - Add utilities for matrix input/output

3. **Supporting Structures**
   - Implement Union-Find (Disjoint Set) data structure
   - Create priority queue implementations
   - Add tree representations if needed

## Phase 3: Implementation

1. **Basic Library**
   - Implement core graph representation
   - Add traversal algorithms
   - Create I/O utilities

2. **Extended Components**
   - Add path-finding algorithms
   - Implement MST algorithms
   - Create topological sorting

3. **Advanced Features**
   - Add flow network algorithms
   - Implement bipartite graph utilities
   - Create cycle detection algorithms

## Phase 4: Refactoring

1. **Sample Refactoring**
   - Take 5 representative problems
   - Refactor them to use the library
   - Verify they still pass all tests

2. **Systematic Refactoring**
   - Refactor all remaining problems
   - Organize solutions consistently
   - Document the refactoring approach

3. **Optimization**
   - Review compressed solutions for further improvements
   - Optimize library components for performance
   - Look for opportunities to merge related components

## Phase 5: Evaluation

1. **Metrics Collection**
   - Measure LLOC for original and compressed solutions
   - Calculate overall compression ratio
   - Analyze compression by problem category

2. **Correctness Verification**
   - Run all test cases on compressed solutions
   - Ensure no regressions in functionality
   - Document any edge cases or limitations

3. **Documentation**
   - Create comprehensive library documentation
   - Add usage examples for each component
   - Document the compression methodology
```

### Phase 5: Example Implementation

Create examples of successful compression to guide Claude Code:

1. **Original Solution Example**
   `examples/original/bfs_example.py`:

```python
def solve():
    n, m = map(int, input().split())

    # Create adjacency list
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)  # Undirected graph

    # Start BFS from node 1
    visited = [False] * (n+1)
    queue = [1]
    visited[1] = True

    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    # Count visited nodes
    count = sum(visited) - 1  # Subtract 1 because we're not counting node 0
    print(count)

if __name__ == "__main__":
    solve()
```

2. **Compressed Solution Example**
   `examples/compressed/bfs_example.py`:

```python
from library.graph.traversal import Graph

def solve():
    n, m = map(int, input().split())

    # Create graph using library
    graph = Graph(directed=False)

    # Add edges
    for _ in range(m):
        a, b = map(int, input().split())
        graph.add_edge(a, b)

    # Use the built-in BFS function
    visited = graph.bfs(1)

    # Count visited nodes (excluding node 0 which doesn't exist)
    count = len(visited)
    print(count)

if __name__ == "__main__":
    solve()
```

3. **Library Implementation Example**
   `examples/library/graph/traversal.py`:

```python
from typing import Dict, List, Set, TypeVar, Generic, Optional, Callable, Deque
from collections import deque

T = TypeVar('T')

class Graph(Generic[T]):
    """A generic graph representation using adjacency lists."""

    def __init__(self, directed: bool = False, weighted: bool = False):
        """
        Initialize a new graph.

        Args:
            directed: Whether the graph is directed
            weighted: Whether the graph has weights on edges
        """
        self.directed = directed
        self.weighted = weighted
        self.adj: Dict[T, List] = {}

    def add_vertex(self, v: T) -> None:
        """Add a vertex to the graph if it doesn't already exist."""
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u: T, v: T, weight: float = 1.0) -> None:
        """Add an edge between vertices u and v."""
        self.add_vertex(u)
        self.add_vertex(v)

        if self.weighted:
            self.adj[u].append((v, weight))
            if not self.directed:
                self.adj[v].append((u, weight))
        else:
            self.adj[u].append(v)
            if not self.directed:
                self.adj[v].append(u)

    def neighbors(self, v: T) -> List:
        """Get all neighbors of vertex v."""
        return self.adj.get(v, [])

    def vertices(self) -> Set[T]:
        """Get all vertices in the graph."""
        return set(self.adj.keys())

    def bfs(self, start: T, visit_fn: Optional[Callable[[T], None]] = None) -> Set[T]:
        """
        Perform breadth-first search starting from vertex.

        Args:
            start: The starting vertex
            visit_fn: Optional function to call on each visited vertex

        Returns:
            Set of vertices reachable from the start vertex
        """
        if start not in self.adj:
            return set()

        visited = set([start])
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if visit_fn:
                visit_fn(vertex)

            for neighbor in self.neighbors(vertex):
                neighbor_node = neighbor if not self.weighted else neighbor[0]
                if neighbor_node not in visited:
                    visited.add(neighbor_node)
                    queue.append(neighbor_node)

        return visited

    def dfs(self, start: T, visit_fn: Optional[Callable[[T], None]] = None) -> Set[T]:
        """
        Perform depth-first search starting from vertex.

        Args:
            start: The starting vertex
            visit_fn: Optional function to call on each visited vertex

        Returns:
            Set of vertices reachable from the start vertex
        """
        if start not in self.adj:
            return set()

        visited = set()

        def dfs_recursive(v: T):
            visited.add(v)
            if visit_fn:
                visit_fn(v)

            for neighbor in self.neighbors(v):
                neighbor_node = neighbor if not self.weighted else neighbor[0]
                if neighbor_node not in visited:
                    dfs_recursive(neighbor_node)

        dfs_recursive(start)
        return visited
```

## Deployment Steps

1. **Prepare the Repository**
   ```bash
   # Create new repo
   mkdir codecontests-claude
   cd codecontests-claude
   git init

   # Create directory structure
   mkdir -p problems/{graph,dp,math}
   mkdir -p library/{graph,io,ds,algo,math,utils}
   mkdir -p examples/{original,compressed,library/graph}
   mkdir -p utils

   # Create initial files
   touch README.md TASKS.md
   touch library/__init__.py
   ```

2. **Copy Selected Problems**
   ```bash
   # Select ~20-30 graph problems from the original repo
   # Copy them to the new repo
   cp -r /path/to/original/problems/selected_problem_id codecontests-claude/problems/graph/
   ```

3. **Create Utility Scripts**
   ```bash
   # Create the metrics, testing, and comparison utilities
   touch utils/metrics.py utils/run_tests.py utils/compare.py
   # Implement as detailed above
   ```

4. **Add Documentation**
   ```bash
   # Create README.md, TASKS.md, and library README.md
   # Implement as detailed above
   ```

5. **Prepare Examples**
   ```bash
   # Add example implementations
   touch examples/original/bfs_example.py
   touch examples/compressed/bfs_example.py
   touch examples/library/graph/traversal.py
   # Implement as detailed above
   ```

6. **Finalize Repository**
   ```bash
   # Commit all files
   git add .
   git commit -m "Initial setup for code compression challenge"

   # Create remote repository
   # Push to GitHub or other hosting service
   git remote add origin https://github.com/yourusername/codecontests-claude.git
   git push -u origin main
   ```

## Success Criteria

The deployment will be considered successful if:

1. The repository contains a representative selection of graph problems
2. All utility scripts work correctly
3. Documentation clearly explains the tasks and objectives
4. Claude Code can successfully:
   - Analyze the problems
   - Create a shared library
   - Refactor solutions
   - Measure the compression achieved

## Next Steps After Deployment

1. Monitor Claude Code's progress and provide feedback
2. Evaluate the compression results
3. Consider adding more problem categories if successful
4. Document the patterns identified and compression techniques used
