# 1407_E. Egor in the Republic of Dagestan

**ID:** 1407_e_egor_in_the_republic_of_dagestan_1382
**Difficulty:** 11

## Description

Egor is a famous Russian singer, rapper, actor and blogger, and finally he decided to give a concert in the sunny Republic of Dagestan.

There are n cities in the republic, some of them are connected by m directed roads without any additional conditions. In other words, road system of Dagestan represents an arbitrary directed graph. Egor will arrive to the city 1, travel to the city n by roads along some path, give a concert and fly away.

As any famous artist, Egor has lots of haters and too annoying fans, so he can travel only by safe roads. There are two types of the roads in Dagestan, black and white: black roads are safe at night only, and white roads — in the morning. Before the trip Egor's manager's going to make a schedule: for each city he'll specify it's color, black or white, and then if during the trip they visit some city, the only time they can leave it is determined by the city's color: night, if it's black, and morning, if it's white. After creating the schedule Egor chooses an available path from 1 to n, and for security reasons it has to be the shortest possible.

Egor's manager likes Dagestan very much and wants to stay here as long as possible, so he asks you to make such schedule that there would be no path from 1 to n or the shortest path's length would be greatest possible.

A path is one city or a sequence of roads such that for every road (excluding the first one) the city this road goes from is equal to the city previous road goes into. Egor can move only along paths consisting of safe roads only. 

The path length is equal to the number of roads in it. The shortest path in a graph is a path with smallest length.

Input

The first line contains two integers n, m (1 ≤ n ≤ 500000, 0 ≤ m ≤ 500000) — the number of cities and the number of roads.

The i-th of next m lines contains three integers — u_i, v_i and t_i (1 ≤ u_i, v_i ≤ n, t_i ∈ \{0, 1\}) — numbers of cities connected by road and its type, respectively (0 — night road, 1 — morning road).

Output

In the first line output the length of the desired path (or -1, if it's possible to choose such schedule that there's no path from 1 to n).

In the second line output the desired schedule — a string of n digits, where i-th digit is 0, if the i-th city is a night one, and 1 if it's a morning one.

If there are multiple answers, print any.

Examples

Input


3 4
1 2 0
1 3 1
2 3 0
2 3 1


Output


2
011

Input


4 8
1 1 0
1 3 0
1 3 1
3 2 0
2 1 0
3 4 1
2 4 0
2 4 1


Output


3
1101

Input


5 10
1 2 0
1 3 1
1 4 0
2 3 0
2 3 1
2 5 0
3 4 0
3 4 1
4 2 1
4 5 0


Output


-1
11111

Note

For the first sample, if we paint city 1 white, the shortest path is 1 → 3. Otherwise, it's 1 → 2 → 3 regardless of other cities' colors.

For the second sample, we should paint city 3 black, and there are both black and white roads going from 2 to 4. Note that there can be a road connecting a city with itself.

## Categories

- constructive algorithms
- dfs and similar
- dp
- graphs
- greedy
- shortest paths

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
3 4
1 2 0
1 3 1
2 3 0
2 3 1
```

**Output**:
```
2
010
```

### Example 2

**Input**:
```
5 10
1 2 0
1 3 1
1 4 0
2 3 0
2 3 1
2 5 0
3 4 0
3 4 1
4 2 1
4 5 0
```

**Output**:
```
-1
01010
```

### Example 3

**Input**:
```
4 8
1 1 0
1 3 0
1 3 1
3 2 0
2 1 0
3 4 1
2 4 0
2 4 1
```

**Output**:
```
3
1100
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
