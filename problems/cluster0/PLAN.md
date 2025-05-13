# Plan for Shared Library and Refactoring

## Goals
- Identify common patterns across all problem solutions
- Create a concise library of reusable components
- Refactor each `main.py` to use these components and pass existing tests

## Proposed Library Components (in `library.py`)
1. IO Helpers
   - `read_int()`: read a single integer
   - `read_ints()`: read multiple integers from a line
2. Graph/Tree Builders
   - `read_tree(n)`: read `n-1` undirected edges into 1-indexed adjacency list
   - `read_graph(n, m, directed=False, weighted=False)`: read `m` edges (optionally weighted/directed)
3. Traversal Algorithms
   - `bfs(adj, start)`: return distance list from `start` (unweighted graph)
   - `dfs(adj, start, visited=None)`: simple DFS ordering or callback support
4. Disjoint Set Union (DSU)
   - `class DSU`: with `find` and `union`

## Refactoring Checklist
Mark each problem as done when its `main.py` uses library functions and passes tests.
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

## Next Steps
1. Implement the library functions in `library.py` incrementally.
2. Refactor `main.py` in each problem to use library helpers.
3. Run `bash {problem}/run.sh` to ensure all tests pass.
4. Iterate: adjust library or solution until all problems are refactored and pass.
