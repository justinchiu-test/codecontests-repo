# 463_D. Gargari and Permutations

**ID:** 463_d_gargari_and_permutations_2442
**Difficulty:** 10

## Description

Gargari got bored to play with the bishops and now, after solving the problem about them, he is trying to do math homework. In a math book he have found k permutations. Each of them consists of numbers 1, 2, ..., n in some order. Now he should find the length of the longest common subsequence of these permutations. Can you help Gargari?

You can read about longest common subsequence there: https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

Input

The first line contains two integers n and k (1 ≤ n ≤ 1000; 2 ≤ k ≤ 5). Each of the next k lines contains integers 1, 2, ..., n in some order — description of the current permutation.

Output

Print the length of the longest common subsequence.

Examples

Input

4 3
1 4 2 3
4 1 2 3
1 2 4 3


Output

3

Note

The answer for the first test sample is subsequence [1, 2, 3].

## Categories

- dfs and similar
- dp
- graphs
- implementation

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
4 3
1 4 2 3
4 1 2 3
1 2 4 3
```

**Output**:
```
3
```

### Example 2

**Input**:
```
6 3
2 5 1 4 6 3
5 1 4 6 2 3
5 4 2 6 3 1
```

**Output**:
```
4
```

### Example 3

**Input**:
```
6 3
2 5 1 4 6 3
5 1 4 3 2 6
5 4 2 6 3 1
```

**Output**:
```
3
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
