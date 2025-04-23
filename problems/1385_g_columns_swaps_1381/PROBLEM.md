# 1385_G. Columns Swaps

**ID:** 1385_g_columns_swaps_1381
**Difficulty:** 13

## Description

You are given a table a of size 2 × n (i.e. two rows and n columns) consisting of integers from 1 to n.

In one move, you can choose some column j (1 ≤ j ≤ n) and swap values a_{1, j} and a_{2, j} in it. Each column can be chosen no more than once.

Your task is to find the minimum number of moves required to obtain permutations of size n in both first and second rows of the table or determine if it is impossible to do that.

You have to answer t independent test cases.

Recall that the permutation of size n is such an array of size n that contains each integer from 1 to n exactly once (the order of elements doesn't matter).

Input

The first line of the input contains one integer t (1 ≤ t ≤ 2 ⋅ 10^4) — the number of test cases. Then t test cases follow.

The first line of the test case contains one integer n (1 ≤ n ≤ 2 ⋅ 10^5) — the number of columns in the table. The second line of the test case contains n integers a_{1, 1}, a_{1, 2}, ..., a_{1, n} (1 ≤ a_{1, i} ≤ n), where a_{1, i} is the i-th element of the first row of the table. The third line of the test case contains n integers a_{2, 1}, a_{2, 2}, ..., a_{2, n} (1 ≤ a_{2, i} ≤ n), where a_{2, i} is the i-th element of the second row of the table.

It is guaranteed that the sum of n does not exceed 2 ⋅ 10^5 (∑ n ≤ 2 ⋅ 10^5).

Output

For each test case print the answer: -1 if it is impossible to obtain permutation of size n in both first and the second rows of the table, or one integer k in the first line, where k is the minimum number of moves required to obtain permutations in both rows, and k distinct integers pos_1, pos_2, ..., pos_k in the second line (1 ≤ pos_i ≤ n) in any order — indices of columns in which you need to swap values to obtain permutations in both rows. If there are several answers, you can print any.

Example

Input


6
4
1 2 3 4
2 3 1 4
5
5 3 5 1 4
1 2 3 2 4
3
1 2 1
3 3 2
4
1 2 2 1
3 4 3 4
4
4 3 1 4
3 2 2 1
3
1 1 2
3 2 2


Output


0

2
2 3
1
1
2
3 4
2
3 4
-1

## Categories

- 2-sat
- dfs and similar
- dsu
- graphs
- implementation

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
6
4
1 2 3 4
2 3 1 4
5
5 3 5 1 4
1 2 3 2 4
3
1 2 1
3 3 2
4
1 2 2 1
3 4 3 4
4
4 3 1 4
3 2 2 1
3
1 1 2
3 2 2
```

**Output**:
```
0

2
1 4
1
1
2
1 2
2
1 2
-1
```

### Example 2

**Input**:
```
6
4
1 2 3 4
2 3 1 4
5
5 3 5 1 4
1 2 3 2 4
3
1 2 1
3 3 2
4
1 2 2 1
3 4 3 4
4
4 3 1 4
3 2 2 2
3
1 1 2
3 2 2
```

**Output**:
```
0

2
1 4
1
1
2
1 2
-1
-1
```

### Example 3

**Input**:
```
6
4
1 2 3 4
2 3 1 4
5
5 3 5 1 4
1 2 3 2 4
3
1 2 1
3 3 2
4
1 2 3 1
3 4 3 4
4
4 3 1 4
3 2 2 2
3
1 1 2
3 2 2
```

**Output**:
```
0

2
1 4
1
1
-1
-1
-1
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
