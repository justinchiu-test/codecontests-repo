# Plan for Shared Library and Refactoring

## Objectives
1. Identify common patterns across solutions and extract into `library.py`.
2. Minimize per-solution code by providing reusable I/O and data-structure utilities.
3. Refactor every `main.py` to use `library.py` without changing problem logic.
4. Ensure all tests continue to pass.

## Proposed Library API (`library.py`)

### I/O Utilities
- `input` alias for `sys.stdin.readline`.
- `ii() -> int`: read and return a single integer.
- `li() -> List[int]`: read a line of space-separated integers and return as list.
- `mi() -> Iterator[int]`: read a line of space-separated integers, return as map(int, …).

### Disjoint Set Union (DSU)
Class `DSU(n)` with methods:
- `find(x) -> int`: find representative of `x`.
- `union(a, b)`: merge sets containing `a` and `b`.
- `size(x) -> int`: return size of the set containing `x`.

### Graph Connectivity
- `connected_components(adj: List[List[int]]) -> List[int]`: return list of component sizes using BFS.

## Refactoring Steps
1. **Implement `library.py`** with the above API.
2. For each problem directory:
   - Replace custom I/O setup (`sys.stdin.readline`, wrappers) with:
     ```python
     from library import input, ii, li, mi
     ```
   - Remove duplicate DSU, BFS helpers if equivalent functions exist in `library.py`, and import them.
   - Adjust indexing to 0-based if needed, or retain 1-based but consistently use library I/O.
   - Import and use `DSU` and `connected_components` where applicable.
3. Run `bash {problem}/run.sh` to verify no regressions.
4. Iterate: extend `library.py` if refactoring many solutions reveal other shared logic.

## Checklist of Problems to Refactor
- [ ] 1000_e_we_need_more_bosses_8440
- [ ] 103_b_cthulhu_4280
- [ ] 104_c_cthulhu_10214
- [ ] 1169_b_pairs_11885
- [ ] 1217_d_coloring_edges_7410
- [ ] 1242_b_01_mst_10223
- [ ] 1243_d_01_mst_12097
- [ ] 1249_b1_books_exchange_easy_version_7099
- [ ] 1263_d_secret_passwords_6164
- [ ] 1277_e_two_fairs_122
- [ ] 1521_d_nastia_plays_with_a_tree_11693
- [ ] 1534_f1_falling_sand_easy_version_9507
- [ ] 156_d_clues_3678
- [ ] 216_b_forming_teams_6387
- [ ] 217_a_ice_skating_2223
- [ ] 27_b_tournament_1914
- [ ] 445_b_dzy_loves_chemistry_1921
- [ ] 45_h_road_problem_460
- [ ] 505_b_mr_kitayutas_colorful_graph_984
- [ ] 505_d_mr_kitayutas_technology_879
- [ ] 510_b_fox_and_two_dots_2444
- [ ] 653_e_bear_and_forgotten_tree_2_10362
- [ ] 659_e_new_reform_13276
- [ ] 690_c1_brain_network_easy_6407
- [ ] 745_c_hongcow_builds_a_nation_7762
- [ ] 771_a_bear_and_friendship_condition_2351
- [ ] 791_b_bear_and_friendship_condition_8388
- [ ] 920_e_connected_components_167
- [ ] 977_e_cyclic_components_8291
- [ ] 9_e_interesting_graph_and_apples_483
