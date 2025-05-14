# PLAN for Shared Library (cluster7)

## 1. Objectives
- Abstract common code patterns across all problems to minimize duplication
- Provide concise, reusable utilities for I/O, math, bitwise operations, data structures, and graph algorithms
- Refactor each `main.py` to leverage the shared library and verify correctness via existing tests

## 2. Library Components
1. I/O Utilities
   - `ri() -> int`: read a single integer
   - `rints() -> List[int]`: read a line of space-separated integers
   - `rmap() -> Iterator[int]`: iterator of ints from input line
   - `rs() -> str`: read a raw input line (stripped)
2. Math Utilities
   - `gcd(a, b) -> int`, `lcm(a, b) -> int`
   - `C2(n) -> int`: compute n choose 2 (`n*(n-1)//2`)
   - `modpow(a, b, mod)`, `modinv(a, mod)` (for modular arithmetic)
3. Bitwise Utilities
   - `xor_sum(iterable) -> int`: compute XOR of all elements
   - `prefix_xor(arr) -> List[int]`: prefix XOR array with initial 0
4. Data Structures (as needed)
   - `FenwickTree(size)`: point-update and prefix-sum
   - `DSU(n)`: union-find structure
5. Graph Utilities
   - `build_adj_list(n, edges, directed=False) -> List[List[int]]`
   - `bfs(start, adj)`, `dfs(start, adj)` (if multiple problems need traversal)

> Only include components used by more than one problem. Remove unused utilities once refactoring is complete.

## 3. Refactoring Workflow
1. Implement basic I/O utilities in `library.py`.
2. Scan each problem directory and identify which library functions apply:
   - Replace manual input parsing with `ri()`, `rints()`, `rmap()`, `rs()`.
   - Replace repeated XOR loops with `xor_sum()` or `prefix_xor()`.
   - Replace manual `n*(n-1)//2` patterns with `C2(n)` if helpful.
3. Update `main.py`:
   - Add `from library import <needed functions>` at the top.
   - Remove duplicated helper code.
4. Run `bash {problem}/run.sh` to verify all tests pass.
5. Iterate: as we refactor, if new common patterns emerge, update `library.py` and refactor earlier solutions.

## 4. Checklist of Problems
<!-- Mark as refactored (✔) when each `main.py` is updated and tests pass -->
- [ ] 1016_d_vasya_and_the_matrix_3445
- [ ] 1031_e_triple_flips_11983
- [ ] 1054_d_changing_array_9485
- [ ] 1071_c_triple_flips_5739
- [ ] 1113_c_sasha_and_a_bit_of_relax_8341
- [ ] 1151_b_dima_and_a_bad_xor_6990
- [ ] 1163_e_magical_permutation_2099
- [ ] 1174_d_ehab_and_the_expected_xor_problem_10531
- [ ] 1323_d_present_959
- [ ] 1325_d_ehab_the_xorcist_11372
- [ ] 1362_b_johnny_and_his_hobbies_8248
- [ ] 1394_b_boboniu_walks_on_graph_6794
- [ ] 1416_c_xor_inverse_4402
- [ ] 1427_e_xum_2840
- [ ] 1438_d_powerful_ksenia_5652
- [ ] 1516_b_agaga_xooorrr_3468
- [ ] 1534_e_lost_array_11486
- [ ] 1547_d_cogrowing_sequence_6488
- [ ] 15_c_industrial_nim_12943
- [ ] 289_e_polo_the_penguin_and_xor_operation_6598
- [ ] 388_d_fox_and_perfect_sets_5562
- [ ] 424_c_magic_formulas_9623
- [ ] 460_d_little_victor_and_set_2650
- [ ] 627_a_xor_equation_4011
- [ ] 634_b_xor_equation_3074
- [ ] 817_e_choosing_the_commander_4644
- [ ] 862_c_mahmoud_and_ehab_and_the_xor_2355
- [ ] 895_c_square_subsets_12662
- [ ] 923_c_perfect_security_7561
- [ ] 925_c_big_secret_3711
