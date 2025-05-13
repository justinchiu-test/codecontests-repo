#!/usr/bin/env python3

from library import read_str

def minlexes():
    """
    Solution for the Minlexes problem.

    The task is to find the lexicographically smallest strings that can be
    obtained by applying a specific algorithm to the suffixes of a given string.
    """
    # Read the input string
    s = read_str()
    string_length = len(s)

    # Handle the trivial case of a single character string
    if string_length == 1:
        return [(1, s[0])]

    # Initialize with the last two characters
    result_strings = [s[-1]]
    result_lengths = [1]

    # Process the second last character
    if s[-2] != s[-1]:
        result_strings.append(s[-2] + s[-1])
        result_lengths.append(2)
    else:
        # If the last two characters are the same, they can be removed
        result_strings.append("")
        result_lengths.append(0)

    # Process the rest of the string from right to left
    for i in range(string_length - 3, -1, -1):
        current_char = s[i]

        # Add current character to the previous result
        new_string = current_char + result_strings[-1]
        new_length = result_lengths[-1] + 1

        # Format long strings according to the problem requirements
        if new_length > 10:
            new_string = new_string[:5] + "..." + new_string[-2:]

        # Check if removing a pair of identical characters gives a better result
        if current_char == s[i + 1] and new_string > result_strings[-2]:
            new_string = result_strings[-2]
            new_length = result_lengths[-2]

        result_strings.append(new_string)
        result_lengths.append(new_length)

    # Prepare the output in required format
    results = []
    for i in range(string_length - 1, -1, -1):
        results.append((result_lengths[i], result_strings[i]))

    return results

# Print the results
for length, string in minlexes():
    print(length, string)
