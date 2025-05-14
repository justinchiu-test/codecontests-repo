# Code Compression Library Plan

## Objective
Design a compact, reusable Python library (`library.py`) for common patterns across all problem solutions.
Refactor every `main.py` to import and use library components, reducing duplicate code.

## Library Components
1. **Input Parsing**
   - `readint()` : read next token as `int`
   - `readints(n=None)` : read `n` tokens as `List[int]`, or all remaining if `n` is `None`
   - `readstr()` : read next token as `str`
   - `readstrs(n=None)` : read `n` tokens as `List[str]`, or all remaining if `n` is `None`
2. **Disjoint Set Union (DSU)**
   - `class DSU` with `find(x)`, `union(a,b)`, `size(x)` methods
3. **Graph Utilities**
   - `read_graph(n, m, zero_index=True, directed=False)` -> adjacency list
   - `read_weighted_edges(m, zero_index=True)` -> list of `(u,v,w)`
4. **Traversal**
   - `dfs_iter(start, graph)` -> iterable or set of visited nodes
   - `bfs_dist(start, graph)` -> `List[int]` distances
5. **Common Algorithms** (as needed)
   - `tree_diameter(graph)` -> diameter length (two-phase BFS)
   - `complement_components(n, edges)` -> number of components in complement graph

## Refactoring Strategy
1. **Implement** above components in `library.py`, keeping code minimal and tested.
2. **Checklist**: Refactor each problem in the order below.
   - DSU problems (17):
     - `920_e_connected_components_167`
     - `1242_b_01_mst_10223`
     - `1243_d_01_mst_12097`
     - `1263_d_secret_passwords_6164`
     - `1521_d_nastia_plays_with_a_tree_11693`
     - `217_a_ice_skating_2223`
     - `103_b_cthulhu_4280`
     - `653_e_bear_and_forgotten_tree_2_10362`
     - `445_b_dzy_loves_chemistry_1921`
     - `1277_e_two_fairs_122`
     - `505_b_mr_kitayutas_colorful_graph_984`
     - `104_c_cthulhu_10214`
     - `771_a_bear_and_friendship_condition_2351`
     - `9_e_interesting_graph_and_apples_483`
     - `1249_b1_books_exchange_easy_version_7099`
     - `659_e_new_reform_13276`
     - `977_e_cyclic_components_8291`
     - `791_b_bear_and_friendship_condition_8388`
   - DFS problems (14):
     - `103_b_cthulhu_4280`
     - `104_c_cthulhu_10214`
     - `1263_d_secret_passwords_6164`
     - `1521_d_nastia_plays_with_a_tree_11693`
     - `653_e_bear_and_forgotten_tree_2_10362`
     - `510_b_fox_and_two_dots_2444`
     - `505_b_mr_kitayutas_colorful_graph_984`
     - `690_c1_brain_network_easy_6407`
     - `1217_d_coloring_edges_7410`
     - `216_b_forming_teams_6387`
     - `9_e_interesting_graph_and_apples_483`
     - `659_e_new_reform_13276`
     - `156_d_clues_3678`
     - `791_b_bear_and_friendship_condition_8388`
   - BFS / Tree problems:
     - `1277_e_two_fairs_122`
     - `745_c_hongcow_builds_a_nation_7762`
     - `1000_e_we_need_more_bosses_8440`
     - `977_e_cyclic_components_8291`
   - Other patterns as encountered.
3. **For each** problem:
   - Remove inline utility definitions (e.g., custom DSU, FastIO)
   - `import` necessary functions/classes from `library`
   - Replace raw `input()` parsing with `readint`/`readints`/`read_graph`
   - Adjust logic to library abstractions
   - Run `bash {problem}/run.sh` to verify

## Testing
After each refactor, run `bash {problem}/run.sh`. Maintain passing status before moving on.

---
*(Update this plan as library evolves and checklist progresses.)*
