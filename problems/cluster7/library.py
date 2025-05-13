"""
Library file for cluster7.
This contains shared code that can be imported by problems in this cluster.
"""

# IO utilities
def read_int():
    """Read a single integer from input."""
    return int(input())

def read_ints():
    """Read a line of integers and return as a list."""
    return list(map(int, input().split()))

def read_int_tuple():
    """Read a line of integers and return as a tuple."""
    return tuple(map(int, input().split()))

def read_2d_array(rows):
    """Read a 2D array of integers."""
    return [read_ints() for _ in range(rows)]

def read_test_cases():
    """Read the number of test cases t, and yield t times."""
    t = read_int()
    for _ in range(t):
        yield

# XOR operations
def xor_list(lst):
    """Compute the XOR of all elements in a list."""
    result = 0
    for x in lst:
        result ^= x
    return result

def xor_range(n):
    """Compute the XOR of all numbers from 0 to n inclusive.

    This uses the pattern that XOR of numbers from 0 to n follows:
    n, 1, n+1, 0 for n % 4 = 0, 1, 2, 3 respectively.
    """
    return [n, 1, n+1, 0][n % 4]

def xor_range_ab(a, b):
    """Compute the XOR of all numbers from a to b inclusive.

    This uses the property that XOR from a to b can be calculated as:
    XOR(0 to b) ^ XOR(0 to a-1)
    """
    return xor_range(b) ^ xor_range(a - 1) if a > 0 else xor_range(b)

def is_xor_zero(lst):
    """Check if the XOR of all elements in a list is zero."""
    return xor_list(lst) == 0

def all_subarray_xors(arr):
    """Compute XORs of all subarrays of the given array and return as a list."""
    n = len(arr)
    result = []
    for i in range(n):
        current_xor = 0
        for j in range(i, n):
            current_xor ^= arr[j]
            result.append(current_xor)
    return result

def prefix_xor(arr):
    """Compute all prefix XORs of the array.

    Returns a list where prefix_xor[i] = XOR of arr[0...i]
    """
    n = len(arr)
    result = [0] * n
    if n > 0:
        result[0] = arr[0]
        for i in range(1, n):
            result[i] = result[i-1] ^ arr[i]
    return result

def xor_in_range(prefix, left, right):
    """Get the XOR of elements in range [left, right] using a prefix XOR array.

    Args:
        prefix: Prefix XOR array (computed using prefix_xor)
        left: Start index (inclusive)
        right: End index (inclusive)

    Returns:
        XOR of elements in range [left, right]
    """
    if left == 0:
        return prefix[right]
    return prefix[right] ^ prefix[left-1]

def is_power_of_two(n):
    """Check if a number is a power of two."""
    return n > 0 and (n & (n - 1)) == 0

def count_set_bits(n):
    """Count the number of set bits in the binary representation of n."""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def highest_bit_position(n):
    """Find the position of the highest set bit in n."""
    pos = 0
    while n:
        pos += 1
        n >>= 1
    return pos

def lowest_bit_position(n):
    """Find the position of the lowest set bit in n."""
    if n == 0:
        return 0
    pos = 1
    while (n & 1) == 0:
        pos += 1
        n >>= 1
    return pos