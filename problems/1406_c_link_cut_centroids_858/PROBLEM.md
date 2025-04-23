# 1406_C. Link Cut Centroids

**ID:** 1406_c_link_cut_centroids_858
**Difficulty:** 9

## Description

Fishing Prince loves trees, and he especially loves trees with only one centroid. The tree is a connected graph without cycles.

A vertex is a centroid of a tree only when you cut this vertex (remove it and remove all edges from this vertex), the size of the largest connected component of the remaining graph is the smallest possible.

For example, the centroid of the following tree is 2, because when you cut it, the size of the largest connected component of the remaining graph is 2 and it can't be smaller.

<image>

However, in some trees, there might be more than one centroid, for example:

<image>

Both vertex 1 and vertex 2 are centroids because the size of the largest connected component is 3 after cutting each of them.

Now Fishing Prince has a tree. He should cut one edge of the tree (it means to remove the edge). After that, he should add one edge. The resulting graph after these two operations should be a tree. He can add the edge that he cut.

He wants the centroid of the resulting tree to be unique. Help him and find any possible way to make the operations. It can be proved, that at least one such way always exists.

Input

The input consists of multiple test cases. The first line contains an integer t (1≤ t≤ 10^4) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n (3≤ n≤ 10^5) — the number of vertices.

Each of the next n-1 lines contains two integers x, y (1≤ x,y≤ n). It means, that there exists an edge connecting vertices x and y.

It's guaranteed that the given graph is a tree.

It's guaranteed that the sum of n for all test cases does not exceed 10^5.

Output

For each test case, print two lines.

In the first line print two integers x_1, y_1 (1 ≤ x_1, y_1 ≤ n), which means you cut the edge between vertices x_1 and y_1. There should exist edge connecting vertices x_1 and y_1.

In the second line print two integers x_2, y_2 (1 ≤ x_2, y_2 ≤ n), which means you add the edge between vertices x_2 and y_2.

The graph after these two operations should be a tree.

If there are multiple solutions you can print any.

Example

Input


2
5
1 2
1 3
2 4
2 5
6
1 2
1 3
1 4
2 5
2 6


Output


1 2
1 2
1 3
2 3

Note

Note that you can add the same edge that you cut.

In the first test case, after cutting and adding the same edge, the vertex 2 is still the only centroid.

In the second test case, the vertex 2 becomes the only centroid after cutting the edge between vertices 1 and 3 and adding the edge between vertices 2 and 3.

## Categories

- constructive algorithms
- dfs and similar
- graphs
- trees

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
2
5
1 2
1 3
2 4
2 5
6
1 2
1 3
1 4
2 5
2 6
```

**Output**:
```
1 2
1 2
2 5
1 5
```

### Example 2

**Input**:
```
15
4
1 2
2 3
3 4
4
1 2
2 4
3 4
4
1 2
1 3
1 4
4
1 3
2 3
4 3
4
1 4
3 4
2 3
4
4 1
3 2
2 1
5
1 2
2 3
3 4
4 5
5
1 2
2 3
4 1
5 1
5
1 2
3 1
4 1
1 5
6
1 2
2 3
3 4
4 5
5 6
6
1 3
2 3
3 4
4 5
4 6
3
1 2
1 3
3
2 1
2 3
3
3 1
3 2
4
1 2
2 3
2 4
```

**Output**:
```
2 1
3 1
2 1
4 1
1 2
1 2
1 3
1 3
3 2
4 2
1 4
2 4
1 2
1 2
1 2
1 2
1 2
1 2
3 2
4 2
3 1
4 1
1 2
1 2
1 2
1 2
1 3
1 3
1 2
1 2
```

### Example 3

**Input**:
```
2
5
1 2
1 3
2 4
2 5
6
1 2
1 3
1 4
2 5
2 6
```

**Output**:
```
1 2
1 2
2 5
1 5
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
