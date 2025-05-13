# Library Design Plan for Cluster 6

After analyzing the problems in this cluster, I've identified several common patterns that can be abstracted into reusable components. The problems predominantly involve probability calculations, combinatorics, and dynamic programming with mathematical components.

## Key Components

### 1. I/O Utilities
- Fast input/output operations
- Parsing common input patterns (integers, floats, arrays)
- Formatting output with specified precision

### 2. Math Utilities
- GCD, LCM functions
- Factorial and combinations calculator
- Fraction simplification 
- Modular arithmetic helpers
- Matrix operations

### 3. Probability Functions
- Common probability calculations
- Expected value calculation helpers
- Functions for working with combinations in probability contexts

### 4. Dynamic Programming Helpers
- Memoization decorators
- Tabulation helpers
- DP state initialization for common patterns

## Implementation Approach

The library will be structured to maximize code reuse while keeping the functions focused and composable. I'll start with implementing the most commonly used functions first and then add more specialized ones as needed during the refactoring process.

1. First, I'll implement the I/O utilities since they appear in nearly every problem.
2. Next, I'll implement the basic math functions that are widely used.
3. Then I'll add probability-specific functions that can be reused across problems.
4. Finally, I'll add DP helpers and other specialized functions as needed.

As I refactor each problem, I'll continue to update the library to extract common patterns and add new utility functions when beneficial.

## Function Categories and Examples

### I/O Utilities
```python
def read_int():
    """Read a single integer from input"""
    
def read_ints():
    """Read multiple integers from a line"""
    
def read_float():
    """Read a single float from input"""
    
def read_floats():
    """Read multiple floats from a line"""
    
def read_array(converter=int):
    """Read an array with specified converter function"""
    
def print_float(value, precision=6):
    """Print a float with specified precision"""
```

### Math Utilities
```python
def gcd(a, b):
    """Calculate greatest common divisor"""
    
def lcm(a, b):
    """Calculate least common multiple"""
    
def factorial(n):
    """Calculate factorial"""
    
def combinations(n, k):
    """Calculate combinations (n choose k)"""
    
def simplify_fraction(numerator, denominator):
    """Return simplified fraction as (numerator, denominator)"""
```

### Probability Functions
```python
def probability_at_least_one(probability, attempts):
    """Calculate probability of at least one success"""
    
def expected_value(probabilities, values):
    """Calculate expected value given probabilities and values"""
    
def conditional_probability(a, b):
    """Calculate conditional probability P(A|B)"""
```

### DP Helpers
```python
def memoize(func):
    """Memoization decorator for recursive functions"""
    
def init_dp_table(dimensions, initial_value=0):
    """Initialize a DP table with specified dimensions"""
```

I'll adjust this plan as I refactor problems and discover more opportunities for code reuse.