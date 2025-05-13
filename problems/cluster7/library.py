"""
Library file for cluster7.
This contains shared code that can be imported by problems in this cluster.
"""

# ===== Input/Output Utilities =====

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

def print_yes_no(condition):
    """Print YES if condition is True, otherwise NO."""
    print("YES" if condition else "NO")

def print_answer(condition, yes_msg="YES", no_msg="NO"):
    """Print yes_msg if condition is True, otherwise no_msg."""
    print(yes_msg if condition else no_msg)

def print_count_and_array(count, arr):
    """Print count followed by space-separated array elements."""
    print(f"{count} {' '.join(map(str, arr))}")

def print_matrix(matrix, row_sep="\n", col_sep=" "):
    """Print a matrix with the given separators."""
    for row in matrix[:-1]:
        print(col_sep.join(map(str, row)), end=row_sep)
    if matrix:
        print(col_sep.join(map(str, matrix[-1])))

# ===== Bit Manipulation Utilities =====

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
    return n + 1

def max_bit_position(n):
    """Return the position of the highest set bit (0-indexed)."""
    return n.bit_length() - 1 if n > 0 else 0

# ===== XOR-Specific Utilities =====

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

def min_cogrowing_sequence(arr):
    """
    Calculate the minimum sequence b such that a XOR b is non-decreasing
    and each b[i] is the minimum possible value.
    """
    sequence = []
    prev_value = 0

    for value in arr:
        # Find the minimum value that needs to be XORed to make the sequence non-decreasing
        n = prev_value & (prev_value ^ value)
        prev_value = value ^ n
        sequence.append(n)

    return sequence

def can_have_equal_xor_segments(arr):
    """
    Check if an array can be split into segments where each segment has the same XOR value.

    This handles three cases:
    1. Total XOR is 0 and there's at least one non-zero segment
    2. Array can be split into exactly 2 segments with equal XOR
    3. Array can be split into 3+ segments with equal XOR

    Returns True if possible, False otherwise.
    """
    n = len(arr)
    total_xor = xor_sum(arr)

    # Case 1: If the total XOR is 0, check for non-zero segment
    if total_xor == 0:
        prefix_xor = 0
        for i in range(n - 1):
            prefix_xor ^= arr[i]
            if prefix_xor != 0:
                return True
        # If all elements are 0, the answer is still Yes
        return True

    # Case 2: Check if we can split into exactly 2 segments with equal XOR
    prefix_xor = 0
    for i in range(n - 1):
        prefix_xor ^= arr[i]
        if prefix_xor == (total_xor ^ prefix_xor):
            return True

    # Case 3: Check if all segments have the same XOR
    segment_xor = 0
    segments_found = 0

    for num in arr:
        segment_xor ^= num
        if segment_xor == total_xor:
            segments_found += 1
            segment_xor = 0

    # We need at least 2 full segments with XOR = total_xor and no remainder
    return segments_found >= 2 and segment_xor == 0

def find_xor_mapping_key(numbers):
    """
    Find a key k such that XORing each number in the set with k
    gives another number in the same set.

    Returns the smallest such k, or -1 if no such k exists.
    """
    numbers_set = set(numbers)

    # Only need to check values up to 1024 based on problem constraints
    for k in range(1, 1025):
        valid = True

        # Check if XORing each number with k gives another number in the set
        for num in numbers_set:
            if num ^ k not in numbers_set:
                valid = False
                break

        if valid:
            return k

    return -1

def count_xor_pairs_with_parity(arr):
    """
    Count pairs of subarrays with the same XOR and same parity.
    Used for problems like Sasha and a Bit of Relax.
    """
    n = len(arr)
    prefix_xor = xor_prefix_array(arr)

    # Separate dictionaries for even and odd indices
    even_xor_count = {0: 1}  # Start with 0 (empty prefix)
    odd_xor_count = {}
    count = 0

    for i in range(1, n + 1):
        xor_val = prefix_xor[i]

        if i % 2 == 0:
            # Current index is even
            if xor_val in even_xor_count:
                count += even_xor_count[xor_val]
            even_xor_count[xor_val] = even_xor_count.get(xor_val, 0) + 1
        else:
            # Current index is odd
            if xor_val in odd_xor_count:
                count += odd_xor_count[xor_val]
            odd_xor_count[xor_val] = odd_xor_count.get(xor_val, 0) + 1

    return count

# ===== Matrix and Array Operations =====

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

# ===== Common Problem-Specific Functions =====

def sequence_with_xor_property(n, x):
    """
    Try to find a sequence of n integers with XOR equal to x.
    Returns the sequence or None if impossible.
    """
    if n == 1:
        return [x]

    if n == 2:
        if x == 0:
            return None  # Can't have 2 numbers with XOR 0
        return [x, 0]

    # Special case for n=3, x=0
    if n == 3 and x == 0:
        return [1 << 17, 1 << 18, (1 << 17) ^ (1 << 18)]

    # For n >= 3, we can always construct a sequence
    a = 1 << 17  # 131072
    b = 1 << 18  # 262144

    result = []
    current_xor = 0

    # Generate first n-3 numbers
    for i in range(n-3):
        num = i + 1
        result.append(num)
        current_xor ^= num

    # Add the last 3 numbers to achieve the desired XOR
    if current_xor == x:
        result.extend([b, a, a ^ b])
    else:
        result.extend([0, a, a ^ current_xor ^ x])

    return result

def construct_balanced_array(n, x):
    """
    Construct an array of n integers with XOR equal to x.
    For problems related to finding collections with specific XOR properties.
    """
    if x == 0:
        return [0] * n

    if n == 1:
        return [x]

    # Generate standard powers of 2 to use as building blocks
    powers = []
    num = x
    while num:
        highest_bit = 1 << (num.bit_length() - 1)
        powers.append(highest_bit)
        num ^= highest_bit

    result = []
    if len(powers) <= n:
        # We can just use powers with remaining zeros
        result = powers + [0] * (n - len(powers))
    else:
        # We need to combine some powers
        for i in range(n - 1):
            if i < len(powers):
                result.append(powers[i])
            else:
                result.append(0)

        # Last element is XOR of remaining powers
        remaining_xor = 0
        for i in range(n - 1, len(powers)):
            remaining_xor ^= powers[i]
        result.append(remaining_xor)

    return result