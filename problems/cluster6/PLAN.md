# Library Design Plan

This document outlines the design of a shared library for CF cluster6, and the strategy to refactor all problem solutions to use it.

## 1. Common Patterns Across Problems
- **Input parsing**: reading integers, lists, tokens, matrices
- **Math & Combinatorics**: modular arithmetic, modular inverse/power, combinations, factorial, GCD/LCM
- **Probability & DP**: DP transitions using inverses, sliding-window DP, prefix sums
- **Graphs & Trees**: BFS/DFS for distances, all-pairs shortest paths on small trees
- **Data structures**: Fenwick tree (BIT), DSU (rare), deque, Counter
- **Utilities**: prefix sums, sliding windows, bitmask enumeration

## 2. Proposed Library Components
1. **IO Utilities**
   - `input = sys.stdin.readline` (fast line reading)
   - `ri()` → read a single integer
   - `ria()` → read a list of integers from one line
   - `rs()` → read a stripped string
   - `rst()` → read a list of tokens (strings)

2. **Math Utilities**
   - `gcd`, `lcm`
   - `inv(a, mod)` → modular inverse via `pow(a, mod-2, mod)`
   - `comb(n, k, mod=None)` → `math.comb` with optional modulo
   - `fact(n, mod=None)` → `math.factorial` with optional modulo
   - `nCr(n, k, mod=None)` → alias to `comb`

3. **Data Structures**
   - `Fenwick(n)` → point-update, prefix-sum BIT
   - `DSU(n)` → union-find structure
   - `deque`, `Counter`, `defaultdict` imports for convenience

4. **Graph Algorithms**
   - `bfs(start, graph)` → returns distance list from `start`
   - `apsp(graph, n)` → all-pairs shortest paths for small `n` (e.g., trees)

5. **Utilities**
   - `prefix_sums(arr)` → builds prefix sums
   - `sliding_window(arr, k)` → generator or helper for sliding windows

## 3. Refactoring Strategy
For each problem `main.py`:
1. Add `from library import *` at the top.
2. Replace low-level input parsing with `ri()`, `ria()`, `rs()`, `rst()`.
3. Remove inlined math helper code (e.g., manual `inv`, `add`) and replace with `inv`, `comb`, etc.
4. Factor out repeated algorithms (BFS, BIT updates) to library calls.
5. Run `bash {problem}/run.sh` and ensure all tests pass.
6. Update `PLAN.md` checklist when each problem is completed.

## 4. Checklist
- [ ] 108_d_basketball_team_11673
- [ ] 1111_d_destroy_the_colony_7405
- [ ] 1172_c1_nauuo_and_pictures_easy_version_2723
- [ ] 1172_c2_nauuo_and_pictures_hard_version_13029
- [ ] 1187_f_expected_square_beauty_12302
- [ ] 1245_e_hyakugoku_and_ladders_2311
- [ ] 1264_c_beautiful_mirrors_with_queries_6684
- [ ] 1349_d_slime_and_biscuits_751
- [ ] 145_c_lucky_subsequence_8670
- [ ] 1461_c_random_events_9295
- [ ] 1475_e_advertising_agency_1071
- [ ] 148_d_bag_of_mice_3571
- [ ] 1541_d_tree_array_2740
- [ ] 1543_c_need_for_pink_slips_3469
- [ ] 160_c_find_pair_12111
- [ ] 167_b_wizards_and_huge_prize_1597
- [ ] 261_b_maxim_and_restaurant_4932
- [ ] 262_d_maxim_and_restaurant_7013
- [ ] 28_c_bath_queue_2018
- [ ] 442_b_andrey_and_problem_4212
- [ ] 50_d_bombing_7752
- [ ] 518_d_ilya_and_escalator_1612
- [ ] 521_d_shop_3485
- [ ] 540_d_bad_luck_island_6817
- [ ] 54_c_first_digit_law_6609
- [ ] 623_d_birthday_6300
- [ ] 785_d_anton_and_school__2_9951
- [ ] 817_b_makes_and_the_product_1937
- [ ] 908_d_new_year_and_arbitrary_arrangement_7769
- [ ] 9_a_die_roll_1319
