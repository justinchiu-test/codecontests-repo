# 959_E. Mahmoud and Ehab and the xor-MST

**ID:** 959_e_mahmoud_and_ehab_and_the_xormst_2359
**Difficulty:** 11

## Description

Ehab is interested in the bitwise-xor operation and the special graphs. Mahmoud gave him a problem that combines both. He has a complete graph consisting of n vertices numbered from 0 to n - 1. For all 0 ≤ u < v < n, vertex u and vertex v are connected with an undirected edge that has weight <image> (where <image> is the [bitwise-xor operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR)). Can you find the weight of the minimum spanning tree of that graph?

You can read about complete graphs in <https://en.wikipedia.org/wiki/Complete_graph>

You can read about the minimum spanning tree in <https://en.wikipedia.org/wiki/Minimum_spanning_tree>

The weight of the minimum spanning tree is the sum of the weights on the edges included in it.

Input

The only line contains an integer n (2 ≤ n ≤ 1012), the number of vertices in the graph.

Output

The only line contains an integer x, the weight of the graph's minimum spanning tree.

Example

Input

4


Output

4

Note

In the first sample: <image> The weight of the minimum spanning tree is 1+2+1=4.

## Categories

- bitmasks
- dp
- graphs
- implementation
- math

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
4
```

**Output**:
```
4
```

### Example 2

**Input**:
```
2
```

**Output**:
```
1
```

### Example 3

**Input**:
```
7
```

**Output**:
```
11
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
