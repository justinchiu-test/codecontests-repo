# 1227_D1. Optimal Subsequences (Easy Version)

**ID:** 1227_d1_optimal_subsequences_easy_version_16
**Difficulty:** 10

## Description

This is the easier version of the problem. In this version 1 ≤ n, m ≤ 100. You can hack this problem only if you solve and lock both problems.

You are given a sequence of integers a=[a_1,a_2,...,a_n] of length n. Its subsequence is obtained by removing zero or more elements from the sequence a (they do not necessarily go consecutively). For example, for the sequence a=[11,20,11,33,11,20,11]:

  * [11,20,11,33,11,20,11], [11,20,11,33,11,20], [11,11,11,11], [20], [33,20] are subsequences (these are just some of the long list); 
  * [40], [33,33], [33,20,20], [20,20,11,11] are not subsequences. 



Suppose that an additional non-negative integer k (1 ≤ k ≤ n) is given, then the subsequence is called optimal if:

  * it has a length of k and the sum of its elements is the maximum possible among all subsequences of length k; 
  * and among all subsequences of length k that satisfy the previous item, it is lexicographically minimal. 



Recall that the sequence b=[b_1, b_2, ..., b_k] is lexicographically smaller than the sequence c=[c_1, c_2, ..., c_k] if the first element (from the left) in which they differ less in the sequence b than in c. Formally: there exists t (1 ≤ t ≤ k) such that b_1=c_1, b_2=c_2, ..., b_{t-1}=c_{t-1} and at the same time b_t<c_t. For example:

  * [10, 20, 20] lexicographically less than [10, 21, 1], 
  * [7, 99, 99] is lexicographically less than [10, 21, 1], 
  * [10, 21, 0] is lexicographically less than [10, 21, 1]. 



You are given a sequence of a=[a_1,a_2,...,a_n] and m requests, each consisting of two numbers k_j and pos_j (1 ≤ k ≤ n, 1 ≤ pos_j ≤ k_j). For each query, print the value that is in the index pos_j of the optimal subsequence of the given sequence a for k=k_j.

For example, if n=4, a=[10,20,30,20], k_j=2, then the optimal subsequence is [20,30] — it is the minimum lexicographically among all subsequences of length 2 with the maximum total sum of items. Thus, the answer to the request k_j=2, pos_j=1 is the number 20, and the answer to the request k_j=2, pos_j=2 is the number 30.

Input

The first line contains an integer n (1 ≤ n ≤ 100) — the length of the sequence a.

The second line contains elements of the sequence a: integer numbers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9).

The third line contains an integer m (1 ≤ m ≤ 100) — the number of requests.

The following m lines contain pairs of integers k_j and pos_j (1 ≤ k ≤ n, 1 ≤ pos_j ≤ k_j) — the requests.

Output

Print m integers r_1, r_2, ..., r_m (1 ≤ r_j ≤ 10^9) one per line: answers to the requests in the order they appear in the input. The value of r_j should be equal to the value contained in the position pos_j of the optimal subsequence for k=k_j.

Examples

Input


3
10 20 10
6
1 1
2 1
2 2
3 1
3 2
3 3


Output


20
10
20
10
20
10


Input


7
1 2 1 3 1 2 1
9
2 1
2 2
3 1
3 2
3 3
1 1
7 1
7 7
7 4


Output


2
3
2
3
2
3
1
1
3

Note

In the first example, for a=[10,20,10] the optimal subsequences are: 

  * for k=1: [20], 
  * for k=2: [10,20], 
  * for k=3: [10,20,10]. 

## Categories

- data structures
- greedy

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
3
10 20 10
6
1 1
2 1
2 2
3 1
3 2
3 3
```

**Output**:
```
20
10
20
10
20
10
```

### Example 2

**Input**:
```
7
1 2 1 3 1 2 1
9
2 1
2 2
3 1
3 2
3 3
1 1
7 1
7 7
7 4
```

**Output**:
```
2
3
2
3
2
3
1
1
3
```

### Example 3

**Input**:
```
2
1 10
3
2 2
2 1
1 1
```

**Output**:
```
10
1
10
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
