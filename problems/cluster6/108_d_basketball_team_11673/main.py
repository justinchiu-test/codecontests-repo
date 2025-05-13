#!/usr/bin/env python3

from library import read_ints, print_float
import sys

n, m, h = read_ints()
departments = read_ints()

total_players = sum(departments)

# Check if there are enough players
if total_players < n:
    print("-1")
    sys.exit()

# Calculate players not in Herr Wafa's department
# Subtract 1 to exclude Herr Wafa himself
players_in_wafa_dept = departments[h-1] - 1
players_other_depts = total_players - departments[h-1]
total_players_excluding_wafa = total_players - 1

# Probability of having no teammates from Wafa's department
# = probability that all (n-1) selected teammates are from other departments
probability_no_teammate_from_dept = 1.0
for i in range(n-1):
    probability_no_teammate_from_dept *= (players_other_depts - i) / (total_players_excluding_wafa - i)

# The probability of having at least one teammate from Wafa's department
# is 1 minus the probability of having none
probability_at_least_one = 1.0 - probability_no_teammate_from_dept

# Special case for probability = 1
if abs(probability_at_least_one - 1.0) < 1e-9:
    print("1")
else:
    print_float(probability_at_least_one, 10)