# 1244_D. Paint the Tree

**ID:** 1244_d_paint_the_tree_1479
**Difficulty:** 10

## Description

You are given a tree consisting of n vertices. A tree is an undirected connected acyclic graph.

<image> Example of a tree.

You have to paint each vertex into one of three colors. For each vertex, you know the cost of painting it in every color.

You have to paint the vertices so that any path consisting of exactly three distinct vertices does not contain any vertices with equal colors. In other words, let's consider all triples (x, y, z) such that x ≠ y, y ≠ z, x ≠ z, x is connected by an edge with y, and y is connected by an edge with z. The colours of x, y and z should be pairwise distinct. Let's call a painting which meets this condition good.

You have to calculate the minimum cost of a good painting and find one of the optimal paintings. If there is no good painting, report about it.

Input

The first line contains one integer n (3 ≤ n ≤ 100 000) — the number of vertices.

The second line contains a sequence of integers c_{1, 1}, c_{1, 2}, ..., c_{1, n} (1 ≤ c_{1, i} ≤ 10^{9}), where c_{1, i} is the cost of painting the i-th vertex into the first color.

The third line contains a sequence of integers c_{2, 1}, c_{2, 2}, ..., c_{2, n} (1 ≤ c_{2, i} ≤ 10^{9}), where c_{2, i} is the cost of painting the i-th vertex into the second color.

The fourth line contains a sequence of integers c_{3, 1}, c_{3, 2}, ..., c_{3, n} (1 ≤ c_{3, i} ≤ 10^{9}), where c_{3, i} is the cost of painting the i-th vertex into the third color.

Then (n - 1) lines follow, each containing two integers u_j and v_j (1 ≤ u_j, v_j ≤ n, u_j ≠ v_j) — the numbers of vertices connected by the j-th undirected edge. It is guaranteed that these edges denote a tree.

Output

If there is no good painting, print -1.

Otherwise, print the minimum cost of a good painting in the first line. In the second line print n integers b_1, b_2, ..., b_n (1 ≤ b_i ≤ 3), where the i-th integer should denote the color of the i-th vertex. If there are multiple good paintings with minimum cost, print any of them.

Examples

Input


3
3 2 3
4 3 2
3 1 3
1 2
2 3


Output


6
1 3 2


Input


5
3 4 2 1 2
4 2 1 5 4
5 3 2 1 1
1 2
3 2
4 3
5 3


Output


-1


Input


5
3 4 2 1 2
4 2 1 5 4
5 3 2 1 1
1 2
3 2
4 3
5 4


Output


9
1 3 2 1 3

Note

All vertices should be painted in different colors in the first example. The optimal way to do it is to paint the first vertex into color 1, the second vertex — into color 3, and the third vertex — into color 2. The cost of this painting is 3 + 2 + 1 = 6.

## Categories

- brute force
- constructive algorithms
- dp
- graphs
- implementation
- trees

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
5
3 4 2 1 2
4 2 1 5 4
5 3 2 1 1
1 2
3 2
4 3
5 3
```

**Output**:
```
-1
```

### Example 2

**Input**:
```
5
3 4 2 1 2
4 2 1 5 4
5 3 2 1 1
1 2
3 2
4 3
5 4
```

**Output**:
```
9
1 3 2 1 3
```

### Example 3

**Input**:
```
3
3 2 3
4 3 2
3 1 3
1 2
2 3
```

**Output**:
```
6
1 3 2
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
