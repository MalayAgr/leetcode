---
layout: default
parent: Easy Problems
grand_parent: Explanations
has_toc: false
nav_order: 12
---

# <!-- omit in toc --> Problem 12 - Plus One

- [Statement](#statement)
- [Examples](#examples)
- [Solution](#solution)
  - [Concept](#concept)
  - [Example](#example)
  - [Time Complexity](#time-complexity)

## Statement

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the $$i^{th}$$ digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

## Examples

```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```

```
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```

## Solution

### Concept

> **Assertion**: Consider a number $$a = d_1d_2...d_n$$, where $$d_i$$ is a digit of the number. Incrementing $$a$$ by $$1$$ is equivalent to setting $$d_i = 0$$ for all consecutive $$d_i=9$$ and adding $$1$$ to the first $$d_i$$ such that $$d_i \not = 9$$, where $$i$$ starts at the end of the number and goes up to the beginning.

Initialize $$i$$ to $$len(\text{digits}) - 1$$.

While $$\text{digits}[i] = 9$$:

- Set $$\text{digits}[i]$$ to $$0$$.
- Decrement $$i$$ by $$1$$.

If $$i = -1$$ after this ($$\text{digits} = [9, 9, ..., 9]$$), insert $$1$$ at the beginning of $$\text{digits}$$ and return the result.

Otherwise, increment $$\text{digits}[i]$$ by $$1$$ and return $$\text{digits}$$.

### Example

**Input**

```
digits = [4,3,2,1]
```

**Procedure**

- \$$i = len(\text{digits}) - 1 = 3$$
- Since $$\text{digits}[3] \not = 9$$, continue
- Since $$i \not = -1$$, continue
- Increment $$\text{digits}[3] = 1$$ by $$1$$ so that $$\text{digits}= [4, 3, 2, 2]$$
- Return $$\text{digits}$$

### Time Complexity

In the worst-case, $$\text{digits}$$ is a number like $$9\dots9$$. All digits will have to be set to $$0$$ and thus, the time complexity is $$\mathcal{O}(n)$$.

In the best-case, $$\text{digits}$$ doesn't end with $$9$$. Only the last digit needs to be incremented by $$1$$. Thus, the time complexity is $$\mathcal{O}(1)$$.
