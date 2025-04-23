# CodeContests Compression Benchmark Plan

## Objective
Create a benchmark for measuring how well an agent can compress competitive programming solutions by identifying and extracting common patterns into a shared library.

## Overview
This benchmark consists of three main components:

1. **Repository Creation Tools**: Scripts to process the DeepMind Code Contests dataset and format problems in a standardized way.
2. **Problem Benchmark**: 100 graph problems (currently) formatted into a consistent structure with tests.
3. **Compression Task**: Instructions for an agent to create a shared library that minimizes total code across solutions.

## Part 1: Repository Creation Tools

The tools directory contains utilities to process the DeepMind Code Contests dataset into a standardized format:

```
tools/
├── dataset/             # Dataset processing utilities
│   └── process.py       # Process and format problems with filtering options
│
├── formatter/           # Problem formatting utilities
│   ├── problem_md.py    # Generate PROBLEM.md files
│   └── script_sh.py     # Generate run.sh test scripts
│
├── models/              # Pydantic data models
│   ├── dataset.py       # Models for the dataset structure
│   ├── problem.py       # Models for problem representation
│   └── solution.py      # Models for solution tracking
│
└── eval/                # Evaluation tools
    ├── loc.py           # Count logical lines of code in solutions
    ├── log_prob.py      # Calculate log probabilities using TogetherAI
    └── metrics.py       # Track code reduction metrics
```

### Problem Processing Flow

1. Download problems from the DeepMind Code Contests dataset
2. Filter problems by tag (if specified) and convert to Pydantic models
3. Extract Python 3 solutions and test cases
4. Generate standardized problem files (PROBLEM.md, main.py, run.sh, tags.txt)
5. Create test cases in a structured format

### Command Line Interface

The dataset processing tool supports:
- Optional tag filtering (e.g., `--tag graphs`)
- Optional limit on number of problems (e.g., `--limit 100`)

Example usage:
```bash
# Process all problems
uv run -m tools.dataset.process

# Process only graph problems, up to 100
uv run -m tools.dataset.process --tag graphs --limit 100
```

## Part 2: Problem Benchmark

The benchmark currently contains 100 graph problems formatted in a consistent structure:

```
problems/
└── problem_id/          # Each problem in its own directory
    ├── PROBLEM.md       # Problem description in Markdown
    ├── main.py          # Original Python solution
    ├── run.sh           # Test script to run the solution
    ├── tags.txt         # Original Codeforces tags
    └── tests/           # Input/output test pairs
        ├── input_1.txt  # Test inputs
        └── output_1.txt # Expected outputs
```

Each problem directory includes:
- A consistent problem description format
- The original solution from the dataset
- Test cases with inputs and expected outputs
- A shell script to run tests automatically
- The original problem tags from Codeforces

### Testing

Solutions can be tested using:
```bash
# Test a specific problem
cd problems/problem_id
./run.sh

# Or from any directory
uv run problems/problem_id/main.py < problems/problem_id/tests/input_1.txt
```

### Scale

The benchmark is designed to scale:
- Currently contains 100 graph problems
- Can be expanded to include more problems of different types
- The dataset processing tool allows filtering by any tag

## Part 3: Compression Task (Instructions for Agents)

This is the core benchmark task: create a shared library in the `library/` directory that minimizes the total amount of code needed across all problems.

### Task Description for Agents

1. **Analyze Problem Set**:
   - Examine the 100 graph problems in the `problems/` directory
   - Identify common patterns, algorithms, data structures, and I/O operations
   - Look for opportunities to abstract and reuse code

2. **Create Library Components**:
   - Implement data structure abstractions (graphs, trees, heaps, etc.)
   - Create algorithm templates (search, traversal, shortest path, etc.)
   - Build I/O utilities for common input/output patterns
   - Develop math utilities for recurring calculations

3. **Refactor Solutions**:
   - Update each problem's `main.py` to use the shared library
   - Ensure all tests still pass after refactoring
   - Maintain solution correctness while reducing code duplication

4. **Measure Improvement**:
   - Calculate logical lines of code (LLOC) before and after refactoring
   - Compute log probability as a measure of code predictability
   - Track code reuse percentage across problems
   - Compare execution time to ensure no significant performance degradation

### Specific Library Components to Consider

1. **Input/Output Utilities**:
   - Parsing integers, arrays, strings, and nested structures
   - Parsing graph representations (adjacency lists, matrices)
   - Formatting outputs according to problem requirements

2. **Graph Algorithm Templates**:
   - Graph representations (directed, undirected, weighted)
   - Search algorithms (DFS, BFS)
   - Shortest path algorithms (Dijkstra's, Bellman-Ford)
   - Connected components and cycle detection
   - Minimum spanning trees
   - Topological sorting

3. **Data Structures**:
   - Priority queues and custom heaps
   - Union-find / Disjoint-set data structures
   - Tree representations and traversals
   - Special purpose graph structures

4. **Math Utilities**:
   - Number theory functions
   - Combinatorial calculations
   - Modular arithmetic

## Evaluation Metrics

The benchmark will evaluate compression success using:

1. **Code Reduction**:
   - Total Lines of Code (LOC) reduction
   - Logical Lines of Code (LLOC) reduction using AST parsing
   - Code reuse percentage across the problem set

2. **Code Quality**:
   - Log probability: How "predictable" the code is from a language model perspective
   - Execution time: Performance impact of refactoring
   - Maintainability metrics

## Current Progress

### Completed
1. ✅ Repository structure and configuration
2. ✅ Dataset processing tools implementation
3. ✅ Problem formatting with standardized structure
4. ✅ Test script generation and execution
5. ✅ Pydantic models for dataset, problems, and solutions
6. ✅ Evaluation tools for measuring code metrics
7. ✅ Processing of 100 graph-labeled problems
8. ✅ Addition of Codeforces tags for each problem

### Next Steps
1. Develop instructions for an agent to perform the compression task
2. Define evaluation criteria for comparing different compression approaches
3. Create a baseline implementation of the shared library
4. Develop automated testing to verify correctness after refactoring
