# Library Refactoring Plan

## Objectives
- Identify common patterns across problem solutions
- Create shared library (`library.py`) with reusable components
- Refactor each `main.py` to use library functions, minimizing code duplication

## Identified Common Patterns
1. **Input Parsing**: functions to read integers and lists of integers (`getint`, `getints`).
2. **Math Utilities**: `gcd`, `lcm`, basic math operations.
3. **Geometry**: 2D vector operations (`Vector` class with `dot`, `cross`, `norm_square`, operator overloads).
4. **Disjoint Set Union (DSU)**: union-find structure for connectivity (potentially used).
5. **Graph/BFS/DFS**: basic traversal templates.
6. **Priority Queue**: wrapper over `heapq`.

## Library Components (`library.py`)
- `getint() -> int`
- `getints() -> iterator[int]`
- `gcd`, `lcm`
- `Vector` class for 2D geometry
- `DSU` class with `find`, `union`
- `bfs`, `dfs` helper functions
- `PriorityQueue` wrapper

## Refactoring Steps
1. Implement `library.py` with above components.
2. For each problem directory:
   - Replace ad-hoc input parsing with `getint`/`getints`.
   - Import `Vector` for geometric problems (remove local class definitions).
   - Import other utilities (`gcd`, `lcm`, `DSU`, etc.) as needed.
   - Remove duplicate helper code moved to library.
3. Run `bash {problem}/run.sh` to verify all tests pass.

## Progress Tracking
- [ ] 1046_i_say_hello_9380
- [ ] 1163_c1_power_transmission_easy_edition_2411
- [ ] 1163_c2_power_transmission_hard_edition_12093
- [ ] 1271_c_shawarma_tent_643
- [ ] 135_b_rectangle_and_square_9812
- [ ] ... (complete for all problems)

_Plan will be updated with components as library evolves._
