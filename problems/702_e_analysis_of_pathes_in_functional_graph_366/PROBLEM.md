# 702_E. Analysis of Pathes in Functional Graph

**ID:** 702_e_analysis_of_pathes_in_functional_graph_366
**Difficulty:** 11

## Description

You are given a functional graph. It is a directed graph, in which from each vertex goes exactly one arc. The vertices are numerated from 0 to n - 1.

Graph is given as the array f0, f1, ..., fn - 1, where fi — the number of vertex to which goes the only arc from the vertex i. Besides you are given array with weights of the arcs w0, w1, ..., wn - 1, where wi — the arc weight from i to fi.

<image> The graph from the first sample test.

Also you are given the integer k (the length of the path) and you need to find for each vertex two numbers si and mi, where:

  * si — the sum of the weights of all arcs of the path with length equals to k which starts from the vertex i;
  * mi — the minimal weight from all arcs on the path with length k which starts from the vertex i.



The length of the path is the number of arcs on this path.

Input

The first line contains two integers n, k (1 ≤ n ≤ 105, 1 ≤ k ≤ 1010). The second line contains the sequence f0, f1, ..., fn - 1 (0 ≤ fi < n) and the third — the sequence w0, w1, ..., wn - 1 (0 ≤ wi ≤ 108).

Output

Print n lines, the pair of integers si, mi in each line.

Examples

Input

7 3
1 2 3 4 3 2 6
6 3 1 4 2 2 3


Output

10 1
8 1
7 1
10 2
8 2
7 1
9 3


Input

4 4
0 1 2 3
0 1 2 3


Output

0 0
4 1
8 2
12 3


Input

5 3
1 2 3 4 0
4 1 2 14 3


Output

7 1
17 1
19 2
21 3
8 1

## Categories

- data structures
- graphs

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
5 3
1 2 3 4 0
4 1 2 14 3
```

**Output**:
```
7                                                                1
                                                              17                                                                1
                                                              19                                                                2
                                                              21                                                                3
                                                               8                                                                1
```

### Example 2

**Input**:
```
7 3
1 2 3 4 3 2 6
6 3 1 4 2 2 3
```

**Output**:
```
10                                                                1
                                                               8                                                                1
                                                               7                                                                1
                                                              10                                                                2
                                                               8                                                                2
                                                               7                                                                1
                                                               9                                                                3
```

### Example 3

**Input**:
```
4 4
0 1 2 3
0 1 2 3
```

**Output**:
```
0                                                                0
                                                               4                                                                1
                                                               8                                                                2
                                                              12                                                                3
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
