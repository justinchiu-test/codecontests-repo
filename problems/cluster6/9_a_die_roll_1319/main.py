#!/usr/bin/env python3

from library import read_ints, simplify_fraction, fraction_to_string

def main():
    # Read Yakko's and Wakko's dice values
    x, y = read_ints()

    # Dot wins if the value on the die is at least max(x, y)
    max_val = max(x, y)

    # Calculate the probability as a fraction
    # Probability of Dot winning = (number of favorable outcomes) / (total outcomes)
    # Favorable outcomes = number of die faces that are at least max(x, y)
    # Die has faces 1 through 6, so there are (7 - max_val) favorable outcomes
    numerator = 7 - max_val  # Faces that are at least max_val
    denominator = 6  # Total number of faces on the die

    # Output the simplified fraction
    print(fraction_to_string(numerator, denominator))

if __name__ == "__main__":
    main()