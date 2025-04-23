# 825_E. Minimal Labels

**ID:** 825_e_minimal_labels_684
**Difficulty:** 11

## Description

You are given a directed acyclic graph with n vertices and m edges. There are no self-loops or multiple edges between any pair of vertices. Graph can be disconnected.

You should assign labels to all vertices in such a way that:

  * Labels form a valid permutation of length n — an integer sequence such that each integer from 1 to n appears exactly once in it.
  * If there exists an edge from vertex v to vertex u then labelv should be smaller than labelu.
  * Permutation should be lexicographically smallest among all suitable.



Find such sequence of labels to satisfy all the conditions.

Input

The first line contains two integer numbers n, m (2 ≤ n ≤ 105, 1 ≤ m ≤ 105).

Next m lines contain two integer numbers v and u (1 ≤ v, u ≤ n, v ≠ u) — edges of the graph. Edges are directed, graph doesn't contain loops or multiple edges.

Output

Print n numbers — lexicographically smallest correct permutation of labels of vertices.

Examples

Input

3 3
1 2
1 3
3 2


Output

1 3 2


Input

4 5
3 1
4 1
2 3
3 4
2 4


Output

4 1 2 3


Input

5 4
3 1
2 1
2 3
4 5


Output

3 1 2 4 5

## Categories

- data structures
- dfs and similar
- graphs
- greedy

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
3 3
1 2
1 3
3 2
```

**Output**:
```
1 3 2
```

### Example 2

**Input**:
```
4 5
3 1
4 1
2 3
3 4
2 4
```

**Output**:
```
4 1 2 3
```

### Example 3

**Input**:
```
5 4
3 1
2 1
2 3
4 5
```

**Output**:
```
3 1 2 4 5
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
