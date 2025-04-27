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

Begin by examining every problem to identify common patterns:
- Look for similar data structures, algorithms, and techniques
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

Be sure to examine every problem to get a good idea of what the library should contain.

### 2. Design and Implement Library

Based on your analysis, design and implement a library of reusable components that can be used across multiple problems. The structure and organization of the library is entirely up to you.

You will continue to edit this library as refactor problem solutions. The goal is to maximize reuse and minimize code.

### 3. Refactor Problem Solutions

For each problem in the `problems/` directory:

1. Read and understand the original solution in `main.py`
2. Identify which library components can replace parts of the solution
3. Refactor the solution to use your library components
4. Test the refactored solution to ensure it still passes all tests
5. Continue editing the library as you refactor solutions
6. Ensure all solutions using any changed library functions still pass tests

### 4. Test Your Refactored Solutions

For each problem, ensure your refactored solution still passes all tests:

```bash
bash problems/problem_id/run.sh
```

If a solution fails, debug and fix it while using the library components.
You may edit the library, but ensure that any downstream solutions still pass tests.

### 5. Evaluate Your Compression

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

3. **Balance Abstraction**: Find the right level of abstraction - too generic may be complex, too specific may not reduce code.

4. **Document Your Library**: Add docstrings explaining parameters, return values, and examples.

5. **Focus on Common Patterns**: Prioritize implementing components that can be used across many problems.

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
