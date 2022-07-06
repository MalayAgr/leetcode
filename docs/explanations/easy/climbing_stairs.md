---
layout: default
parent: Easy Problems
grand_parent: Explanations
has_toc: false
nav_order: 15
---

# <!-- omit in toc --> Problem 15 - Climbing Stairs

> Leetcode Link: [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/).

- [Statement](#statement)
- [Examples](#examples)
- [Solution - Use the Fibonacci Sequence](#solution---use-the-fibonacci-sequence)
  - [Concept](#concept)
  - [Example](#example)
  - [Time complexity](#time-complexity)

## Statement

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

## Examples

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

## Solution - Use the Fibonacci Sequence

### Concept

> **Assertion 1**: Consider that there is a staircase requiring $$n$$ steps to reach the top and a person can either climb $$1$$ or $$2$$ steps at a time. Let $$a_n$$ be the number of ways of climbing $$n$$ steps. Then:
>
> - The person can take $$1$$ step and climb the remaining $$n - 1$$ steps in $$a_{n - 1}$$ ways, or
> - The person can take $$2$$ steps and climb the remaining $$n - 2$$ steps in $$a_{n - 2}$$ ways
>
> That is:
>
> $$a_n = a_{n - 1} + a_{n - 2}$$
>
> Where $$a_0 = 0$$ and $$a_1 = 1$$

> **Assertion 2**: The number of ways of climbing the $$n$$ steps is equal to the $$n^{th}$$ Fibonacci number when counted from $$0$$.

Initialize $$a$$ to $$0$$ and $$b$$ to $$1$$.

For $$i = 0 \dots n - 1$$, exchange $$a$$ with $$b$$ and $$b$$ with $$a + b$$ using `a, b = b, a + b`.

Return $$b$$.

### Example

**Input**

```
n = 3
```

**Procedure**

> **Note**: Since this uses `a, b = b, a + b`, `a` and `b` will be changed using their previous values.

- $$a = 0$$, $$b = 1$$
- Iteration 1:
  - \$$a = 1$$
  - \$$b = 0 + 1 = 1$$
- Iteration 2:
  - \$$a = 1$$
  - \$$b = 1 + 1 = 2$$
- Iteration 3:
  - \$$a = 2$$
  - \$$b = 1 + 2 = 3$$
- Return $$b = 3$$

### Time complexity

Since the solution does $$n$$ iterations, the time complexity is $$\mathcal{O}(n)$$.
