# <!-- omit in toc --> Problem 2 - Palindrome Number

> Leetcode Link: [Palindrome Number](https://leetcode.com/problems/palindrome-number).

- [Statement](#statement)
- [Examples](#examples)
- [Solution 1 - Convert Number to a String](#solution-1---convert-number-to-a-string)
  - [Concept](#concept)
  - [Example](#example)
  - [Time Complexity](#time-complexity)
- [Solution 2 - Construct Reverse Using Mod 10](#solution-2---construct-reverse-using-mod-10)
  - [Concept](#concept-1)
  - [Example](#example-1)
  - [Time Complexity](#time-complexity-1)

## Statement

Given an integer `x`, return true if `x` is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

## Examples

```block
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

```block
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

```block
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

## Solution 1 - Convert Number to a String

### Concept

Convert number to a string and compare it with its reverse.

### Example

**Input**

```block
x = 121
```

**Procedure**

- Use `str()` to convert `121` to a string.
- Compare `'121'` with `'121'` and return the result.

### Time Complexity

Since the number is converted to a string and then reversed, the time complexity is $\mathcal{O}(n)$, where $n$ is the number of digits in the number.

## Solution 2 - Construct Reverse Using Mod 10

### Concept

> **Assertion 1**: If a number is divided by $10$, the remainder is the last digit of the number. Example: $134\bmod10=4$.
>
> **Assertion 2**: If a number is divided by $10$, the quotient is the number formed by all digits of the number except the last one. Example: $134\div10=13$.
>
> **Assertion 3**. Consider a number $d_1d_2...d_n$, where $d_i$ is a digit of the number. If the reverse of the number so far is $d_nd_{n-1}...d_{i+1}$ and the current digit from the right is $d_i$, then the new reverse $d_nd_{n-1}...d_{i+1}d_i = d_nd_{n-1}...d_{i+1}*10+d_i$.

If $x \lt 0$, return `False` since no negative number can be a palindrome due to the negative sign.

Otherwise, initialize $reverse$ as $0$ to store the reverse of $x$.

Create a copy $temp_x$ of $x$.

While $temp_x \not ={0}$:

- Get the remainder as $remainder = temp_x \bmod 10$
- Update the reverse as $reverse=reverse*10+remainder$
- Update $temp_x$ as $temp_x = \lfloor temp_x \div 10 \rfloor$

If $reverse=x$, return `True`. Otherwise, return `False`.

### Example

**Input**

```block
x = 121
```

**Procedure**

- $reverse = 0$ and $temp_x = x = 121$
- Iteration 1:
  - $remainder = 121 \bmod 10 = 1$
  - $reverse = 0 * 10 + 1 = 1$
  - $temp_x = \lfloor 121 \div 10 \rfloor = 12$
- Iteration 2:
  - $remainder = 12 \bmod 10 = 2$
  - $reverse = 1 * 10 + 2 = 12$
  - $temp_x = \lfloor 12 \div 10 \rfloor = 1$
- Iteration 3:
  - $remainder = 1 \bmod 10 = 1$
  - $reverse = 12 * 10 + 1 = 121$
  - $temp_x = \lfloor 1 \div 10 \rfloor = 0$
- Since $reverse = 121 = x$, return `True`

### Time Complexity

Since the reverse is built one digit at a time, the time complexity is $\mathcal{O}(n)$, where $n$ is the number of digits in the number.
