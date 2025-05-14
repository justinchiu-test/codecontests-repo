# Plan for Shared Library

This document outlines the design of the shared `library.py` and a checklist to refactor each problem solution to use it.

## Library Design

1. I/O Utilities
   - `read_int()` → int
   - `read_ints()` → list[int]
   - `read_strs()` → list[str]
   - `read_points(n)` → list[complex] or list[tuple[int,int]]

2. Math Utilities
   - `gcd(a, b)`, `lcm(a, b)`
   - `normalize_rational(num, den)` → tuple[int, int]
   - Alias `Fraction` from `fractions` for exact rational arithmetic

3. Geometry Utilities (using complex for points)
   - `dot(a, b)`, `cross(a, b)`
   - `norm2(a)` (squared length), `dist2(a, b)`
   - `segment_point_dist2(a, b, p)`
   - `segment_segment_dist2(a, b, c, d)`
   - `line_through(a, b)` → (A, B, C) normalized ints for Ax+By+C=0
   - `intersection_with_x_axis(line)` → x as int or None

4. Shape Predicates
   - `is_square(pts: list[complex])` → bool
   - `is_rectangle(pts: list[complex])` → bool

5. Directional Counting
   - `best_cardinal_move(x, y, points)` → (count, (nx, ny))

6. Specialized Algorithms
   - Line grouping / intersection counting
   - Circle-line intersection and angle utilities (for Apollonius problems)
   - Symmetric projection count (for CF 886/889 tasks)

## Refactoring Checklist

- [x] 1046_i_say_hello_9380
- [ ] 1163_c1_power_transmission_easy_edition_2411
- [ ] 1163_c2_power_transmission_hard_edition_12093
- [x] 1271_c_shawarma_tent_643
- [ ] 135_b_rectangle_and_square_9812
- [ ] 136_d_rectangle_and_square_9500
- [ ] 13_b_letter_a_6066
- [ ] 1468_f_full_turn_7213
- [x] 165_a_supercentral_point_7945
- [ ] 183_b_zoo_1910
- [ ] 2_c_commentator_problem_4414
- [ ] 32_e_hideandseek_3373
- [ ] 334_b_eight_point_sets_7016
- [ ] 407_a_triangle_11184
- [ ] 464_b_restore_cube__2130
- [ ] 498_a_crazy_town_4318
- [ ] 499_c_crazy_town_6399
- [ ] 514_b_han_solo_and_lazer_gun_9314
- [ ] 552_d_vanya_and_triangles_5048
- [ ] 598_f_cut_length_4738
- [ ] 617_d_polyline_7236
- [ ] 618_c_constellation_3489
- [ ] 630_o_arrow_1929
- [ ] 659_d_bicycle_race_5157
- [ ] 749_b_parallelogram_is_back_2975
- [ ] 850_a_five_dimensional_points_3812
- [ ] 886_f_symmetric_projections_6728
- [ ] 889_d_symmetric_projections_6832
- [ ] 934_e_a_colourful_prospect_3399
- [ ] 961_d_pair_of_lines_12769
