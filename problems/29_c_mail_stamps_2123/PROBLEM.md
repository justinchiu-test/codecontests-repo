# 29_C. Mail Stamps

**ID:** 29_c_mail_stamps_2123
**Difficulty:** 9

## Description

One day Bob got a letter in an envelope. Bob knows that when Berland's post officers send a letter directly from city «A» to city «B», they stamp it with «A B», or «B A». Unfortunately, often it is impossible to send a letter directly from the city of the sender to the city of the receiver, that's why the letter is sent via some intermediate cities. Post officers never send a letter in such a way that the route of this letter contains some city more than once. Bob is sure that the post officers stamp the letters accurately.

There are n stamps on the envelope of Bob's letter. He understands that the possible routes of this letter are only two. But the stamps are numerous, and Bob can't determine himself none of these routes. That's why he asks you to help him. Find one of the possible routes of the letter.

Input

The first line contains integer n (1 ≤ n ≤ 105) — amount of mail stamps on the envelope. Then there follow n lines with two integers each — description of the stamps. Each stamp is described with indexes of the cities between which a letter is sent. The indexes of cities are integers from 1 to 109. Indexes of all the cities are different. Every time the letter is sent from one city to another, exactly one stamp is put on the envelope. It is guaranteed that the given stamps correspond to some valid route from some city to some other city.

Output

Output n + 1 numbers — indexes of cities in one of the two possible routes of the letter.

Examples

Input

2
1 100
100 2


Output

2 100 1

Input

3
3 1
100 2
3 2


Output

100 2 3 1

## Categories

- data structures
- dfs and similar
- graphs
- implementation

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
2
1 100
100 2
```

**Output**:
```
1 100 2
```

### Example 2

**Input**:
```
3
3 1
100 2
3 2
```

**Output**:
```
1 3 2 100
```

### Example 3

**Input**:
```
6
264896923 2497658
57071588 447086061
2497658 483723090
57071588 264896923
158310110 483723090
158310110 72866107
```

**Output**:
```
72866107 158310110 483723090 2497658 264896923 57071588 447086061
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
