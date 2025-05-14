# Plan

## Library Design

We will implement a shared library with the following components:

### Input Parsing Utilities
- I(): Read a single integer from stdin
- MI(): Read a line of space-separated integers as a map(int, ...)
- LI(): Read a line of space-separated integers as a list
- LLI(n): Read n lines, each as a list of integers
- S(): Read a stripped string
- SS(): Read a line of space-separated strings

### Math Utilities
- gcd(a, b): Greatest common divisor
- lcm(a, b): Least common multiple
- factors(n): List all divisors of n
- is_prime(n): Primality test (O(√n))
- prime_sieve(n): List primes up to n
- factorize(n): Prime factorization as a dict
- nCr(n, r): Compute combinations

Additional utilities will be added as needed when refactoring solutions.

## Refactoring Checklist

We will refactor every problem to use the above library functions.
Mark each as completed when the solution is updated and passes its tests.

- [ ] 1068_b_lcm_2510
- [ ] 1076_b_divisor_subtraction_738
- [ ] 1091_c_new_year_and_the_sphere_transmission_1262
- [ ] 1110_c_meaningless_operations_3658
- [ ] 1141_a_game_23_2618
- [ ] 1228_c_primes_and_multiplication_13032
- [ ] 1242_a_tile_painting_5747
- [ ] 1243_c_tile_painting_2415
- [ ] 1294_c_product_of_three_numbers_4292
- [ ] 1295_d_same_gcds_6373
- [ ] 1343_a_candies_8456
- [ ] 1360_d_buying_shovels_6584
- [ ] 1362_a_johnny_and_ancient_computer_1692
- [ ] 1374_b_multiply_by_2_divide_by_6_231
- [ ] 1444_a_division_6380
- [ ] 1454_d_number_into_sequence_7733
- [ ] 150_a_win_or_freeze_5134
- [ ] 151_c_win_or_freeze_133
- [ ] 177_b1_rectangular_game_2533
- [ ] 271_e_three_horses_3683
- [ ] 288_c_polo_the_penguin_and_xor_operation_9826
- [ ] 371_b_fox_dividing_cheese_352
- [ ] 487_c_prefix_product_sequence_2443
- [ ] 576_a_vasya_and_petyas_game_7650
- [ ] 680_c_bear_and_prime_100_4430
- [ ] 762_a_kth_divisor_5057
- [ ] 803_f_coprime_subsequences_8909
- [ ] 893_e_counting_arrays_6936
- [ ] 98_b_help_king_3609
- [ ] 99_d_help_king_8501
