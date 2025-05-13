#!/usr/bin/env python3

from library import read_int_pair, print_yes_no, print_array, sequence_with_xor_property

n, x = read_int_pair()

# Special case: n=2, x=0 is impossible
sequence = sequence_with_xor_property(n, x)
if sequence is None:
    print_yes_no(False)
else:
    print_yes_no(True)
    print_array(sequence)