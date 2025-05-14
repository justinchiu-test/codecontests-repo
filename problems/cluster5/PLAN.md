 # Project Plan for Code Compression Benchmark

 ## 1. Library API Design
 We will centralize common input/output patterns into concise helper functions in `library.py`:
   - rl(): read a line from stdin, stripped of trailing newline
   - ri(): read a single integer
   - ril(): read a list of integers
   - rsl(): read a list of strings (split by whitespace)
   - rg(): generator of integers from the next input line

 These helpers cover the vast majority of input parsing across all problems.

 ## 2. Refactoring Strategy
 For each problem directory (`<problem>/main.py`):
   1. Add `from library import rl, ri, ril, rsl, rg` at the top.
   2. Replace all uses of `input()`, `int(input())`, `input().split()`, and list/map comprehensions over `input().split()` with our helpers.
   3. Preserve problem-specific algorithms and imports (e.g., `sys.setrecursionlimit`, `math` functions).
   4. Remove any overridden `input = sys.stdin.readline` statements.
   5. Run `bash <problem>/run.sh` to verify all tests pass.

 ## 3. Progress Checklist
 We will refactor each problem in sequence, marking it off upon successful test pass:
   - [x] 1003_f_abbreviation_11357
   - [x] 1093_f_vasya_and_array_10216
   - [x] 1120_c_compress_string_7093
   - [x] 1129_c_morse_code_3034
   - [ ] 1131_e_string_multiplication_636
   - [ ] 1149_b_three_religions_220
   - [ ] 1183_h_subsequences_hard_version_3870
   - [ ] 1188_c_array_beauty_9595
   - [ ] 118_d_caesars_legions_2724
   - [x] 126_b_password_13138
   - [ ] 1303_e_erase_subsequences_10330
   - [ ] 1337_e_kaavi_and_magic_spell_10539
   - [ ] 1422_e_minlexes_13041
   - [ ] 1499_e_chaotic_merge_7526
   - [x] 14_e_camels_3676
   - [ ] 404_d_minesweeper_1d_2023
   - [ ] 44_h_phone_number_12435
   - [ ] 476_e_dreamoon_and_strings_2026
   - [ ] 477_c_dreamoon_and_strings_12540
   - [ ] 597_c_subsequences_6091
   - [ ] 61_e_enemy_is_weak_2240
   - [ ] 633_c_spy_syndrome_2_3594
   - [ ] 653_b_bear_and_compressing_5990
   - [ ] 666_a_reberland_linguistics_4325
   - [ ] 667_c_reberland_linguistics_6406
   - [ ] 682_d_alyona_and_strings_1931
   - [ ] 774_h_repairing_of_string_9638
   - [ ] 805_d_minimum_number_of_steps_8284
   - [ ] 900_e_maximum_questions_7560
   - [x] 91_a_newspaper_headline_6625

 ## 4. Testing
 After each refactoring, execute the provided `run.sh` script to ensure correctness.  Address any failures by debugging and adjusting either the library or the problem solution.
