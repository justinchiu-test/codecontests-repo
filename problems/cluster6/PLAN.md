# Library Plan for Cluster 6

Based on my analysis of the problem solutions in this cluster, I've identified several common patterns and functions that can be extracted into a reusable library. The problems in this cluster are primarily focused on math, probability, combinatorics, and dynamic programming.

## Library Structure

The library will be organized into the following main modules:

### 1. Input/Output Utilities

```python
# Fast input reading
def read_int():
    """Read a single integer from stdin."""
    return int(input())

def read_ints():
    """Read multiple integers from a single line."""
    return list(map(int, input().split()))

def read_float():
    """Read a single float from stdin."""
    return float(input())

def read_floats():
    """Read multiple floats from a single line."""
    return list(map(float, input().split()))
```

### 2. Mathematical Utilities

```python
# Constants
MOD = 10**9 + 7  # Common modulo value used in many problems

# Basic math functions
def gcd(a, b):
    """Calculate the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate the least common multiple of a and b."""
    return a * b // gcd(a, b)

# Modular arithmetic
def mod_pow(x, y, m=MOD):
    """Fast modular exponentiation: x^y % m."""
    if x == 0:
        return 0
    res = 1
    x = x % m
    while y > 0:
        if y & 1:
            res = (res * x) % m
        y = y >> 1
        x = (x * x) % m
    return res

def mod_inverse(x, m=MOD):
    """Calculate the modular multiplicative inverse of x."""
    return mod_pow(x, m - 2, m)

# Combinatorial functions
def factorial(n, m=MOD):
    """Calculate n! % m."""
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % m
    return result

def combination(n, k, m=MOD):
    """Calculate nCk % m using modular arithmetic."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    # Calculate using modular arithmetic to avoid overflow
    num = 1
    den = 1
    for i in range(k):
        num = (num * (n - i)) % m
        den = (den * (i + 1)) % m
    return (num * mod_inverse(den, m)) % m

# Fraction simplification
def simplify_fraction(numerator, denominator):
    """Simplify a fraction to its lowest terms."""
    g = gcd(numerator, denominator)
    return numerator // g, denominator // g
```

### 3. Probability Utilities

```python
def expected_value(probabilities, values):
    """Calculate the expected value given probability and value arrays."""
    return sum(p * v for p, v in zip(probabilities, values))

def conditional_probability(event_and_condition, condition):
    """Calculate the conditional probability: P(A|B) = P(A∩B) / P(B)."""
    if condition == 0:
        return 0
    return event_and_condition / condition
```

### 4. Dynamic Programming Utilities

```python
def memoize(func):
    """Decorator to memoize a function."""
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper
```

## Specific Functions for Common Problem Patterns

```python
# Probability transition calculation
def probability_transition(states, transitions, initial=None):
    """
    Calculate the probability distribution after applying transitions.

    Args:
        states: List of possible states
        transitions: Dictionary mapping from state to {next_state: probability}
        initial: Initial probability distribution (uniform if None)

    Returns:
        Final probability distribution
    """
    if initial is None:
        initial = {state: 1.0 / len(states) for state in states}

    result = {state: 0.0 for state in states}
    for state, prob in initial.items():
        for next_state, trans_prob in transitions[state].items():
            result[next_state] += prob * trans_prob

    return result

# Matrix operations for DP
def matrix_multiply(A, B, mod=MOD):
    """Multiply two matrices with mod arithmetic."""
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod

    return C

def matrix_power(A, n, mod=MOD):
    """Calculate A^n with mod arithmetic."""
    rows = len(A)
    result = [[1 if i == j else 0 for j in range(rows)] for i in range(rows)]

    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, A, mod)
        A = matrix_multiply(A, A, mod)
        n //= 2

    return result
```

## Refactoring Checklist

As I refactor each problem, I will track progress here. For each problem, I will:
1. Analyze the solution
2. Identify library components that can be used
3. Refactor the solution
4. Test to ensure it still passes

| Problem ID | Status | Notes |
|------------|--------|-------|
| 108_d_basketball_team_11673 | Pending | |
| 1111_d_destroy_the_colony_7405 | Pending | |
| 1172_c1_nauuo_and_pictures_easy_version_2723 | Pending | |
| 1172_c2_nauuo_and_pictures_hard_version_13029 | Pending | |
| 1187_f_expected_square_beauty_12302 | Pending | |
| 1245_e_hyakugoku_and_ladders_2311 | Pending | |
| 1264_c_beautiful_mirrors_with_queries_6684 | Pending | |
| 1349_d_slime_and_biscuits_751 | Pending | |
| 145_c_lucky_subsequence_8670 | Pending | |
| 1461_c_random_events_9295 | Pending | |
| 1475_e_advertising_agency_1071 | Pending | |
| 148_d_bag_of_mice_3571 | Pending | |
| 1541_d_tree_array_2740 | Pending | |
| 1543_c_need_for_pink_slips_3469 | Pending | |
| 160_c_find_pair_12111 | Pending | |
| 167_b_wizards_and_huge_prize_1597 | Pending | |
| 261_b_maxim_and_restaurant_4932 | Pending | |
| 262_d_maxim_and_restaurant_7013 | Pending | |
| 28_c_bath_queue_2018 | Pending | |
| 442_b_andrey_and_problem_4212 | Pending | |
| 50_d_bombing_7752 | Pending | |
| 518_d_ilya_and_escalator_1612 | Pending | |
| 521_d_shop_3485 | Pending | |
| 540_d_bad_luck_island_6817 | Pending | |
| 54_c_first_digit_law_6609 | Pending | |
| 623_d_birthday_6300 | Pending | |
| 785_d_anton_and_school__2_9951 | Pending | |
| 817_b_makes_and_the_product_1937 | Pending | |
| 908_d_new_year_and_arbitrary_arrangement_7769 | Pending | |
| 9_a_die_roll_1319 | Pending | |

## Implementation Notes

1. Start with the most commonly used math and probability functions, as these appear across many problems.
2. Add specialized functions for DP problems with similar patterns.
3. Implement I/O utilities that help standardize input parsing across problems.
4. Add specialized functions for specific problem patterns as they are identified during refactoring.

## Expected Benefits

1. **Code Reduction**: Functions like `mod_pow`, `factorial`, and `combination` appear in multiple problems and can be reused.
2. **Improved Readability**: Standard library functions will have clear names and documentation.
3. **Consistency**: Common operations will be handled the same way across problems.
4. **Reduced Bugs**: Well-tested library functions are less likely to contain errors.

As I refactor each problem, I'll update this plan with additional patterns and utility functions that emerge.
