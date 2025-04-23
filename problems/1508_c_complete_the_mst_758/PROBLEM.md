# 1508_C. Complete the MST

**ID:** 1508_c_complete_the_mst_758
**Difficulty:** 9

## Description

As a teacher, Riko Hakozaki often needs to help her students with problems from various subjects. Today, she is asked a programming task which goes as follows.

You are given an undirected complete graph with n nodes, where some edges are pre-assigned with a positive weight while the rest aren't. You need to assign all unassigned edges with non-negative weights so that in the resulting fully-assigned complete graph the [XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) sum of all weights would be equal to 0.

Define the ugliness of a fully-assigned complete graph the weight of its [minimum spanning tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree), where the weight of a spanning tree equals the sum of weights of its edges. You need to assign the weights so that the ugliness of the resulting graph is as small as possible.

As a reminder, an undirected complete graph with n nodes contains all edges (u, v) with 1 ≤ u < v ≤ n; such a graph has (n(n-1))/(2) edges.

She is not sure how to solve this problem, so she asks you to solve it for her.

Input

The first line contains two integers n and m (2 ≤ n ≤ 2 ⋅ 10^5, 0 ≤ m ≤ min(2 ⋅ 10^5, (n(n-1))/(2) - 1)) — the number of nodes and the number of pre-assigned edges. The inputs are given so that there is at least one unassigned edge.

The i-th of the following m lines contains three integers u_i, v_i, and w_i (1 ≤ u_i, v_i ≤ n, u ≠ v, 1 ≤ w_i < 2^{30}), representing the edge from u_i to v_i has been pre-assigned with the weight w_i. No edge appears in the input more than once.

Output

Print on one line one integer — the minimum ugliness among all weight assignments with XOR sum equal to 0.

Examples

Input


4 4
2 1 14
1 4 14
3 2 15
4 3 8


Output


15


Input


6 6
3 6 4
2 4 1
4 5 7
3 4 10
3 5 1
5 2 15


Output


0


Input


5 6
2 3 11
5 3 7
1 4 10
2 4 14
4 3 8
2 5 6


Output


6

Note

The following image showcases the first test case. The black weights are pre-assigned from the statement, the red weights are assigned by us, and the minimum spanning tree is denoted by the blue edges.

<image>

## Categories

- bitmasks
- brute force
- data structures
- dfs and similar
- dsu
- graphs
- greedy
- trees

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
4 4
2 1 14
1 4 14
3 2 15
4 3 8
```

**Output**:
```
15
```

### Example 2

**Input**:
```
5 6
2 3 11
5 3 7
1 4 10
2 4 14
4 3 8
2 5 6
```

**Output**:
```
6
```

### Example 3

**Input**:
```
6 6
3 6 4
2 4 1
4 5 7
3 4 10
3 5 1
5 2 15
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
