# 1332_F. Independent Set

**ID:** 1332_f_independent_set_12309
**Difficulty:** 12

## Description

Eric is the teacher of graph theory class. Today, Eric teaches independent set and edge-induced subgraph.

Given a graph G=(V,E), an independent set is a subset of vertices V' ⊂ V such that for every pair u,v ∈ V', (u,v) not ∈ E (i.e. no edge in E connects two vertices from V').

An edge-induced subgraph consists of a subset of edges E' ⊂ E and all the vertices in the original graph that are incident on at least one edge in the subgraph.

Given E' ⊂ E, denote G[E'] the edge-induced subgraph such that E' is the edge set of the subgraph. Here is an illustration of those definitions:

<image>

In order to help his students get familiar with those definitions, he leaves the following problem as an exercise:

Given a tree G=(V,E), calculate the sum of w(H) over all except null edge-induced subgraph H of G, where w(H) is the number of independent sets in H. Formally, calculate ∑ _{∅ not= E' ⊂ E} w(G[E']).

Show Eric that you are smarter than his students by providing the correct answer as quickly as possible. Note that the answer might be large, you should output the answer modulo 998,244,353.

Input

The first line contains a single integer n (2 ≤ n ≤ 3 ⋅ 10^5), representing the number of vertices of the graph G.

Each of the following n-1 lines contains two integers u and v (1 ≤ u,v ≤ n, u not= v), describing edges of the given tree.

It is guaranteed that the given edges form a tree.

Output

Output one integer, representing the desired value modulo 998,244,353.

Examples

Input


2
2 1


Output


3


Input


3
1 2
3 2


Output


11

Note

For the second example, all independent sets are listed below.

<image>

## Categories

- dfs and similar
- dp
- trees

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
2
2 1
```

**Output**:
```
3
```

### Example 2

**Input**:
```
3
1 2
3 2
```

**Output**:
```
11
```

### Example 3

**Input**:
```
10
2 8
5 10
3 4
1 6
3 9
1 7
4 8
10 8
1 8
```

**Output**:
```
24497
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
