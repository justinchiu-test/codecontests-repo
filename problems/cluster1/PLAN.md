# Library Design Plan for Cluster1

## Overview

Based on an analysis of the problems in cluster1, I've identified several common patterns and functionalities that can be extracted into a shared library. This cluster primarily contains problems related to number theory, math, and computational algorithms.

## Common Patterns

1. **Number Theory Operations**
   - Prime factorization
   - Finding divisors/factors of numbers
   - Primality testing
   - GCD/LCM calculations
   - Modular arithmetic (including modular exponentiation)

2. **Input/Output Patterns**
   - Reading multiple integers from a line
   - Handling test cases
   - Formatted output

3. **Utility Functions**
   - Mathematical helper functions
   - Optimization techniques (square root optimization for divisors)
   - Handling large numbers

## Library Structure

The library will be organized into the following modules:

### 1. Prime Number Operations
- `is_prime(n)`: Check if a number is prime
- `prime_factors(n)`: Get all prime factors of a number
- `get_unique_prime_factors(n)`: Get unique prime factors of a number

### 2. Divisors and Factors
- `get_all_divisors(n)`: Find all divisors of a number
- `get_kth_divisor(n, k)`: Find the kth divisor of a number

### 3. Mathematical Operations
- `gcd(a, b)`: Greatest common divisor
- `lcm(a, b)`: Least common multiple
- `mod_pow(base, exp, mod)`: Modular exponentiation

### 4. Input/Output Utilities
- `read_int()`: Read a single integer
- `read_ints()`: Read multiple integers from a line
- `read_test_cases()`: Handle reading multiple test cases

## Implementation Strategy

1. Start with core number theory functions that appear in multiple problems
2. Add I/O utilities to simplify reading input and formatting output
3. Add specialized functions for specific problem patterns
4. Refactor problems to use the library components

## Refactoring Checklist

- [x] 1068_b_lcm_2510
- [x] 1076_b_divisor_subtraction_738
- [x] 1091_c_new_year_and_the_sphere_transmission_1262
- [x] 1110_c_meaningless_operations_3658
- [x] 1141_a_game_23_2618
- [x] 1228_c_primes_and_multiplication_13032
- [x] 1242_a_tile_painting_5747
- [x] 1243_c_tile_painting_2415
- [x] 1294_c_product_of_three_numbers_4292
- [x] 1295_d_same_gcds_6373
- [x] 1343_a_candies_8456
- [x] 1360_d_buying_shovels_6584
- [x] 1362_a_johnny_and_ancient_computer_1692
- [x] 1374_b_multiply_by_2_divide_by_6_231
- [x] 1444_a_division_6380
- [x] 1454_d_number_into_sequence_7733
- [x] 150_a_win_or_freeze_5134
- [ ] 151_c_win_or_freeze_133
- [x] 177_b1_rectangular_game_2533
- [ ] 271_e_three_horses_3683
- [ ] 288_c_polo_the_penguin_and_xor_operation_9826
- [x] 371_b_fox_dividing_cheese_352
- [x] 487_c_prefix_product_sequence_2443
- [ ] 576_a_vasya_and_petyas_game_7650
- [x] 680_c_bear_and_prime_100_4430
- [x] 762_a_kth_divisor_5057
- [ ] 803_f_coprime_subsequences_8909
- [ ] 893_e_counting_arrays_6936
- [ ] 98_b_help_king_3609
- [ ] 99_d_help_king_8501

## Todo List

1. ✅ Implement core number theory functions in library.py
2. ✅ Implement I/O utilities
3. ⏳ Refactor each problem solution to use the library (20/30 completed)
4. ⏳ Test each refactored solution to ensure it passes all tests (20/30 completed)
5. ⏳ Optimize library functions for performance
6. ⏳ Clean up unused functions

## Library Implementation Progress

We have successfully implemented the following components in our shared library:

### Input/Output Utilities
- ✅ `read_int()` - Read a single integer from stdin
- ✅ `read_ints()` - Read multiple integers from a line
- ✅ `read_int_list()` - Read a list of integers from a line
- ✅ `read_test_cases()` - Parse multiple test cases

### Prime Number Operations
- ✅ `is_prime()` - Check if a number is prime
- ✅ `prime_factors()` - Get all prime factors of a number
- ✅ `get_unique_prime_factors()` - Get unique prime factors of a number
- ✅ `smallest_prime_divisor()` - Find the smallest prime divisor of a number
- ✅ `is_prime_interactive()` - Determine if a hidden number is prime using interactive queries
- ✅ `sieve_of_eratosthenes()` - Generate all primes up to n

### Divisors and Factors
- ✅ `get_all_divisors()` - Find all divisors of a number
- ✅ `get_kth_divisor()` - Get the kth divisor of a number

### Mathematical Operations
- ✅ `gcd()` - Greatest common divisor
- ✅ `lcm()` - Least common multiple
- ✅ `mod_pow()` - Modular exponentiation
- ✅ `euler_totient()` - Calculate Euler's totient function φ(n)
- ✅ `find_primitive_root()` - Find a primitive root modulo p

### Problem-Specific Solutions
- ✅ `game_23_moves()` - Calculate minimum moves for Game 23 problem
- ✅ `min_moves_to_one()` - Calculate minimum moves to make n equal to 1
- ✅ `find_three_factors()` - Find three distinct integers a, b, c where a*b*c = n
- ✅ `tile_painting()` - Solve the tile painting problem
- ✅ `min_packages()` - Find minimum number of packages needed
- ✅ `primes_and_multiplication()` - Solve primes and multiplication problem
- ✅ `divisor_subtraction()` - Find number of subtractions needed to reach 0
- ✅ `sphere_transmission_fun_values()` - Calculate fun values for sphere transmission
- ✅ `solve_candies()` - Find x for the candies problem
- ✅ `min_operations_power_of_two()` - Find minimum operations for power of two transformations
- ✅ `min_operations_cheese()` - Find minimum operations for cheese division
- ✅ `count_coprime_numbers()` - Count numbers with same GCD property
- ✅ `meaningless_operations()` - Find max GCD for XOR and AND operations
- ✅ `max_divisor_not_divisible_by_q()` - Find largest divisor not divisible by q
- ✅ `rectangular_game()` - Solve the rectangular game problem
- ✅ `number_into_sequence()` - Construct a sequence with specific properties
- ✅ `win_or_freeze()` - Determine winner in the Win or Freeze game
- ✅ `prefix_product_sequence()` - Find a sequence with prefix products ≡ 1 (mod p)