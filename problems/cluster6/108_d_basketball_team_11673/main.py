#!/usr/bin/env python3

from library import read_ints, combination

# Read input
n, m, h = read_ints()  # Number of players needed, number of departments, Herr Wafa's department
students_per_dept = read_ints()  # Number of basketball players in each department

# Calculate total students
total_students = sum(students_per_dept)

# Check if there are enough students to form a team
if total_students < n:
    print("-1")
    exit()

# Herr Wafa's department (0-indexed)
h_dept = h - 1

# Herr Wafa is already on the team, so we need to subtract him from his department's count
students_per_dept[h_dept] -= 1

# Players needed to be selected (excluding Herr Wafa)
players_needed = n - 1

# Total students excluding Herr Wafa
total_students_excluding_wafa = total_students - 1

# Students in other departments
students_in_other_depts = total_students_excluding_wafa - students_per_dept[h_dept]

# Calculate probability of having no teammate from Herr Wafa's department
# This means all players_needed must be chosen from other departments
if students_in_other_depts < players_needed:
    # Not enough students in other departments, so Herr Wafa must have teammates from his department
    probability_at_least_one = 1
else:
    # Ways to choose players_needed from students_in_other_depts
    favorable_outcomes = combination(students_in_other_depts, players_needed)
    
    # Total ways to choose players_needed from total_students_excluding_wafa
    total_outcomes = combination(total_students_excluding_wafa, players_needed)
    
    # Probability of having no teammate from Herr Wafa's department
    probability_no_teammate = favorable_outcomes / total_outcomes
    
    # Probability of having at least one teammate from Herr Wafa's department
    probability_at_least_one = 1 - probability_no_teammate

# Print the result, formatted to match expected output
if probability_at_least_one == 1:
    print("1")
else:
    print(f"{probability_at_least_one:.10f}")