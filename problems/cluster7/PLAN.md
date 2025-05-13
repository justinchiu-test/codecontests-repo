# PLAN for Code Compression

## Library Design (`library.py`)
1. I/O Overrides and Readers
   - Override built-in `input` with `sys.stdin.readline` for fast reading.
   - `read_int()` → read and return a single integer.
   - `read_ints()` → read and return a list of integers.
   - `read_strs()` → read and return a list of strings.
   - `read_matrix(n, m, *, type=int)` → read an `n x m` matrix of `type`.

2. Numeric Utilities
   - `xor_list(it)` → XOR-reduce an iterable of ints.
   - `prefix_xor(lst)` → return list of prefix XORs of `lst`.
   - `prefix_sum(lst)` → return list of prefix sums of `lst`.
   - `popcount(x)` → return the number of set bits (`int.bit_count`).

3. Printing Helpers
   - `print_list(lst, sep=' ')` → `print(*lst, sep=sep)` for compact output.

4. Fast I/O Setup
   - `setup_fast_io()` → optional call to use `sys.stdin.buffer` and `sys.stdout` wrappers

## Refactor Checklist
Will refactor each problem under its directory. For each:
  - [ ] Override I/O and use `read_*` in place of raw `input` or `map(int, ...)`.
  - [ ] Replace manual XOR loops with `xor_list` or `prefix_xor`.
  - [ ] Use `print_list` for space-separated outputs.
  - [ ] Remove now-unused imports or helper lambdas.
  - [ ] Run `bash {problem}/run.sh` to ensure all tests pass.

Problems to refactor:
```
1016_d_vasya_and_the_matrix_3445
1031_e_triple_flips_11983
1054_d_changing_array_9485
1071_c_triple_flips_5739
1113_c_sasha_and_a_bit_of_relax_8341
1151_b_dima_and_a_bad_xor_6990
1163_e_magical_permutation_2099
1174_d_ehab_and_the_expected_xor_problem_10531
1323_d_present_959
1325_d_ehab_the_xorcist_11372
1362_b_johnny_and_his_hobbies_8248
1394_b_boboniu_walks_on_graph_6794
1416_c_xor_inverse_4402
1427_e_xum_2840
1438_d_powerful_ksenia_5652
1516_b_agaga_xooorrr_3468
1534_e_lost_array_11486
1547_d_cogrowing_sequence_6488
15_c_industrial_nim_12943
289_e_polo_the_penguin_and_xor_operation_6598
388_d_fox_and_perfect_sets_5562
424_c_magic_formulas_9623
460_d_little_victor_and_set_2650
627_a_xor_equation_4011
634_b_xor_equation_3074
817_e_choosing_the_commander_4644
862_c_mahmoud_and_ehab_and_the_xor_2355
895_c_square_subsets_12662
923_c_perfect_security_7561
925_c_big_secret_3711
```
