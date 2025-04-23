# 687_A. NP-Hard Problem

**ID:** 687_a_nphard_problem_261
**Difficulty:** very hard

## Description

Recently, Pari and Arya did some research about NP-Hard problems and they found the minimum vertex cover problem very interesting.

Suppose the graph G is given. Subset A of its vertices is called a vertex cover of this graph, if for each edge uv there is at least one endpoint of it in this set, i.e. <image> or <image> (or both).

Pari and Arya have won a great undirected graph as an award in a team contest. Now they have to split it in two parts, but both of them want their parts of the graph to be a vertex cover.

They have agreed to give you their graph and you need to find two disjoint subsets of its vertices A and B, such that both A and B are vertex cover or claim it's impossible. Each vertex should be given to no more than one of the friends (or you can even keep it for yourself).

Input

The first line of the input contains two integers n and m (2 ≤ n ≤ 100 000, 1 ≤ m ≤ 100 000) — the number of vertices and the number of edges in the prize graph, respectively.

Each of the next m lines contains a pair of integers ui and vi (1 ≤ ui, vi ≤ n), denoting an undirected edge between ui and vi. It's guaranteed the graph won't contain any self-loops or multiple edges.

Output

If it's impossible to split the graph between Pari and Arya as they expect, print "-1" (without quotes).

If there are two disjoint sets of vertices, such that both sets are vertex cover, print their descriptions. Each description must contain two lines. The first line contains a single integer k denoting the number of vertices in that vertex cover, and the second line contains k integers — the indices of vertices. Note that because of m ≥ 1, vertex cover cannot be empty.

Examples

Input

4 2
1 2
2 3


Output

1
2
2
1 3


Input

3 3
1 2
2 3
1 3


Output

-1

Note

In the first sample, you can give the vertex number 2 to Arya and vertices numbered 1 and 3 to Pari and keep vertex number 4 for yourself (or give it someone, if you wish).

In the second sample, there is no way to satisfy both Pari and Arya.

## Categories

- dfs and similar
- graphs

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
4 2
1 2
2 3
```

**Output**:
```
3
1 3 4
1
2
```

### Example 2

**Input**:
```
3 3
1 2
2 3
1 3
```

**Output**:
```
-1
```

### Example 3

**Input**:
```
10 16
6 10
5 2
6 4
6 8
5 3
5 4
6 2
5 9
5 7
5 1
6 9
5 8
5 10
6 1
6 7
6 3
```

**Output**:
```
8
1 2 3 4 7 8 9 10
2
5 6
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
