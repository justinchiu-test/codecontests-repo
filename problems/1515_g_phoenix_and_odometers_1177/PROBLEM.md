# 1515_G. Phoenix and Odometers

**ID:** 1515_g_phoenix_and_odometers_1177
**Difficulty:** 13

## Description

In Fire City, there are n intersections and m one-way roads. The i-th road goes from intersection a_i to b_i and has length l_i miles.

There are q cars that may only drive along those roads. The i-th car starts at intersection v_i and has an odometer that begins at s_i, increments for each mile driven, and resets to 0 whenever it reaches t_i. Phoenix has been tasked to drive cars along some roads (possibly none) and return them to their initial intersection with the odometer showing 0.

For each car, please find if this is possible.

A car may visit the same road or intersection an arbitrary number of times. The odometers don't stop counting the distance after resetting, so odometers may also be reset an arbitrary number of times.

Input

The first line of the input contains two integers n and m (2 ≤ n ≤ 2 ⋅ 10^5; 1 ≤ m ≤ 2 ⋅ 10^5) — the number of intersections and the number of roads, respectively.

Each of the next m lines contain three integers a_i, b_i, and l_i (1 ≤ a_i, b_i ≤ n; a_i ≠ b_i; 1 ≤ l_i ≤ 10^9) — the information about the i-th road. The graph is not necessarily connected. It is guaranteed that between any two intersections, there is at most one road for each direction.

The next line contains an integer q (1 ≤ q ≤ 2 ⋅ 10^5) — the number of cars.

Each of the next q lines contains three integers v_i, s_i, and t_i (1 ≤ v_i ≤ n; 0 ≤ s_i < t_i ≤ 10^9) — the initial intersection of the i-th car, the initial number on the i-th odometer, and the number at which the i-th odometer resets, respectively.

Output

Print q answers. If the i-th car's odometer may be reset to 0 by driving through some roads (possibly none) and returning to its starting intersection v_i, print YES. Otherwise, print NO.

Examples

Input


4 4
1 2 1
2 3 1
3 1 2
1 4 3
3
1 1 3
1 2 4
4 0 1


Output


YES
NO
YES


Input


4 5
1 2 1
2 3 1
3 1 2
1 4 1
4 3 2
2
1 2 4
4 3 5


Output


YES
YES

Note

The illustration for the first example is below:

<image>

In the first query, Phoenix can drive through the following cities: 1 → 2 → 3 → 1 → 2 → 3 → 1. The odometer will have reset 3 times, but it displays 0 at the end.

In the second query, we can show that there is no way to reset the odometer to 0 and return to intersection 1.

In the third query, the odometer already displays 0, so there is no need to drive through any roads.

Below is the illustration for the second example:

<image>

## Categories

- dfs and similar
- graphs
- math
- number theory

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
4 5
1 2 1
2 3 1
3 1 2
1 4 1
4 3 2
2
1 2 4
4 3 5
```

**Output**:
```
YES
YES
```

### Example 2

**Input**:
```
4 4
1 2 1
2 3 1
3 1 2
1 4 3
3
1 1 3
1 2 4
4 0 1
```

**Output**:
```
YES
NO
YES
```

### Example 3

**Input**:
```
2 1
2 1 1
1
2 1 2
```

**Output**:
```
NO
```


## Testing

Run the solution with:

```bash
./run.sh
```

Or test with a specific input file:

```bash
uv run main.py < tests/input_1.txt
```
