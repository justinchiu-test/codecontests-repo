# 1062_D. Fun with Integers

**ID:** 1062_d_fun_with_integers_633
**Difficulty:** 10

## Description

You are given a positive integer n greater or equal to 2. For every pair of integers a and b (2 ≤ |a|, |b| ≤ n), you can transform a into b if and only if there exists an integer x such that 1 < |x| and (a ⋅ x = b or b ⋅ x = a), where |x| denotes the absolute value of x.

After such a transformation, your score increases by |x| points and you are not allowed to transform a into b nor b into a anymore.

Initially, you have a score of 0. You can start at any integer and transform it as many times as you like. What is the maximum score you can achieve?

Input

A single line contains a single integer n (2 ≤ n ≤ 100 000) — the given integer described above.

Output

Print an only integer — the maximum score that can be achieved with the transformations. If it is not possible to perform even a single transformation for all possible starting integers, print 0.

Examples

Input

4


Output

8

Input

6


Output

28

Input

2


Output

0

Note

In the first example, the transformations are 2 → 4 → (-2) → (-4) → 2.

In the third example, it is impossible to perform even a single transformation.

## Categories

- dfs and similar
- graphs
- implementation
- math

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
2
```

**Output**:
```
0
```

### Example 2

**Input**:
```
4
```

**Output**:
```
8
```

### Example 3

**Input**:
```
6
```

**Output**:
```
28
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
