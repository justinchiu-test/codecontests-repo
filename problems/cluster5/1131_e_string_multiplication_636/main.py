#!/usr/bin/env python3

from library import read_int, read_str

# Constants
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
MAX_BEAUTY = 10**9

def count_max_consecutive(s: str) -> dict:
    """
    Count the maximum consecutive occurrences of each character in a string.

    Args:
        s: Input string

    Returns:
        Dictionary mapping each character to its maximum consecutive occurrences
    """
    # Initialize counts for all lowercase letters
    counts = {ch: 0 for ch in ALPHABET}

    i = 0
    while i < len(s):
        # Find consecutive run of the same character
        j = i + 1
        while j < len(s) and s[i] == s[j]:
            j += 1

        # Update max consecutive count for this character
        counts[s[i]] = max(counts[s[i]], j - i)

        # Move to the next different character
        i = j

    return counts

def compute_next_counts(current_counts: dict, next_string: str) -> dict:
    """
    Compute the maximum consecutive character counts after multiplication.

    Args:
        current_counts: Current character counts from previous multiplications
        next_string: The next string to multiply with

    Returns:
        Updated character counts after multiplication
    """
    # Get counts for the next string
    next_counts = count_max_consecutive(next_string)

    # Characters that were present before but not in the new string
    # will appear at least once (surrounded by the new string)
    for ch in ALPHABET:
        if current_counts[ch] > 0 and next_counts[ch] == 0:
            next_counts[ch] = 1

    # Count consecutive characters at the beginning of the string
    prefix_count = 0
    while prefix_count < len(next_string) and next_string[prefix_count] == next_string[0]:
        prefix_count += 1

    # Count consecutive characters at the end of the string
    suffix_count = 0
    while suffix_count < len(next_string) and next_string[-1 - suffix_count] == next_string[-1]:
        suffix_count += 1

    # Handle special cases based on whether the first and last characters are the same
    if next_string[0] == next_string[-1]:
        # If the string consists of only one character repeated
        if prefix_count == len(next_string):
            # Formula for the beauty when we multiply a string with all same characters
            next_counts[next_string[0]] = max(
                next_counts[next_string[0]],
                current_counts[next_string[0]] + (current_counts[next_string[0]] + 1) * len(next_string)
            )
        # If the character existed before, we can connect prefix and suffix
        elif current_counts[next_string[0]] > 0:
            next_counts[next_string[0]] = max(
                next_counts[next_string[0]],
                prefix_count + 1 + suffix_count
            )
    else:
        # For different start/end characters, handle them separately
        next_counts[next_string[0]] = max(
            next_counts[next_string[0]],
            prefix_count + (current_counts[next_string[0]] > 0)
        )
        next_counts[next_string[-1]] = max(
            next_counts[next_string[-1]],
            suffix_count + (current_counts[next_string[-1]] > 0)
        )

    # Cap values at the maximum beauty to avoid integer overflow
    return {x: min(MAX_BEAUTY, y) for x, y in next_counts.items()}

def main():
    n = read_int()
    # Process the first string
    counts = count_max_consecutive(read_str())

    # Process the remaining strings
    for _ in range(n - 1):
        counts = compute_next_counts(counts, read_str())

    # The beauty is the maximum consecutive count of any character
    print(max(counts.values()))

if __name__ == "__main__":
    main()