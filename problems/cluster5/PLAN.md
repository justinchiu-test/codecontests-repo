 # PLAN for CodeContests Library Refactoring

 This plan outlines steps to centralize I/O functionality into a shared `library.py`, refactor solutions to use it, and ensure all tests continue to pass.

 1. Library Design
    - Provide fast, consistent input override: `input` uses `sys.stdin.readline` with newline stripping.
    - Convenience functions:
      * `read_int()` → single integer
      * `read_ints()` → iterator of ints from a line
      * `read_list()` → list of ints from a line
      * `read_str()` → stripped string line
      * `read_strs()` → list of strings from a line
    - Set a higher recursion limit (`sys.setrecursionlimit(10**7)`).

 2. Refactoring Solutions
    - Add `from library import *` after the shebang in each `main.py`.
    - Remove any custom I/O hacks (none present in current solutions).
    - Optionally replace direct parsing (e.g., `int(input())`, `list(map(int, input().split()))`) with convenience functions for more compact code.

 3. Verification
    - Run each problem’s `run.sh` to execute its test suite.
    - If any test fails, examine mismatches and update the library or solution accordingly.

 Goals:
    - Eliminate duplicated I/O boilerplate.
    - Keep solution code compact and focused on algorithms.
    - Maintain full compatibility with existing tests.
