# Claude Usage Guide for CodeContests Repository

This document contains tips and guidelines for working with Claude on this code repository.

## Repository Structure

The repository is structured as follows:
```
codecontests-repo/
├── tools/                  # Repository creation tools
│   ├── dataset/            # For processing the code_contests dataset
│   ├── formatter/          # For formatting problems
│   └── models/             # Pydantic models for problems/solutions
│
├── library/                # Shared library (will be populated during refactoring)
│
├── problems/               # Formatted problems from code_contests
│   └── problem_id/
│       ├── PROBLEM.md      # Problem description
│       ├── main.py         # Python 3 solution
│       ├── run.sh          # Test script
│       └── tests/          # Test cases
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
uv run -m pyright .
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
