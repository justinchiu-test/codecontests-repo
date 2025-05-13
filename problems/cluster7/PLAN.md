# Library Design Plan for Cluster7

After analyzing the problems in cluster7, it's clear that most problems are focused on bitwise operations, particularly XOR (^). The library should provide utility functions for common bit manipulation tasks and input/output operations.

## Core Components

### 1. Input/Output Utilities

```python
def read_int():
    """Read a single integer from input."""
    return int(input())

def read_ints():
    """Read space-separated integers from input."""
    return list(map(int, input().split()))

def read_int_pair():
    """Read two space-separated integers."""
    return map(int, input().split())

def read_int_matrix(rows):
    """Read a matrix of integers with given number of rows."""
    return [read_ints() for _ in range(rows)]

def read_test_cases(processor_fn):
    """Read multiple test cases and process each with the given function."""
    t = read_int()
    results = []
    for _ in range(t):
        results.append(processor_fn())
    return results

def print_array(arr, sep=" "):
    """Print an array with the given separator."""
    print(sep.join(map(str, arr)))

def print_matrix(matrix, row_sep="\n", col_sep=" "):
    """Print a matrix with the given separators."""
    print(row_sep.join(col_sep.join(map(str, row)) for row in matrix))

def print_yes_no(condition):
    """Print YES if condition is True, otherwise NO."""
    print("YES" if condition else "NO")
```

### 2. Bit Manipulation Utilities

```python
def bit_count(n):
    """Count the number of set bits in an integer."""
    return bin(n).count('1')

def get_bit(n, position):
    """Get the bit value at a specific position."""
    return (n >> position) & 1

def set_bit(n, position):
    """Set the bit at a specific position to 1."""
    return n | (1 << position)

def clear_bit(n, position):
    """Clear the bit at a specific position to 0."""
    return n & ~(1 << position)

def toggle_bit(n, position):
    """Toggle the bit at a specific position."""
    return n ^ (1 << position)

def is_power_of_two(n):
    """Check if a number is a power of 2."""
    return n > 0 and (n & (n - 1)) == 0

def next_power_of_two(n):
    """Get the next power of 2 greater than or equal to n."""
    if n <= 0:
        return 1
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    n |= n >> 32
    return n + 1
```

### 3. XOR-Specific Utilities

```python
def xor_sum(arr):
    """Calculate the XOR of all elements in the array."""
    result = 0
    for x in arr:
        result ^= x
    return result

def xor_prefix_array(arr):
    """Create a prefix XOR array (with 0 at the beginning)."""
    prefix = [0]
    for x in arr:
        prefix.append(prefix[-1] ^ x)
    return prefix

def xor_range(start, end):
    """Calculate XOR of all numbers from start to end (inclusive) efficiently."""
    def xor_1_to_n(n):
        mod = n % 4
        if mod == 0:
            return n
        if mod == 1:
            return 1
        if mod == 2:
            return n + 1
        return 0
    
    return xor_1_to_n(end) ^ xor_1_to_n(start - 1) if start > 0 else xor_1_to_n(end)
```

### 4. Matrix and Array XOR Operations

```python
def transpose(matrix):
    """Transpose a matrix."""
    return [list(row) for row in zip(*matrix)]

def xor_rows(matrix):
    """Calculate XOR of each row in the matrix."""
    return [xor_sum(row) for row in matrix]

def xor_cols(matrix):
    """Calculate XOR of each column in the matrix."""
    return xor_rows(transpose(matrix))

def create_matrix(rows, cols, default_value=0):
    """Create a matrix with the specified dimensions and default value."""
    return [[default_value for _ in range(cols)] for _ in range(rows)]
```

## Integration in Solutions

The library components will be used in solutions by:

1. Replacing common input parsing code with library functions
2. Using XOR utility functions to simplify bit manipulation operations
3. Leveraging array/matrix operations to reduce boilerplate code

This approach will significantly reduce the code size of each solution while maintaining readability and correctness.

## Implementation Plan

1. Implement the core IO utilities first
2. Add basic bit manipulation functions
3. Implement XOR-specific utilities
4. Add matrix/array operations as needed
5. Refactor solutions to use the library, starting with the simplest ones
6. Test each refactored solution to ensure correctness
7. Continue refining the library based on patterns discovered during refactoring