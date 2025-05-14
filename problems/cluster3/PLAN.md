# PLAN

## 1. Library Components

We will create a minimal shared library in `library.py` containing:

### IO Utilities
- `ni()`: read next integer from stdin tokens
- `ns()`: read next string token
- `read_int()`: alias for `ni()`
- `read_ints()`: read a list of integers from the current line or token stream

### Graph and Tree Builders
- `read_tree(n, directed=False) -> List[List[int]]`
- `read_weighted_tree(n, directed=False) -> List[List[Tuple[int, int]]]`
- `read_graph(n, m, directed=False) -> List[List[int]]`
- `read_weighted_graph(n, m, directed=False) -> List[List[Tuple[int, int]]]`

### Utilities
- `setrecursionlimit(n)`: set Python recursionlimit

Additional functions may be added if recurring patterns emerge.

## 2. Refactoring Strategy

For each problem in `{problem}/main.py`:
1. Remove custom I/O boilerplate
2. `from library import ni, ns, read_int, read_ints, read_tree, read_graph, setrecursionlimit`
3. Replace raw `input()` and `map(int, ...)` with `ni()`, `read_ints()`, etc.
4. Use `read_tree` or `read_graph` to build adjacency lists when appropriate.
5. Insert `setrecursionlimit(...)` if deep recursion is used.
6. Run `bash {problem}/run.sh` to verify tests pass.

## 3. Refactoring Checklist

- [ ] 1056_d_decorate_apple_tree_1782
- [ ] 1076_e_vasya_and_a_tree_11985
- [ ] 1083_a_the_fair_nut_and_the_best_path_12817
- [ ] 1084_d_the_fair_nut_and_the_best_path_3448
- [ ] 1092_f_tree_with_maximum_cost_8028
- [ ] 1153_d_serval_and_rooted_tree_2202
- [ ] 1187_e_tree_painting_12718
- [ ] 1280_c_jeremy_bearimy_11057
- [ ] 1281_e_jeremy_bearimy_9704
- [ ] 1324_f_maximum_white_subtree_3668
- [ ] 1332_f_independent_set_12309
- [ ] 1336_a_linova_and_kingdom_8768
- [ ] 1436_d_bandit_in_a_city_4611
- [ ] 1453_e_dog_snacks_5757
- [ ] 1498_f_christmas_game_5028
- [ ] 1499_f_diameter_cuts_11692
- [ ] 1528_a_parsas_humongous_tree_10236
- [ ] 1540_b_tree_array_3053
- [ ] 23_e_tree_4723
- [ ] 274_b_zero_tree_3163
- [ ] 275_d_zero_tree_12948
- [ ] 461_b_appleman_and_tree_11604
- [ ] 538_e_demiurges_play_again_12023
- [ ] 543_d_road_improvement_5673
- [ ] 696_b_puzzles_9008
- [ ] 697_d_puzzles_7551
- [ ] 700_b_connecting_universities_5263
- [ ] 735_e_ostap_and_tree_2037
- [ ] 80_e_beavermuncher0xff_11410
- [ ] 846_e_chemistry_in_berland_60
