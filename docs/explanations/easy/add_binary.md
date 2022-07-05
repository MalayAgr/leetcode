---
layout: default
parent: Easy Problems
grand_parent: Explanations
has_toc: false
nav_order: 13
---

# <!-- omit in toc --> Problem 13 - Add Binary

> Leetcode Link: [Add Binary](https://leetcode.com/problems/add-binary/).

- [Statement](#statement)
- [Examples](#examples)
- [Solution 1 - Use Reverse Loops](#solution-1---use-reverse-loops)
  - [Concept](#concept)
  - [Example](#example)
  - [Time complexity](#time-complexity)
- [Solution 2 - Use `str()`, `int()` and `bin()`](#solution-2---use-str-int-and-bin)
  - [Concept](#concept-1)
  - [Example](#example-1)
  - [Time complexity](#time-complexity-1)

## Statement

Given two binary strings `a` and `b`, return their sum as a binary string.

## Examples

```
Input: a = "11", b = "1"
Output: "100"
```

```
Input: a = "1010", b = "1011"
Output: "10101"
```

## Solution 1 - Use Reverse Loops

### Concept

> **Assertion**: When $$n$$ single digit numbers $$a_1, a_2, ..., a_n$$ in base $$r$$ (i.e $$a_i \lt r$$) are added in base $$r$$, the carry bit is given by $$\lfloor (a_1 + a_2 + ... + a_n) \div r \rfloor$$ and the result bit is given by $$(a_1 + a_2 + ... + a_n) \bmod r$$.
>
> **Note**: This solution uses the ability to index lists and other sequences by negative indices in Python. It only requires small changes to make it work in other languages without changing the underlying concept.

Start with the assumption that $$b$$ is the shorter binary number.

Initialize $$n_a$$ to $$len(a)$$, $$n_b$$ to $$len(b)$$ and $$\text{end}$$ to $$-(n_b + 1)$$.

If $$n_a \lt n_b$$, the assumption is wrong and so make changes to make sure $$b$$ is shorter:

- Exchange $$a$$ and $$b$$
- Set $$\text{end}$$ to $$-(n_a + 1)$$
- Exchange $$n_a$$ and $$n_b$$

Initialize $$\text{carry}$$ to $$0$$.

Initialize $$i$$ to $$-1$$.

Initialize $$\text{result}$$ as the empty string. This will store the sum of $$a$$ and $$b$$ in reverse order.

Since $$b$$ is the shorter binary number, each bit in $$b$$ has a corresponding bit in $$a$$.

While $$i \gt \text{end}$$:

- Set $$\text{carry}$$ to $$\lfloor (a[i] + b[i] + \text{carry}) \div 2 \rfloor$$
- Append the result of $$(a[i] + b[i] + \text{carry}) \bmod 2$$ to $$\text{result}$$
- Decrement $$i$$ by $$1$$

There are no more bits remaining in $$b$$.

Set $$\text{end}$$ to $$-(n_a + 1)$$.

While $$i \gt \text{end}$$:

- Set $$\text{carry}$$ to $$\lfloor (a[i] + \text{carry}) \div 2 \rfloor$$
- Append the result of $$(a[i] + \text{carry}) \bmod 2$$ to $$\text{result}$$
- Decrement $$i$$ by $$1$$

If $$\text{carry} = 1$$, append $$\text{carry}$$ to $$\text{result}$$.

Return the reverse of $$\text{result}$$.

> **Note**: When $$n_a = n_b$$, after the first loop and after $$\text{end}$$ is changed to $$-(n_a + 1)$$, $$i$$ will already be equal to $$\text{end}$$ and hence, the second loop will not run.

### Example

**Input**

```
a = "1101"   # 13
b = "11"     # 3
```

**Indices**

| $$i$$ | $$-4$$ | $$-3$$ | $$-2$$ | $$-1$$ |
|:---:|:---:|:---:|:---:|:---:|
| $$a[i]$$ | 1 | 1 | 0 | 1 |
| $$b[i]$$ |  |  | 1 | 1 |

**Procedure**

- $$n_a = 4$$, $$n_b = 2$$, $$\text{end} = -3$$
- Since $$b$$ is indeed the shorter number, continue
- $$\text{carry} = 0$$, $$i = -1$$, $$\text{result} = \epsilon$$
- Iteration 1:
  - \$$\text{carry} = \lfloor (a[-1] + b[-1] + 0) \div 2 \rfloor = 1$$
  - \$$\text{result} = \epsilon + (a[-1] + b[-1] + 0) \bmod 2 = 0$$
  - \$$i = -1 - 1 = -2$$
- Iteration 2:
  - \$$\text{carry} = \lfloor (a[-2] + b[-2] + 1) \div 2 \rfloor = 1$$
  - \$$\text{result} = 0 + (a[-2] + b[-2] + 1) \bmod 2 = 00$$
  - \$$i = -2 -1 = -3$$
- Since $$i \not \gt \text{end}$$, continue
- \$$\text{end} = -4$$
- Iteration 1:
  - \$$\text{carry} = \lfloor (a[-3] + 1) \div 2 \rfloor = 1$$
  - \$$\text{result} = 00 + (a[-3] + 1) \bmod 2 = 000$$
  - \$$i = -3 - 1 = -4$$
- Iteration 2:
  - \$$\text{carry} = \lfloor (a[-4] + 1) \div 2 \rfloor = 1$$
  - \$$\text{result} = 000 + (a[-4] + 1) \bmod 2 = 0000$$
  - \$$i = -4 - 1 = -5$$
- Since $$i \not \gt \text{end}$$, continue
- Since $$\text{carry} = 1$$, $$\text{result} = 0000 + 1= 00001$$
- Return reverse of $$\text{result}$$, `"10000"` ($$16$$)

### Time complexity

The solution will have to loop over every digit of the longer binary number. Thus, the time complexity is $$\mathcal{O}(\max \{n_a, n_b\})$$.

## Solution 2 - Use `str()`, `int()` and `bin()`

### Concept

Convert $$a$$ and $$b$$ to `int` by calling `a = int(a, 2)` and `b = int(b, 2)` respectively.

Let $$\text{result} = a + b$$.

Convert $$\text{result}$$ to binary by calling `result = bin(result)`.

Convert $$\text{result}$$ to `str` by calling `result = str(result)`.

Return $$\text{result}[2:]$$ since the first two characters are `0b`.

### Example

**Input**

```
a = "1101"   # 13
b = "11"     # 3
```

**Procedure**

- `a = int("1101", 2) = 13`
- `b = int("11", 2) = 3`
- `result = a + b = 16`
- `result = bin(16) = "0b10000`
- `result = str(result)`
- Return `10000`

### Time complexity

The conversion of  the two numbers to `int` is $$\mathcal{O}(n_a)$$ and $$\mathcal{O}(n_b)$$ respectively since the base is known and each digit can be multiplied by a power of the base and added to the overall result.

The conversion to binary and string both are  $$\mathcal{O}(\max \{n_a, n_b\})$$.

Since $$n_a + n_b \gt \max \{n_a, n_b \}$$, the overall time complexity is $$\mathcal{O}(n_a + n_b)$$.
