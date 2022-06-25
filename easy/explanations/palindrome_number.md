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

Since the number is converted to a string and then reversed, the time complexity is $\mathcal{O}(k)$, where $k$ is the number of digits in the number.

## Solution 2 - Construct Reverse Using Mod 10

### Concept

> **Assertion 1**: If a number is divided by $10$, the remainder is the last digit of the number. Example: $134\bmod10=4$.
>
> **Assertion 2**: If a number is divided by $10$, the quotient is the number formed by all digits of the number except the last one. Example: $134\div10=13$.
>
> **Assertion 3**. Consider a number $d_1d_2...d_n$, where $d_i$ is a digit of the number. If the reverse of the number so far is $d_nd_{n-1}...d_{i+1}$ and the current digit from the right is $d_i$, then the new reverse is $d_nd_{n-1}...d_{i+1}*10+d_i$.

If $x$ negative, return `False` since no negative number can be a palindrome due to the negative sign.

Otherwise, initialize $reverse$ as $0$ to store the reverse of $x$. Create a copy of $x$ and do the following using the copy:

1. Get the remainder when $x$ is divided by $10$. This will give the last digit of the number.
2. Update the reverse so that the last digit will be in the correct position. This is done as $reverse=reverse*10+remainder$.
3. Update $x$ by dividing it by $10$ so that the last digit is dropped.

Repeat this until the copy becomes $0$. At the end, $reverse$ will have the reverse of $x$.

Return the result of $reverse==x$.

### Example

**Input**

```block
x = 121
```

**Procedure**

- `reverse = 0` and `temp_x = x = 121`.
- Iteration 1:
  - `remainder = 121 % 10 = 1`
  - `reverse = 0 * 10 + 1 = 1`
  - `temp_x = 121 // 10 = 12`
- Iteration 2:
  - `remainder = 12 % 10 = 2`
  - `reverse = 1 * 10 + 2 = 12`
  - `temp_x = 12 // 10 = 1`
- Iteration 3:
  - `remainder = 1 % 10 = 1`
  - `reverse = 12 * 10 + 1 = 121`.
  - `temp_x = 1 // 10 = 0`
- Since `reverse = 121 = x`, return `True`.

### Time Complexity

Since the reverse is built one digit at a time, the time complexity is $\mathcal{O}(k)$, where $k$ is the number of digits in the number.
