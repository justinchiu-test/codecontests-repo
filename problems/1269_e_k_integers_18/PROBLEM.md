# 1269_E. K Integers

**ID:** 1269_e_k_integers_18
**Difficulty:** 11

## Description

You are given a permutation p_1, p_2, …, p_n.

In one move you can swap two adjacent values.

You want to perform a minimum number of moves, such that in the end there will exist a subsegment 1,2,…, k, in other words in the end there should be an integer i, 1 ≤ i ≤ n-k+1 such that p_i = 1, p_{i+1} = 2, …, p_{i+k-1}=k.

Let f(k) be the minimum number of moves that you need to make a subsegment with values 1,2,…,k appear in the permutation.

You need to find f(1), f(2), …, f(n).

Input

The first line of input contains one integer n (1 ≤ n ≤ 200 000): the number of elements in the permutation.

The next line of input contains n integers p_1, p_2, …, p_n: given permutation (1 ≤ p_i ≤ n).

Output

Print n integers, the minimum number of moves that you need to make a subsegment with values 1,2,…,k appear in the permutation, for k=1, 2, …, n.

Examples

Input


5
5 4 3 2 1


Output


0 1 3 6 10 


Input


3
1 2 3


Output


0 0 0 

## Categories

- binary search
- data structures

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
3
1 2 3
```

**Output**:
```
0 0 0
```

### Example 2

**Input**:
```
5
5 4 3 2 1
```

**Output**:
```
0 1 3 6 10
```

### Example 3

**Input**:
```
1
1
```

**Output**:
```
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
