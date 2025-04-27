"""
Input/output utilities for competitive programming.
"""

from typing import Any, Callable, List, Optional, Tuple, TypeVar

T = TypeVar("T")


def read_int() -> int:
    """Read a single integer from stdin."""
    return int(input())


def read_ints() -> List[int]:
    """Read a list of integers from a single line."""
    return list(map(int, input().split()))


def read_int_tuple() -> Tuple[int, ...]:
    """Read integers from a line as a tuple."""
    return tuple(map(int, input().split()))


def read_int_pair() -> Tuple[int, int]:
    """Read two integers from a line."""
    a, b = map(int, input().split())
    return a, b


def read_int_triple() -> Tuple[int, int, int]:
    """Read three integers from a line."""
    a, b, c = map(int, input().split())
    return a, b, c


def read_str() -> str:
    """Read a single string from stdin."""
    return input().strip()


def read_strs() -> List[str]:
    """Read a list of strings from a single line."""
    return input().split()


def read_matrix(
    n: int, m: Optional[int] = None, t: Callable[[str], T] = int
) -> List[List[T]]:
    """Read an n×m matrix (or n×n if m is not provided).

    Args:
        n: Number of rows
        m: Number of columns (if None, assumed to be n)
        t: Function to convert elements (default: int)

    Returns:
        List of lists containing the matrix elements
    """
    if m is None:
        m = n
    return [list(map(t, input().split())) for _ in range(n)]


def read_grid(n: int, m: Optional[int] = None) -> List[str]:
    """Read a grid of characters.

    Args:
        n: Number of rows
        m: Number of columns (unused but included for API consistency)

    Returns:
        List of strings, each representing a row of the grid
    """
    return [input() for _ in range(n)]


def read_lines(n: int) -> List[str]:
    """Read n lines of input."""
    return [input() for _ in range(n)]


def print_grid(grid: List[str]) -> None:
    """Print a grid of characters."""
    for row in grid:
        print(row)


def print_yes_no(condition: bool, uppercase: bool = True) -> None:
    """Print YES/NO based on condition."""
    if uppercase:
        print("YES" if condition else "NO")
    else:
        print("Yes" if condition else "No")


def print_possible(condition: bool, uppercase: bool = False) -> None:
    """Print Possible/Impossible based on condition."""
    if uppercase:
        print("POSSIBLE" if condition else "IMPOSSIBLE")
    else:
        print("Possible" if condition else "Impossible")


def print_case(case_num: int, result: Any) -> None:
    """Print the result of a test case."""
    print(f"Case #{case_num}: {result}")
