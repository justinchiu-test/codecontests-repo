# Library Design Plan for Cluster 7

After analyzing the problems in this cluster, the dominant theme is operations related to **bitwise operations**, particularly XOR (^). The library should provide utility functions for common bit manipulation operations, XOR-related algorithms, and I/O helpers.

## Core Components

### 1. Input/Output Utilities
- Fast I/O reading for common competitive programming input patterns
- Formatted output for common output patterns

### 2. Bitwise Utilities
- XOR prefix sums
- XOR of ranges (cumulative XOR)
- XOR of sequences
- Common XOR properties (finding pairs with certain XOR, etc.)
- Bit manipulation (getting/setting individual bits, bit counting)
- Trie-based operations for XOR optimization

### 3. Common Algorithms
- Binary search
- Fast modular arithmetic
- Common number theory functions for bit operations

## Implementation Plan

### I/O Module
- `read_int()`: Read a single integer
- `read_ints()`: Read multiple integers on a line
- `read_array()`: Read an array of integers
- `read_matrix(rows, cols)`: Read a 2D matrix of integers
- `read_test_cases(reader_func)`: Process multiple test cases

### Bit Operations Module
- `xor_range(n)`: Calculate XOR of all numbers from 0 to n
- `xor_prefix_array(arr)`: Calculate prefix XOR array
- `xor_sum(arr)`: XOR sum of all elements in array
- `find_xor_pairs(arr, target_xor)`: Find pairs with a target XOR value
- `find_nonzero_xor_combination(matrix)`: Find a combination with non-zero XOR 
- `count_bits(n)`: Count set bits in an integer
- `get_bit(n, i)`: Get the ith bit of n
- `set_bit(n, i)`: Set the ith bit of n
- `clear_bit(n, i)`: Clear the ith bit of n
- `toggle_bit(n, i)`: Toggle the ith bit of n

### Trie Implementation for XOR Operations
- `XORTrie`: A trie data structure optimized for XOR operations
  - `add(x)`: Add a number to the trie
  - `find_max_xor(x)`: Find the maximum XOR possible with x
  - `find_min_xor(x)`: Find the minimum XOR possible with x

## Refactoring Checklist

- [ ] 1016_d_vasya_and_the_matrix_3445
- [ ] 1031_e_triple_flips_11983
- [ ] 1054_d_changing_array_9485
- [x] 1071_c_triple_flips_5739
- [x] 1113_c_sasha_and_a_bit_of_relax_8341
- [x] 1151_b_dima_and_a_bad_xor_6990
- [ ] 1163_e_magical_permutation_2099
- [x] 1174_d_ehab_and_the_expected_xor_problem_10531
- [ ] 1323_d_present_959
- [x] 1325_d_ehab_the_xorcist_11372
- [x] 1362_b_johnny_and_his_hobbies_8248
- [ ] 1394_b_boboniu_walks_on_graph_6794
- [ ] 1416_c_xor_inverse_4402
- [ ] 1427_e_xum_2840
- [ ] 1438_d_powerful_ksenia_5652
- [x] 1516_b_agaga_xooorrr_3468
- [ ] 1534_e_lost_array_11486
- [x] 1547_d_cogrowing_sequence_6488
- [x] 15_c_industrial_nim_12943
- [x] 289_e_polo_the_penguin_and_xor_operation_6598
- [ ] 388_d_fox_and_perfect_sets_5562
- [x] 424_c_magic_formulas_9623
- [ ] 460_d_little_victor_and_set_2650
- [x] 627_a_xor_equation_4011
- [x] 634_b_xor_equation_3074
- [ ] 817_e_choosing_the_commander_4644
- [x] 862_c_mahmoud_and_ehab_and_the_xor_2355
- [ ] 895_c_square_subsets_12662
- [x] 923_c_perfect_security_7561
- [ ] 925_c_big_secret_3711