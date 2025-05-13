# PLAN for Shared Library Refactoring

## Overview
We aim to minimize total code size across all tree and graph-related problems by:
- Identifying and extracting common patterns
- Implementing a compact, reusable library (`library.py`)
- Refactoring each `main.py` to use the library

## Proposed Library Components
1. **Fast I/O**
   - `read_int()`, `read_ints()`, `read_str()`, `read_strs()`
2. **Graph Utilities**
   - `graph(n, edges, directed=False)` → adjacency list
3. **Tree Utilities**
   - DFS traversal: compute `parent`, `depth`, `subtree_size`, Euler tour (`tin`, `tout`)
   - `tree(n, edges, root=0)` → returns `(adj, parent, depth, order)`
4. **LCA (Binary Lifting)**
   - `LCA(parent, root)` class with `.lca(u, v)` and `.dist(u, v)`
5. **Fenwick Tree (BIT)**
   - `Fenwick(n)` with `.add(i, v)`, `.sum(r)`, `.range_sum(l, r)`
6. **DSU (Union-Find)**
   - `DSU(n)` with `.find(x)`, `.union(a, b)`
7. **Combinatorics & Mod Arithmetic**
   - `fact`, `inv_fact`, `nCr(n, r, mod)` utilities
   - `pow_mod(x, y, mod)`

Components will be trimmed or extended based on actual usage.

## Refactor Checklist
Mark each problem as completed when its `main.py` is refactored and tests pass.

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
- [ ] 1498_f_christmas_game_5029
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
