# 263_D. Cycle in Graph

**ID:** 263_d_cycle_in_graph_660
**Difficulty:** 10

## Description

You've got a undirected graph G, consisting of n nodes. We will consider the nodes of the graph indexed by integers from 1 to n. We know that each node of graph G is connected by edges with at least k other nodes of this graph. Your task is to find in the given graph a simple cycle of length of at least k + 1.

A simple cycle of length d (d > 1) in graph G is a sequence of distinct graph nodes v1, v2, ..., vd such, that nodes v1 and vd are connected by an edge of the graph, also for any integer i (1 ≤ i < d) nodes vi and vi + 1 are connected by an edge of the graph.

Input

The first line contains three integers n, m, k (3 ≤ n, m ≤ 105; 2 ≤ k ≤ n - 1) — the number of the nodes of the graph, the number of the graph's edges and the lower limit on the degree of the graph node. Next m lines contain pairs of integers. The i-th line contains integers ai, bi (1 ≤ ai, bi ≤ n; ai ≠ bi) — the indexes of the graph nodes that are connected by the i-th edge.

It is guaranteed that the given graph doesn't contain any multiple edges or self-loops. It is guaranteed that each node of the graph is connected by the edges with at least k other nodes of the graph.

Output

In the first line print integer r (r ≥ k + 1) — the length of the found cycle. In the next line print r distinct integers v1, v2, ..., vr (1 ≤ vi ≤ n) — the found simple cycle.

It is guaranteed that the answer exists. If there are multiple correct answers, you are allowed to print any of them.

Examples

Input

3 3 2
1 2
2 3
3 1


Output

3
1 2 3

Input

4 6 3
4 3
1 2
1 3
1 4
2 3
2 4


Output

4
3 4 1 2

## Categories

- dfs and similar
- graphs

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
4 6 3
4 3
1 2
1 3
1 4
2 3
2 4
```

**Output**:
```
4
1 2 3 4
```

### Example 2

**Input**:
```
3 3 2
1 2
2 3
3 1
```

**Output**:
```
3
1 2 3
```

### Example 3

**Input**:
```
30 70 4
22 1
1 25
27 5
25 10
10 2
29 4
29 26
28 18
15 18
25 11
11 10
11 28
4 11
4 26
26 7
26 18
18 21
14 17
17 30
30 9
30 6
30 27
27 22
22 15
22 8
8 4
8 17
17 16
16 19
16 12
12 23
23 20
20 1
1 23
23 15
15 24
24 28
28 21
21 9
21 27
29 13
13 5
20 19
20 5
5 2
2 29
25 2
3 16
3 8
3 24
3 12
12 13
13 24
9 6
9 7
7 19
7 10
6 14
6 19
14 8
14 28
8 19
13 22
19 26
10 17
18 4
20 12
6 2
11 7
13 28
```

**Output**:
```
18
13 29 4 11 25 10 2 6 30 17 14 8 3 16 19 20 23 12
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
