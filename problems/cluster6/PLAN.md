 # Plan for Shared Library (cluster6)

 ## 1. Library Components

 1. **I/O Utilities**
    - `read_int()`: Read a single integer from stdin
    - `read_ints()`: Read a list of integers
    - `read_str()`: Read a stripped string
    - `read_strs()`: Read a list of strings
    - `read_matrix(n, m, typ=int)`: Read an n×m matrix of values of type `typ`

 2. **Math Utilities**
    - `gcd(a, b)`, `lcm(a, b)`
    - `frac(a, b)`: Return simplified `(num, den)` tuple
    - `frac_str(a, b)`: Return simplified fraction as string

 3. **Combinatorics**
    - `fact(n)`, `comb(n, k)`

 4. **Modulo Arithmetic**
    - `modinv(a, m)`: Modular inverse via Fermat's little theorem
    - (Optional) `nCr_mod(n, k, m)` if needed

 5. **Graph Algorithms**
    - `bfs(adj, start)`, `dfs(adj, start)`
    - `dijkstra(adj, start)`
    - `UnionFind` (Disjoint Set Union)

 6. **Data Structures**
    - `Fenwick` (Binary Indexed Tree)
    - `prefix_sum(a)`: Prefix-sum array builder

 7. **Utilities**
    - `bisect_left`, `bisect_right` (aliases to `bisect` module)

 ## 2. Refactoring Checklist

 We will refactor each problem solution to import and use library functions. Status marked as [ ] pending.

- [x] 9_a_die_roll_1319
 - [ ] 28_c_bath_queue_2018
 - [ ] 50_d_bombing_7752
 - [ ] 54_c_first_digit_law_6609
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
 - [ ] 442_b_andrey_and_problem_4212
 - [ ] 518_d_ilya_and_escalator_1612
 - [ ] 521_d_shop_3485
 - [ ] 540_d_bad_luck_island_6817
 - [ ] 623_d_birthday_6300
 - [ ] 785_d_anton_and_school__2_9951
 - [ ] 817_b_makes_and_the_product_1937
 - [ ] 908_d_new_year_and_arbitrary_arrangement_7769

 ## 3. Refactoring Strategy

 1. Implement and validate core I/O and math utilities.
 2. Refactor simple problems (pure I/O or basic math) to use the library.
 3. Introduce combinatorics and modular arithmetic helpers; refactor medium problems.
 4. Add graph algorithms and data structures; refactor graph/tree problems.
 5. Continuously test each refactored solution to ensure all tests pass.
 6. Remove or merge unused functions in the library for final cleanup.
