# 1345_E. Quantifier Question

**ID:** 1345_e_quantifier_question_3149
**Difficulty:** 11

## Description

Logical quantifiers are very useful tools for expressing claims about a set. For this problem, let's focus on the set of real numbers specifically. The set of real numbers includes zero and negatives. There are two kinds of quantifiers: universal (∀) and existential (∃). You can read more about them here.

The universal quantifier is used to make a claim that a statement holds for all real numbers. For example:

  * ∀ x,x<100 is read as: for all real numbers x, x is less than 100. This statement is false. 
  * ∀ x,x>x-1 is read as: for all real numbers x, x is greater than x-1. This statement is true. 



The existential quantifier is used to make a claim that there exists some real number for which the statement holds. For example:

  * ∃ x,x<100 is read as: there exists a real number x such that x is less than 100. This statement is true. 
  * ∃ x,x>x-1 is read as: there exists a real number x such that x is greater than x-1. This statement is true. 



Moreover, these quantifiers can be nested. For example:

  * ∀ x,∃ y,x<y is read as: for all real numbers x, there exists a real number y such that x is less than y. This statement is true since for every x, there exists y=x+1. 
  * ∃ y,∀ x,x<y is read as: there exists a real number y such that for all real numbers x, x is less than y. This statement is false because it claims that there is a maximum real number: a number y larger than every x. 



Note that the order of variables and quantifiers is important for the meaning and veracity of a statement.

There are n variables x_1,x_2,…,x_n, and you are given some formula of the form $$$ f(x_1,...,x_n):=(x_{j_1}<x_{k_1})∧ (x_{j_2}<x_{k_2})∧ ⋅⋅⋅∧ (x_{j_m}<x_{k_m}), $$$

where ∧ denotes logical AND. That is, f(x_1,…, x_n) is true if every inequality x_{j_i}<x_{k_i} holds. Otherwise, if at least one inequality does not hold, then f(x_1,…,x_n) is false.

Your task is to assign quantifiers Q_1,…,Q_n to either universal (∀) or existential (∃) so that the statement $$$ Q_1 x_1, Q_2 x_2, …, Q_n x_n, f(x_1,…, x_n) $$$

is true, and the number of universal quantifiers is maximized, or determine that the statement is false for every possible assignment of quantifiers.

Note that the order the variables appear in the statement is fixed. For example, if f(x_1,x_2):=(x_1<x_2) then you are not allowed to make x_2 appear first and use the statement ∀ x_2,∃ x_1, x_1<x_2. If you assign Q_1=∃ and Q_2=∀, it will only be interpreted as ∃ x_1,∀ x_2,x_1<x_2.

Input

The first line contains two integers n and m (2≤ n≤ 2⋅ 10^5; 1≤ m≤ 2⋅ 10^5) — the number of variables and the number of inequalities in the formula, respectively.

The next m lines describe the formula. The i-th of these lines contains two integers j_i,k_i (1≤ j_i,k_i≤ n, j_i≠ k_i).

Output

If there is no assignment of quantifiers for which the statement is true, output a single integer -1.

Otherwise, on the first line output an integer, the maximum possible number of universal quantifiers.

On the next line, output a string of length n, where the i-th character is "A" if Q_i should be a universal quantifier (∀), or "E" if Q_i should be an existential quantifier (∃). All letters should be upper-case. If there are multiple solutions where the number of universal quantifiers is maximum, print any.

Examples

Input


2 1
1 2


Output


1
AE


Input


4 3
1 2
2 3
3 1


Output


-1


Input


3 2
1 3
2 3


Output


2
AAE

Note

For the first test, the statement ∀ x_1, ∃ x_2, x_1<x_2 is true. Answers of "EA" and "AA" give false statements. The answer "EE" gives a true statement, but the number of universal quantifiers in this string is less than in our answer.

For the second test, we can show that no assignment of quantifiers, for which the statement is true exists.

For the third test, the statement ∀ x_1, ∀ x_2, ∃ x_3, (x_1<x_3)∧ (x_2<x_3) is true: We can set x_3=max\\{x_1,x_2\}+1.

## Categories

- dfs and similar
- dp
- graphs
- math

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
3 2
1 3
2 3
```

**Output**:
```
2
AAE
```

### Example 2

**Input**:
```
4 3
1 2
2 3
3 1
```

**Output**:
```
-1
```

### Example 3

**Input**:
```
2 1
1 2
```

**Output**:
```
1
AE
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
