# 1497_D. Genius

**ID:** 1497_d_genius_132
**Difficulty:** 10

## Description

Please note the non-standard memory limit.

There are n problems numbered with integers from 1 to n. i-th problem has the complexity c_i = 2^i, tag tag_i and score s_i.

After solving the problem i it's allowed to solve problem j if and only if IQ < |c_i - c_j| and tag_i ≠ tag_j. After solving it your IQ changes and becomes IQ = |c_i - c_j| and you gain |s_i - s_j| points.

Any problem can be the first. You can solve problems in any order and as many times as you want.

Initially your IQ = 0. Find the maximum number of points that can be earned.

Input

The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case contains an integer n (1 ≤ n ≤ 5000) — the number of problems.

The second line of each test case contains n integers tag_1, tag_2, …, tag_n (1 ≤ tag_i ≤ n) — tags of the problems.

The third line of each test case contains n integers s_1, s_2, …, s_n (1 ≤ s_i ≤ 10^9) — scores of the problems.

It's guaranteed that sum of n over all test cases does not exceed 5000.

Output

For each test case print a single integer — the maximum number of points that can be earned.

Example

Input


5
4
1 2 3 4
5 10 15 20
4
1 2 1 2
5 10 15 20
4
2 2 4 1
2 8 19 1
2
1 1
6 9
1
1
666


Output


35
30
42
0
0

Note

In the first test case optimal sequence of solving problems is as follows:

  1. 1 → 2, after that total score is 5 and IQ = 2
  2. 2 → 3, after that total score is 10 and IQ = 4
  3. 3 → 1, after that total score is 20 and IQ = 6
  4. 1 → 4, after that total score is 35 and IQ = 14



In the second test case optimal sequence of solving problems is as follows:

  1. 1 → 2, after that total score is 5 and IQ = 2
  2. 2 → 3, after that total score is 10 and IQ = 4
  3. 3 → 4, after that total score is 15 and IQ = 8
  4. 4 → 1, after that total score is 35 and IQ = 14



In the third test case optimal sequence of solving problems is as follows:

  1. 1 → 3, after that total score is 17 and IQ = 6
  2. 3 → 4, after that total score is 35 and IQ = 8
  3. 4 → 2, after that total score is 42 and IQ = 12

## Categories

- bitmasks
- dp
- graphs
- number theory

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
5
4
1 2 3 4
5 10 15 20
4
1 2 1 2
5 10 15 20
4
2 2 4 1
2 8 19 1
2
1 1
6 9
1
1
666
```

**Output**:
```
35
30
42
0
0
```

### Example 2

**Input**:
```
5
4
1 2 3 4
5 10 15 20
4
1 2 1 2
5 10 15 20
4
2 2 4 1
2 8 19 2
2
1 1
6 9
1
1
666
```

**Output**:
```
35
30
40
0
0
```

### Example 3

**Input**:
```
5
4
1 2 3 4
5 10 15 20
4
1 2 2 2
5 10 15 20
4
2 2 4 1
2 8 19 2
2
1 1
6 9
1
1
666
```

**Output**:
```
35
25
40
0
0
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
