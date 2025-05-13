 # PLAN for cluster7 library

 This document outlines the design and refactoring plan for the shared library (`library.py`) in cluster7, focusing on bitmask-related problems.

 ## Library components

 1. I/O helpers
    - Override `input` to `sys.stdin.readline` for fast reading
    - `read_int()` -> `int`
    - `read_ints()` -> `List[int]`
    - `read_str()` -> `str`
    - `read_strs()` -> `List[str]`

 2. Bit utilities
    - `xor_list(a: List[int]) -> int`: XOR of a list of integers
    - `xor_upto(n: int) -> int`: XOR of all integers from 1 to n
    - `prefix_xor(a: List[int]) -> List[int]`: prefix XOR array, with initial 0
    - `bits_to_int(bits: List[int]) -> int`: interpret list `bits` (LSB first) as integer
    - `bit_positions(n: int) -> List[int]`: 1-based positions of set bits in `n`

 3. Problem-specific solvers
    - `solve_triple_flips(a: List[int]) -> List[List[int]]`: CF 1031E / 1071C solver for small arrays
    - `count_xor_solutions(s: int, x: int) -> int`: CF 627A / 634B count of (u, v) pairs satisfying u+v=s, u^v=x

 ## Refactoring steps

 For each `problem/main.py`:
 1. Remove custom I/O boilerplate and add `from library import *`
 2. Replace inline XOR/list/sum logic with `xor_list`, `xor_upto`, `prefix_xor`, etc.
 3. Replace duplicated solvers (triple flips, XOR equation) with library calls.
 4. Verify all tests still pass via `bash {problem}/run.sh`.

 Focus on maximizing code reuse across the cluster while ensuring correctness.
