 # PLAN.md

 ## Summary
 This document outlines the design of a shared library (`library.py`) to consolidate common patterns across all problem solutions.

 ## Goals
 1. Minimize duplicated code across all `main.py` files.
 2. Provide clean, reusable abstractions for common tasks:
    - Input parsing
    - Graph construction and traversal
    - Disjoint-set (Union-Find)
    - Common algorithms (DFS, BFS, Dijkstra)

 ## Proposed Library Structure

 1. **Input Utilities**
    - `next_int()`: read next integer from stdin
    - `next_str()`: read next token as string
    - `next_ints(n)`: read next `n` integers

 2. **Graph Utilities**
    - `read_graph(n, m, directed=False, weighted=False, one_indexed=True)`: build adjacency list
    - `dfs(graph, start)`: iterative DFS returning visit order
    - `bfs(graph, start)`: iterative BFS returning visit order
    - `dijkstra(graph, source)`: return `(dist, prev)` arrays for weighted graphs

 3. **Disjoint Set Union (DSU)**
    - `class DSU`: `find`, `union` with path compression and union by rank

 4. **Optional Utilities** (add later if needed)
    - Priority queue wrappers
    - Fenwick tree / Segment tree
    - Combinatorics (nCr, factorial modulo)

 ## Refactoring Plan
 1. Implement input and graph utilities in `library.py`.
 2. For each problem directory:
    - Import needed utilities from `library.py`.
    - Replace custom input-reading boilerplate with library functions.
    - Replace manual graph building/traversal with library calls where applicable.
    - Ensure solution logic remains the same but more concise.
    - Run `bash {problem}/run.sh` and verify all tests pass.
 3. Iterate: extend `library.py` with new utilities as common patterns emerge.
 4. Remove any unused functions and finalize.

 ## Checklist of Refactored Problems
 (Mark off once refactored and tested)
 - [ ] 1041_e_tree_reconstruction_8858
 - [ ] 1076_d_edge_deletion_9486
 - [ ] 1086_b_minimum_diameter_tree_8860
 - [ ] 110_e_lucky_tree_11049
 - [ ] 1118_f1_tree_cutting_easy_version_12195
 - [ ] 1133_f1_spanning_tree_with_maximum_degree_10945
 - [ ] 1143_c_queen_2410
 - [ ] 116_c_party_7303
 - [ ] 1176_e_cover_it_10635
 - [ ] 1286_b_numbers_on_tree_11475
 - [ ] 1287_d_numbers_on_tree_1897
 - [ ] 1325_c_ehab_and_pathetic_mexs_1064
 - [ ] 1338_b_edge_weight_assignment_7623
 - [ ] 1391_e_pairs_of_pairs_6690
 - [ ] 246_d_colorful_graph_3682
 - [ ] 292_b_network_topology_9930
 - [ ] 319_b_psychos_in_a_line_454
 - [ ] 404_c_restore_graph_3793
 - [ ] 420_c_bug_in_code_5355
 - [ ] 421_d_bug_in_code_563
 - [ ] 580_c_kefa_and_park_5570
 - [ ] 747_e_comments_9533
 - [ ] 796_c_bank_hacking_5163
 - [ ] 839_c_journey_2458
 - [ ] 902_b_coloring_a_tree_2877
 - [ ] 913_b_christmas_spruce_7977
 - [ ] 931_d_peculiar_appletree_4441
 - [ ] 963_b_destruction_of_a_tree_65
 - [ ] 981_c_useful_decomposition_4026
 - [ ] 982_c_cut_em_all_5275
