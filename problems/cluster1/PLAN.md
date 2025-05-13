# PLAN for Shared Library and Refactoring

## 1. Library Design
We will create a minimal, token-based I/O utility plus common math helpers to cover repeated patterns across problems.

### Input/Output Utilities
- `ni() -> int`: Read next token as integer.
- `ns() -> str`: Read next token as string.
- `na(n: int) -> List[int]`: Read next `n` tokens as a list of integers.

### Math Utilities
- `gcd(a, b) -> int`: Greatest common divisor.
- `lcm(a, b) -> int`: Least common multiple.
- `is_prime(n) -> bool`: Primality test via trial division.
- `prime_factors(n) -> List[int]`: Prime factorization (with repetition).
- `unique_prime_factors(n) -> List[int]`: Sorted list of unique prime factors.
- `divisors(n) -> List[int]`: Sorted list of all divisors of `n`.

### Additional Helpers (if needed)
- `prefix_sums(arr: List[int]) -> List[int]`: Compute prefix sums.

## 2. Refactoring Strategy
For each problem directory:
1. Replace raw `input()` and `map(int, input().split())` calls with `ni()`, `na()` or `ns()`.
2. Replace custom math routines (gcd loops, prime checks, factorization) with library calls.
3. Remove unused imports and helper classes from `main.py`.
4. Import only needed functions: `from library import ni, na, gcd, prime_factors, ...`.
5. Run `bash {problem}/run.sh` to verify all tests pass.

Maintain a checklist of refactored problems below.

## 3. Refactoring Checklist
* [x] 1068_b_lcm_2510
* [x] 1076_b_divisor_subtraction_738
* [x] 1091_c_new_year_and_the_sphere_transmission_1262
* [x] 1110_c_meaningless_operations_3658
* [x] 1141_a_game_23_2618
* [x] 1228_c_primes_and_multiplication_13032
* [x] 1242_a_tile_painting_5747
* [x] 1243_c_tile_painting_2415
* [x] 1294_c_product_of_three_numbers_4292  # refactored with divisor search algorithm
* [ ] 1295_d_same_gcds_6373
* [ ] 1343_a_candies_8456
* [ ] 1360_d_buying_shovels_6584
* [ ] 1362_a_johnny_and_ancient_computer_1692
* [ ] 1374_b_multiply_by_2_divide_by_6_231
* [ ] 1444_a_division_6380
* [ ] 1454_d_number_into_sequence_7733
* [ ] 150_a_win_or_freeze_5134
* [ ] 151_c_win_or_freeze_133
* [ ] 177_b1_rectangular_game_2533
* [ ] 271_e_three_horses_3683
* [ ] 288_c_polo_the_penguin_and_xor_operation_9826
* [ ] 371_b_fox_dividing_cheese_352
* [ ] 487_c_prefix_product_sequence_2443
* [ ] 576_a_vasya_and_petyas_game_7650
* [ ] 680_c_bear_and_prime_100_4430
* [ ] 762_a_kth_divisor_5057
* [ ] 803_f_coprime_subsequences_8909
* [ ] 893_e_counting_arrays_6936
* [ ] 98_b_help_king_3609
* [ ] 99_d_help_king_8501
