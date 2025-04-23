# 899_C. Dividing the numbers

**ID:** 899_c_dividing_the_numbers_2044
**Difficulty:** 9

## Description

Petya has n integers: 1, 2, 3, ..., n. He wants to split these integers in two non-empty groups in such a way that the absolute difference of sums of integers in each group is as small as possible.

Help Petya to split the integers. Each of n integers should be exactly in one group.

Input

The first line contains a single integer n (2 ≤ n ≤ 60 000) — the number of integers Petya has.

Output

Print the smallest possible absolute difference in the first line.

In the second line print the size of the first group, followed by the integers in that group. You can print these integers in arbitrary order. If there are multiple answers, print any of them.

Examples

Input

4


Output

0
2 1 4


Input

2


Output

1
1 1

Note

In the first example you have to put integers 1 and 4 in the first group, and 2 and 3 in the second. This way the sum in each group is 5, and the absolute difference is 0.

In the second example there are only two integers, and since both groups should be non-empty, you have to put one integer in the first group and one in the second. This way the absolute difference of sums of integers in each group is 1.

## Categories

- constructive algorithms
- graphs
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
1
1 1
```

### Example 2

**Input**:
```
4
```

**Output**:
```
0
2 4 1
```

### Example 3

**Input**:
```
3
```

**Output**:
```
0
1 3
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
