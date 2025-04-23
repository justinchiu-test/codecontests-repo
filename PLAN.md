# CodeContests Library Refactoring Plan

## Objective
Create a shared library for code_contests problems to minimize the total code required across all solutions.

## Repository Design
1. **Single Repository Approach** (Recommended)
   - Central shared library with all reusable components
   - Solutions organized in a standardized directory structure
   - Benefits:
     - Easier maintenance of shared code
     - Simplified dependency management
     - Better code reuse across problems
     - Simpler testing and CI/CD setup

2. **Standard I/O Handling**
   - Create dedicated I/O utilities for:
     - Parsing various input formats from stdin
     - Formatting output correctly to stdout
     - Supporting common input patterns (integers, arrays, graphs)
     - Optimized reading of large inputs

## Analysis Phase
1. **Dataset Exploration**
   - Download and explore the deepmind/code_contests dataset
   - Analyze solution patterns across different problems
   - Identify common algorithms, data structures, and utilities

2. **Pattern Identification**
   - Group solutions by algorithmic techniques (e.g., graphs, dynamic programming)
   - Extract common helper functions and utility code
   - Identify language-specific optimizations (focusing on Python initially)

## Implementation Phase
1. **Core Library Structure**
   - Create modular components for:
     - Data structures (graphs, trees, priority queues)
     - Algorithm templates (dynamic programming, graph traversal)
     - Input/output handling
     - Math utilities
     - String processing

2. **Problem Representation with Pydantic**
   - Use Pydantic models to represent:
     ```python
     class TestCase(BaseModel):
         input: str
         output: str
         time_limit_ms: Optional[int] = 30000
         memory_limit_mb: Optional[int] = 512

     class Problem(BaseModel):
         id: str
         name: str
         description: str
         category: List[str]
         difficulty: str
         test_cases: List[TestCase]
         source: Optional[str] = None

     class Solution(BaseModel):
         problem_id: str
         code: str
         language: str = "python"
         uses_shared_lib: bool = True
         original_code: Optional[str] = None  # For comparison
         metrics: Optional[Dict[str, Any]] = None

     class ExecutionResult(BaseModel):
         passed: List[bool]
         test_inputs: List[str]
         test_outputs: List[str]
         predicted_outputs: List[str]
         stderrs: List[str]
         execution_times_ms: Optional[List[float]] = None
         memory_usage_mb: Optional[List[float]] = None
     ```
   - Benefits:
     - Type validation and documentation
     - Serialization/deserialization for API and storage
     - Schema evolution with backward compatibility
     - Integration with IDE tools for autocompletion

2. **Directory Structure**
   ```
   codecontests-repo/
   ├── tools/                  # Repository creation tools (Part 1)
   │   ├── dataset/            # Dataset processing utilities
   │   │   ├── download.py     # Download/extract codecontests dataset
   │   │   ├── process.py      # Process and format problems
   │   │   └── validate.py     # Validate processed problems
   │   │
   │   ├── formatter/          # Problem formatting utilities
   │   │   ├── problem_md.py   # Generate PROBLEM.md files
   │   │   ├── solution_py.py  # Extract initial main.py solutions
   │   │   └── script_sh.py    # Generate run.sh test scripts
   │   │
   │   └── models/             # Pydantic data models
   │       ├── problem.py      # Problem, TestCase models
   │       └── solution.py     # Solution, ExecutionResult models
   │
   ├── library/                # Shared library components (Part 2)
   │   ├── io/                 # Input/output utilities
   │   │   ├── parser.py       # Input parsing utilities
   │   │   └── formatter.py    # Output formatting utilities
   │   │
   │   ├── ds/                 # Data structures
   │   │   ├── graph.py        # Graph representations
   │   │   ├── tree.py         # Tree structures
   │   │   └── heap.py         # Priority queue implementations
   │   │
   │   ├── algo/               # Algorithm templates
   │   │   ├── dp.py           # Dynamic programming templates
   │   │   ├── graph.py        # Graph algorithms
   │   │   └── search.py       # Search algorithms
   │   │
   │   └── math/               # Math utilities
   │       ├── number.py       # Number theory functions
   │       └── geometry.py     # Computational geometry
   │
   ├── problems/               # Formatted problems (Part 3)
   │   ├── problem_1/          # Each problem in its own directory
   │   │   ├── PROBLEM.md      # Problem description
   │   │   ├── main.py         # Initial solution
   │   │   ├── run.sh          # Test script
   │   │   └── tests/          # Test cases
   │   │       ├── input_1.txt # Test inputs
   │   │       └── output_1.txt # Expected outputs
   │   │
   │   ├── problem_2/
   │   └── ...
   │
   ├── data/                   # Raw data storage (gitignored)
   │   └── raw/                # Raw data from code_contests
   │
   └── scripts/                # Utility scripts
       ├── setup.sh            # Set up the repository
       ├── test_all.sh         # Run all tests
       └── analyze.py          # Analyze code reduction
   ```

3. **Code Execution Integration**
   - Leverage the existing code-execution server (github.com/justinchiu/code-execution)
   - Integration benefits:
     - Standardized execution environment for all problems
     - Consistent measurement of runtime performance
     - Ability to test against problem test cases
     - Support for input/output validation

4. **Refactoring Process**
   - Select representative problems from each category
   - Refactor solutions to use the shared library
   - Measure code reduction and performance impact
   - Iterate on the library design based on findings

5. **Testing Framework**
   - Ensure refactored solutions pass all original test cases
   - Create regression tests for library components
   - Implement utility to run solutions against problem test cases
   - Compare performance before and after refactoring
   - Use code-execution server for consistent evaluation

6. **Problem Testing Workflow**
   - **Test Case Format**:
     - Store test cases for each problem in standardized JSON format
     - Each test case contains input data and expected output
     - Include time and memory limits for each problem

   - **Testing Process**:
     1. **Execution Engine**:
        - Leverage the provided execution code which:
          ```python
          # Main execution function that:
          # 1. Writes the program to a temporary file
          # 2. Runs the program for each test input using subprocess
          # 3. Captures stdout and stderr
          # 4. Compares outputs with expected results
          # 5. Handles timeouts (30 seconds per test)
          # 6. Returns detailed execution results
          ```
        - Add parallelization for performance with `concurrent.futures`
        - Implement additional metrics collection (memory usage, execution time)

     2. **Local Testing**:
        - Create a test runner script that:
          - Loads test cases for a specific problem
          - Uses the execution engine to run solutions
          - Reports pass/fail status and execution metrics
          - Support batch testing across multiple problems
        - Helper methods to test a single solution or all solutions

     3. **Code Execution Server Integration**:
        - Configure API client to connect to code-execution server
        - Submit solution code with test cases
        - Receive execution results (pass/fail, runtime metrics)
        - Log results for performance comparison
        - Fallback to local execution when server unavailable

   - **Continuous Integration**:
     - Automated testing of all solutions with GitHub Actions
     - Regression testing of shared library components
     - Performance benchmarking to detect optimization impacts
     - Track code reduction metrics over time

## Evaluation
1. **Metrics**
   - Total lines of code (original vs. refactored)
   - Code reuse percentage
   - Execution time comparison
   - Maintainability score

2. **Documentation**
   - Library API documentation
   - Usage examples for each component
   - Patterns and best practices

## Roadmap
1. Set up project structure and development environment
2. Download the code_contests dataset
3. Format all problems into standardized structure in problems/ directory
   - Parse problem descriptions into PROBLEM.md
   - Extract initial Python solutions into main.py
   - Generate test cases from dataset
   - Create run.sh scripts for each problem
   - Ensure all test cases can be run with uv
4. Analyze common patterns across all problems
5. Implement shared components in the library directory
   - Input/output utilities for handling stdin/stdout
   - Common data structures and algorithms
   - Math utilities
6. Refactor solutions to use the shared library
   - Start with representative problems from each category
   - Measure code reduction and performance
7. Iterate on library design based on findings
8. Finalize library and comprehensive documentation
