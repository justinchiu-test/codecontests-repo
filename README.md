# CodeContests Refactoring Project

This repository provides a framework for refactoring solutions from the [DeepMind Code Contests dataset](https://huggingface.co/datasets/deepmind/code_contests).

## Project Goal

The primary objective is to create a shared library that minimizes the total code required to solve competitive programming problems by identifying and extracting common patterns, algorithms, and utilities.

## Repository Organization

The project is organized into three main components:

1. **Tools for Repository Creation**: Utilities to download and format problems from the code_contests dataset, creating standardized problem descriptions, initial solutions, and test scripts.

2. **Shared Library**: Reusable components that solutions can import to reduce duplicate code, including I/O utilities, data structures, algorithms, and math functions.

3. **Formatted Problems**: The actual competitive programming problems, each with a problem description (PROBLEM.md), initial solution (main.py), test script (run.sh), and test cases.

## Structure

```
codecontests-repo/
├── tools/                  # Repository creation tools
│   ├── dataset/            # Dataset processing
│   ├── formatter/          # Problem formatting 
│   └── models/             # Pydantic data models
│
├── library/                # Shared library components
│
├── problems/               # Formatted problems
│   └── problem_id/
│       ├── PROBLEM.md      # Problem description
│       ├── main.py         # Initial solution
│       ├── run.sh          # Test script
│       └── tests/          # Input/output test cases
│
├── data/                   # Raw dataset (gitignored)
└── scripts/                # Utility scripts
```

## Getting Started

```bash
# Install dependencies
uv pip install -e "."

# Download and format problems
uv run -m tools.dataset.download
uv run -m tools.dataset.process

# Run tests for a specific problem
cd problems/problem_id
./run.sh

# Or run directly from any directory
uv run problems/problem_id/main.py < problems/problem_id/tests/input_1.txt
```

## Features

- Standardized problem representation using Pydantic
- Automated test script generation for stdin/stdout testing
- Shared library for common algorithms and data structures
- I/O utilities for parsing competitive programming inputs
- Tools for measuring code reduction and performance

## Plan

For the detailed refactoring approach and roadmap, see [PLAN.md](PLAN.md).