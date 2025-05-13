"""
Library file for cluster7.
This contains shared code that can be imported by problems in this cluster.
"""

import sys
from typing import List, Tuple, Dict, Set, Optional, Union, Callable, Any, Iterable

# Fast I/O for competitive programming
def fast_input() -> str:
    return sys.stdin.readline().rstrip()

def fast_int() -> int:
    return int(fast_input())

def fast_ints() -> Tuple[int, ...]:
    return tuple(map(int, fast_input().split()))

def fast_int_list() -> List[int]:
    return list(map(int, fast_input().split()))

def fast_int_grid(n: int) -> List[List[int]]:
    """Read n lines of integers as a grid."""
    return [fast_int_list() for _ in range(n)]

# XOR operations
def xor_list(lst: List[int]) -> int:
    """XOR all elements in a list."""
    result = 0
    for x in lst:
        result ^= x
    return result

def xor_range(n: int) -> int:
    """Calculate XOR of all numbers from 1 to n.
    This has a pattern: 
    1..n = [n, 1, n+1, 0][n % 4]
    """
    return [n, 1, n+1, 0][n % 4]

def prefix_xor(arr: List[int]) -> List[int]:
    """Calculate prefix XOR array."""
    pref = [0]
    for num in arr:
        pref.append(pref[-1] ^ num)
    return pref

def get_xor_mask(n: int) -> int:
    """Get a bit mask with all 1s for n bits."""
    return (1 << n) - 1

def count_bits(n: int) -> int:
    """Count the number of set bits in an integer."""
    return bin(n).count('1')

def is_bit_set(n: int, pos: int) -> bool:
    """Check if bit at position pos is set in n."""
    return (n & (1 << pos)) != 0

def set_bit(n: int, pos: int) -> int:
    """Set bit at position pos in n."""
    return n | (1 << pos)

def clear_bit(n: int, pos: int) -> int:
    """Clear bit at position pos in n."""
    return n & ~(1 << pos)

def find_lowest_set_bit(n: int) -> int:
    """Find position of the lowest set bit in n."""
    if n == 0:
        return -1
    return (n & -n).bit_length() - 1

# Common output functions
def yes():
    print("YES")

def no():
    print("NO")

def answer(condition: bool):
    """Print YES if condition is True, NO otherwise."""
    print("YES" if condition else "NO")

def tak():
    """Print TAK (Polish for YES)."""
    print("TAK")

def nie():
    """Print NIE (Polish for NO)."""
    print("NIE")

def print_matrix(matrix: List[List[int]], sep: str = ' '):
    """Print a 2D matrix."""
    for row in matrix:
        print(sep.join(map(str, row)))

def print_list(lst: List[Any], sep: str = ' '):
    """Print a list with the given separator."""
    print(sep.join(map(str, lst)))

# Useful for matrix problems
def create_matrix(n: int, m: int, default_value: Any = 0) -> List[List[Any]]:
    """Create a 2D matrix of size n×m with default_value."""
    return [[default_value for _ in range(m)] for _ in range(n)]

def create_3d_array(n: int, m: int, p: int, default_value: Any = 0) -> List[List[List[Any]]]:
    """Create a 3D array of size n×m×p with default_value."""
    return [[[default_value for _ in range(p)] for _ in range(m)] for _ in range(n)]

# For binary search
def binary_search(low: int, high: int, predicate: Callable[[int], bool]) -> int:
    """Binary search in [low, high] range.
    Returns highest value where predicate is True, or low-1 if none found.
    """
    while low <= high:
        mid = (low + high) // 2
        if predicate(mid):
            low = mid + 1
        else:
            high = mid - 1
    return high

# For many problems requiring indices
def one_indexed(func):
    """Decorator to convert 0-indexed functions to 1-indexed."""
    def wrapper(*args, **kwargs):
        # Convert 1-indexed inputs to 0-indexed
        args = list(args)
        for i in range(len(args)):
            if isinstance(args[i], int):
                args[i] -= 1
        
        # Call the function with 0-indexed parameters
        result = func(*args, **kwargs)
        
        # If returning an index or list of indices, convert back to 1-indexed
        if isinstance(result, int):
            return result + 1
        elif isinstance(result, list) and result and isinstance(result[0], int):
            return [i + 1 for i in result]
        
        return result
    return wrapper