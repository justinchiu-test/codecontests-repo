# Library Plan for Cluster1 (Number Theory and Math Problems)

## Overview

After analyzing the solutions in cluster1, I've identified that most problems are focused on number theory, mathematical operations, and related algorithms. The plan is to create a comprehensive library that abstracts common patterns and utilities found across these problems.

## Components

### 1. Input/Output Utilities

Many solutions start with similar I/O patterns:

```python
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input_int(): return int(sys.stdin.readline().strip())
def input_str(): return sys.stdin.readline().strip()
```

### 2. Number Theory Functions

Most problems require various number theory operations:

#### Prime Numbers
- `is_prime(n)`: Check if a number is prime
- `sieve_of_eratosthenes(n)`: Generate all primes up to n using Sieve
- `prime_factors(n)`: Get prime factorization of a number
- `get_all_prime_factors(n)`: Get all prime factors of a number (without repetition)

#### Divisors and Factors
- `get_all_divisors(n)`: Get all divisors of a number
- `count_divisors(n)`: Count the number of divisors of a number
- `get_kth_divisor(n, k)`: Get the kth divisor of n

#### GCD and LCM
- `gcd(a, b)`: Greatest common divisor
- `lcm(a, b)`: Least common multiple
- `extended_gcd(a, b)`: Extended Euclidean Algorithm
- `modular_inverse(a, m)`: Calculate modular inverse

### 3. Modular Arithmetic

- `mod_pow(base, exp, mod)`: Calculate (base^exp) % mod efficiently
- `mod_add(a, b, mod)`: Calculate (a + b) % mod
- `mod_multiply(a, b, mod)`: Calculate (a * b) % mod
- `mod_divide(a, b, mod)`: Calculate (a / b) % mod

### 4. Combinatorics

- `factorial(n, mod=None)`: Calculate n! (with optional modulo)
- `nCr(n, r, mod=None)`: Calculate combinations (n choose r)
- `nPr(n, r, mod=None)`: Calculate permutations
- `modular_factorial_precomputation`: Precompute factorials and inverses

### 5. Bit Manipulation

- `count_set_bits(n)`: Count number of set bits in n
- `is_power_of_two(n)`: Check if n is a power of two
- `next_power_of_two(n)`: Get next power of two
- `bit_operations`: Various bit manipulation utilities

### 6. Advanced Data Structures

- `SegmentTree`: Implementation for range queries
- `BIT (Binary Indexed Tree)`: For prefix sums and updates
- `LazySegmentTree`: For range updates and queries

## Implementation Strategy

1. Start with the most commonly used functions (I/O, prime checks, GCD/LCM, factorization)
2. Add more specialized functions as needed when refactoring specific problems
3. Maintain consistent function signatures and naming conventions
4. Add proper documentation for each function

## Checklist of Refactored Problems

This section will track our progress as we refactor each problem to use the library.

- [ ] 762_a_kth_divisor_5057
- [ ] 1076_b_divisor_subtraction_738
- [ ] 680_c_bear_and_prime_100_4430
- [ ] 1374_b_multiply_by_2_divide_by_6_231
- [ ] 1068_b_lcm_2510
- [ ] 1295_d_same_gcds_6373
- [ ] 1228_c_primes_and_multiplication_13032
- [ ] 893_e_counting_arrays_6936
- [ ] 1110_c_meaningless_operations_3658
- [ ] 1141_a_game_23_2618
- [ ] 1242_a_tile_painting_5747
- [ ] 1243_c_tile_painting_2415
- [ ] 1294_c_product_of_three_numbers_4292
- [ ] 1343_a_candies_8456
- [ ] 1360_d_buying_shovels_6584
- [ ] 1362_a_johnny_and_ancient_computer_1692
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
- [ ] 803_f_coprime_subsequences_8909
- [ ] 98_b_help_king_3609
- [ ] 99_d_help_king_8501

## Conclusion

The library will focus on providing robust, reusable components for number theory and mathematical operations. By abstracting common patterns, we'll significantly reduce code duplication and make the solutions more concise and maintainable.
