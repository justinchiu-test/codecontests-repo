# PLAN for CodeContests Library Refactoring

This plan outlines the steps to centralize I/O functionality into a shared `library.py`, refactor solutions to use it, and ensure all tests continue to pass.

1. Library Design
   - Provide a fast, consistent input override (`input = sys.stdin.readline`).
   - Include helper functions for common patterns:
     * `read_int()` → single integer
     * `read_ints()` → iterator over integers in a line
     * `read_list()` → list of integers in a line
     * `read_str()` → stripped string line
     * `read_strs()` → list of strings in a line
   - Set a higher recursion limit (`sys.setrecursionlimit(10**7)`).

2. Refactoring Solutions
   - Identify files with custom input hacks (`sys.stdin.readline`, `io.BytesIO` hacks, reader generators).
   - Remove those hacks and top‐level `import sys`/`import io, os` lines.
   - Add `from library import *` at the top of each affected `main.py`.
   - Preserve all existing algorithm logic and other imports (e.g., `collections`, `heapq`, etc.).

3. Verification
   - Use each problem’s `run.sh` to execute all test cases after refactoring.
   - If any test fails, examine mismatches and update the library or solution accordingly.

4. Goals
   - Eliminate duplicated I/O boilerplate.
   - Keep solution code as compact and focused on algorithms.
   - Maintain full compatibility with existing test suites.
