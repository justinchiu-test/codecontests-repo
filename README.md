# CodeContests Compression Benchmark

This repository provides a benchmark compression solutions to the [DeepMind Code Contests dataset](https://huggingface.co/datasets/deepmind/code_contests).

## Project Goal

The primary objective is to create a shared library that minimizes the total code required to jointly solve competitive programming problems by identifying and extracting common patterns, algorithms, and utilities. We aim to:

1. Reduce the amount of code needed per solution through abstraction and reuse
2. Improve code readability and maintainability
3. Provide optimized implementations of common algorithms and data structures
4. Quantify improvements using metrics like logical lines of code (LLOC) and log probability

## Repository Organization

The project is organized into three main components:

1. **Tools for Repository Creation**: Utilities to download and format problems from the code_contests dataset, creating standardized problem descriptions, initial solutions, and test scripts.

2. **Formatted Problems**: The actual competitive programming problems, each with a problem description (PROBLEM.md), initial solution (main.py), test script (run.sh), and test cases.

3. **Shared Library**: Reusable components that solutions can import to reduce duplicate code. Initially empty for an Agent to populate following the instructions in [INSTRUCTIONS.md](INSTRUCTIONS.md).


## Structure

```
codecontests-repo/
├── tools/                  # Repository creation tools
│   ├── dataset/            # Dataset processing
│   │   └── process.py      # Process and format problems
│   │
│   ├── formatter/          # Problem formatting
│   │   ├── problem_md.py   # Format problem descriptions
│   │   ├── script_sh.py    # Generate test scripts
│   │   └── ...
│   │
│   ├── models/             # Pydantic data models
│   │   ├── dataset.py      # Models for the dataset structure
│   │   ├── problem.py      # Models for problem representation
│   │   └── solution.py     # Models for solution tracking
│   │
│   └── eval/               # Evaluation tools
│       ├── loc.py          # Count logical lines of code
│       ├── log_prob.py     # Calculate log probabilities
│       └── metrics.py      # Track metrics
│
├── library/                # Shared library components (to be developed)
│
├── problems/               # Formatted problems (100 graph problems currently)
│   └── problem_id/
│       ├── PROBLEM.md      # Problem description
│       ├── main.py         # Initial solution
│       ├── run.sh          # Test script
│       ├── tags.txt        # Codeforces tags for the problem
│       └── tests/          # Input/output test cases
│
├── test/                   # Testing utilities
│   └── validate_models.py  # Validate Pydantic models
│
└── .pre-commit-config.yaml # Pre-commit hooks configuration
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/yourusername/codecontests-repo.git
cd codecontests-repo

# Install dependencies
uv pip install -e "."

# Install pre-commit hooks
pre-commit install

# Process problems from the dataset (examples)
# Process all problems (no limit)
uv run -m tools.dataset.process

# Process up to 100 graph problems
uv run -m tools.dataset.process --tag graphs --limit 100

# Each processed problem will include a tags.txt file with Codeforces tags

# Run tests for a specific problem
cd problems/problem_id
./run.sh

# Or run directly from any directory
uv run problems/problem_id/main.py < problems/problem_id/tests/input_1.txt

# Run linting and type checking
uv run -m ruff check .
uv run -m ruff format .
uv run pyright .

# Run model validation tests
uv run python test/validate_models.py
```

## Features

- **Standardized Problem Structure**: Each problem has a consistent format with problem description, solution, and test cases
- **Problem Tags**: Each problem includes original Codeforces tags in tags.txt for better categorization
- **Type-Safe Models**: Pydantic models for dataset problems, test cases, and solutions
- **Code Quality Tools**: Pre-commit hooks for linting, formatting, and type checking
- **Test File Protection**: Prevention of accidental test file modifications
- **Evaluation Metrics**: Tools to measure:
  - Logical Lines of Code (LLOC): Using AST parsing to count logical statements
  - Log Probability: Using TogetherAI's Qwen model to measure code predictability
- **Graph Problem Focus**: 100 graph problems processed from the DeepMind Code Contests dataset

## Current Status

- ✅ Repository setup with structure and configuration
- ✅ Pre-commit hooks for code quality enforcement
- ✅ Pydantic models for dataset and problem representation
- ✅ Evaluation tools implementation
- ✅ Dataset processing for 100 graph problems
- ✅ Created [INSTRUCTIONS.md](INSTRUCTIONS.md) for agents performing the compression task
- 🔄 Library implementation by compression agents (next steps)

For the detailed benchmark plan and implementation roadmap, see [PLAN.md](PLAN.md).

## Additional Documentation

- [INSTRUCTIONS.md](INSTRUCTIONS.md): Detailed instructions for agents performing code compression
- [CLAUDE.md](CLAUDE.md): Guidelines for working with Claude on this repository
- [PLAN.md](PLAN.md): Detailed benchmark plan and implementation roadmap

## License

This project is licensed under the MIT License - see the LICENSE file for details.
