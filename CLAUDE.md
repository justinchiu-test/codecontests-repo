# Claude Usage Guide for CodeContests Repository

This document contains tips and guidelines for working with Claude on this code repository.

## Repository Structure

The repository is structured as follows:
```
codecontests-repo/
├── tools/                  # Repository creation tools
│   ├── dataset/            # For processing the code_contests dataset
│   ├── formatter/          # For formatting problems
│   ├── models/             # Pydantic models for problems/solutions
│   │   ├── dataset.py      # Models for code_contests dataset (DatasetProblem, TestSet, Solution)
│   │   ├── problem.py      # Models for our internal representation (Problem, TestCase)
│   │   └── solution.py     # Models for solution tracking
│   │
│   └── eval/               # Evaluation tools
│       ├── loc.py          # Count logical lines of code
│       ├── log_prob.py     # Calculate log probabilities using TogetherAI API
│       └── metrics.py      # Track metrics for comparing solutions
│
├── library/                # Shared library (will be populated during refactoring)
│
├── problems/               # Formatted problems from code_contests (100 graph problems currently)
│   └── problem_id/
│       ├── PROBLEM.md      # Problem description
│       ├── main.py         # Python 3 solution
│       ├── run.sh          # Test script
│       └── tests/          # Test cases
│
├── test/                   # Testing utilities
│   └── validate_models.py  # Validation for Pydantic models
```

## Common Commands

### Testing Problems

To test a specific problem:
```bash
cd problems/problem_id
./run.sh
```

Or from any directory:
```bash
uv run problems/problem_id/main.py < problems/problem_id/tests/input_1.txt
```

### Important: Test Files Protection

The test files in `problems/*/tests/` are considered ground truth and should NOT be modified.
These files are protected by:

1. Git attributes marking them as generated files
2. A pre-commit hook that prevents committing changes to these files
3. Special handling in the codebase

When evaluating solutions, always use the original test files. If you need different test cases for debugging,
create them in a separate location.

### Adding More Problems

To process more problems from the code_contests dataset:
```bash
uv run -m tools.dataset.process
```

### Linting and Type Checking

```bash
uv run -m ruff check .
uv run -m ruff format .
uv run pyright .
```

### Evaluation Tools

To count logical lines of code in a Python file:
```bash
uv run -m tools.eval.loc /path/to/file.py
```

To get log probability scores (requires TogetherAI API key):
```bash
TOGETHER_API_KEY=your_api_key uv run -m tools.eval.log_prob /path/to/file.py
```

### Running Model Validation Tests

```bash
uv run python test/validate_models.py
```

## Workflow Tips

1. When refactoring a solution to use the shared library:
   - First identify common patterns across solutions
   - Extract the pattern into an appropriate module in the library/ directory
   - Update the solution to import and use the shared component
   - Verify the solution still passes all tests

2. When analyzing solutions:
   - Look for common data structure usage
   - Identify repeated I/O patterns
   - Note algorithmic techniques that appear in multiple problems

3. For library development:
   - Keep modules focused on a single responsibility
   - Ensure good test coverage for shared components
   - Maintain backward compatibility with existing solutions
   - Document usage with clear examples

## Project Goals

The main goal is to minimize the total code required to solve the problems by creating reusable components for:

1. Input/output handling
2. Common data structures
3. Algorithm templates
4. Mathematical utilities

This will make solutions more concise, readable, and maintainable.

## Working with stdin/stdout

All problems use stdin for input and stdout for output. The `library.io` module (to be developed) will provide utilities to simplify parsing common input patterns and formatting output.
