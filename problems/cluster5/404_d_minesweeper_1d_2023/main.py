#!/usr/bin/env python3

from library import read_str, mod_add, MOD_10_9_PLUS_7

def minesweeper_1d():
    """
    Solution for the Minesweeper 1D problem.

    We use a dynamic programming approach with state transitions based on the current
    cell value and previous state values.

    States:
    - a: Cell is a mine with a mine to the left
    - b: Cell is a mine with no mine to the left
    - c: Cell is not a mine with no mine to the left
    - d: Cell is not a mine with a mine to the left
    """
    # Read input
    field = read_str()
    n = len(field)

    # Initialize states:
    # Start with a=1 because we can place a mine at the first position
    # without considering anything to the left
    a, b, c, d = 1, 0, 0, 0

    # Process each cell
    for i in range(n):
        if field[i] == '*':  # Cell is definitely a mine
            # Can only be state b (mine with no mine to left) or state a (mine with mine to left)
            new_a = 0  # Can't have mine-mine-mine pattern at start
            new_b = mod_add(a, mod_add(b, d, MOD_10_9_PLUS_7), MOD_10_9_PLUS_7)  # Mine after anything except c
            new_c = 0  # Can't be non-mine
            new_d = 0  # Can't be non-mine

        elif field[i] == '?':  # Cell can be either mine or non-mine
            # Can be any state depending on previous cell
            new_a = mod_add(a, mod_add(b, c, MOD_10_9_PLUS_7), MOD_10_9_PLUS_7)  # Mine after anything
            new_b = mod_add(a, mod_add(b, d, MOD_10_9_PLUS_7), MOD_10_9_PLUS_7)  # Mine after anything except c
            new_c = 0  # Reset for next iteration
            new_d = 0  # Reset for next iteration

        elif field[i] == '0':  # Cell has no adjacent mines
            # Must be state c (non-mine with no mine to left)
            new_a = 0  # Can't be mine
            new_b = 0  # Can't be mine
            new_c = mod_add(a, c, MOD_10_9_PLUS_7)  # No mine after a mine or no mine
            new_d = 0  # Can't have mine to left

        elif field[i] == '1':  # Cell has exactly one adjacent mine
            # Must be state d (non-mine with mine to left) or state b (mine with no mine to left)
            new_a = 0  # Can't have two mines adjacent
            new_b = 0  # Can't be mine with no mine to left
            new_c = b  # Non-mine after mine (b→c gives 1 adjacent mine)
            new_d = mod_add(a, c, MOD_10_9_PLUS_7)  # Non-mine after mine or after non-mine with mine before

        else:  # field[i] == '2', Cell has two adjacent mines
            # Must be state d (non-mine with mine to left)
            new_a = 0  # Can't be mine
            new_b = 0  # Can't be mine
            new_c = 0  # Can't be non-mine with no mine to left
            new_d = mod_add(b, d, MOD_10_9_PLUS_7)  # Non-mine with mine to left

        # Update states for next iteration
        a, b, c, d = new_a, new_b, new_c, new_d

    # Final count is the sum of valid end states (a, b, c)
    # We don't include d because it would require a mine after the last cell
    return mod_add(a, mod_add(b, c, MOD_10_9_PLUS_7), MOD_10_9_PLUS_7)

print(minesweeper_1d())
