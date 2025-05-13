# Plan for Shared Library and Refactoring

This document outlines the design of our shared `library.py` and the steps to refactor each problem solution to use it.

## Library Functions

- **Input Handling**
  - Override `input()` to use `sys.stdin.readline()` and strip the trailing newline, matching built-in semantics.
  - `ni()`: read and return an integer (`int(input())`).
  - `na()`: read a line of input and return a list of integers (`list(map(int, input().split()))`).
  - `ns()`: read and return a raw string line (`input()`).
- **String Utilities**
  - `zf(s)`: compute and return the Z-function array for string or list `s`.
  - `cnt(s)`: count the maximum run length of each lowercase letter in string `s`, return dict `{char: max_run}`.
  - `nxt(cnt_dict, t)`: merge run counts according to the "string multiplication" problem logic, return updated dict.

## Refactoring Steps per Problem

For each problem directory `{problem}`:
1. Open `main.py`.
2. Remove any custom input overrides (e.g., `input = sys.stdin.readline`).
3. Remove local definitions of utilities now in the library (`zf`, `cnt`, `nxt`, etc.).
4. Add at the top:
   ```python
   from library import input, ni, na, ns, zf, cnt, nxt
   ```
5. Replace input patterns:
   - `n = int(input())` → `n = ni()`
   - `a = list(map(int, input().split()))` → `a = na()`
   - `s = input().strip()` → `s = ns()`
6. Replace calls to local utility functions with the library versions:
   - `zfunc(s)` or `f(s)` → `zf(s)`
   - `cnt(s)` and `nxt(c, t)` use the library definitions.
7. Keep problem-specific constants (e.g., `MOD`, `BAD`, tags) intact.
8. Run and verify tests with:
   ```bash
   bash {problem}/run.sh
   ```
9. If tests fail, debug or adjust the refactoring, ensuring the library remains valid across all problems.

## Quality Checks

- Ensure `library.py` contains only shared, well-tested utilities.
- Remove any unused library functions once all refactorings are complete.
- Run pre-commit checks if the repo uses them.
- Track progress by marking completed problems in this `PLAN.md` (optional).
