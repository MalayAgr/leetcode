---
layout: default
parent: Easy Problems
grand_parent: Explanations
has_toc: false
nav_order: 14
---

# <!-- omit in toc --> Problem 14 - Sqrt(x)

> Leetcode Link: [Sqrt(x)](https://leetcode.com/problems/sqrtx/).

- [Statement](#statement)
- [Examples](#examples)
- [Solution - Use Newton's Method](#solution---use-newtons-method)
  - [Concept](#concept)
  - [Example](#example)
  - [Time complexity](#time-complexity)

## Statement

Given a non-negative integer `x`, compute and return the square root of `x`.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

**Note**: You are not allowed to use any built-in exponent function or operator, such as `pow(x, 0.5)` or `x ** 0.5`.

## Examples

```
Input: x = 4
Output: 2
```

```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
```

## Solution - Use Newton's Method

### Concept

> To learn more about Newton's Method, see: [Newton's Method](https://en.wikipedia.org/wiki/Newton%27s_method).

> **Assertion 1**: Given a number $$a$$, the square root of $$a$$ is a number $$x$$ such that $$x^2 = a$$. Finding this $$x$$ is equivalent to finding the roots of the function $$f(x) = x^2 - a$$ since $$f(x)$$ can be written as $$f(x) = (x - \sqrt{a})(x + \sqrt{a})$$, which has the two roots $$\pm \sqrt{a}$$.

> **Assertion 2**: According to Newton's Method, given an initial guess $$x_0$$, the roots of a function $$f(x)$$ can be found using the recurrent formula below, where $$f^\prime(x)$$ is the first-order derivative of $$f(x)$$, with more iterations yielding a more accurate result:

> $$x_{n + 1} = x_n - \frac{f(x_n)}{f^\prime(x_n)}$$

> **Assertion 3**: If $$f(x) = x^2 - a$$, then $$f^\prime(x) = 2x$$.

> **Assertion 4**: The roots of $$f(x) = x^2 - a$$ can be found by the following recurrent formula (arithmetic mean of $$x_n$$ and $$\frac{a}{x_n}$$):

> $$x_{n + 1} = \frac{1}{2}(x_n + \frac{a}{x_n})$$
>
> Since, according to Newton's method:
>
> $$x_{n + 1} = x_n - \frac{x_n^2 - a}{2x_n} = \frac{1}{2x_n}(2x_n^2 - x_n^2 + a) = \frac{1}{2x_n}(x_n^2 + a) = \frac{1}{2}(x_n + \frac{a}{x_n})$$

> **Note**: $$a$$ in the above assertions is $$x$$ in the problem statement.

If $$x = 0$$, return $$x$$.

Initialize $$\text{root}$$ to $$\frac{x}{2}$$. This will be the initial guess and will be updated in a loop according to the formula defined above.

Since only the integer part is required, initialize $$\text{epsilon}$$ to the relatively large number $$1 \times 10^{-3}$$. This will be the precision level.

In an infinite loop:

- Set $$\text{prev}$$ to $$\text{root}$$ to store the previous value of $$\text{root}$$
- Set $$\text{root}$$ to $$\frac{1}{2}(\text{root} + \frac{a}{\text{root}})$$
- If $$\lvert \text{prev} - \text{root} \rvert \le \text{epsilon}$$, return the integer part of $$\text{root}$$
- Otherwise, continue

### Example

**Input**

```
x = 8
```

**Procedure**

- Since $$x \not = 0$$, continue
- $$\text{root} = 8 / 2 = 4$$, $$\text{epsilon} = 0.001$$
- Iteration 1:
  - \$$\text{prev} = 4$$
  - \$$\text{root} = \frac{1}{2}(4 + \frac{8}{4}) = 3$$
  - Since $$\lvert \text{prev} - \text{root} \rvert = 1 \not \le 0.001$$, continue
- Iteration 2:
  - \$$\text{prev} = 3$$
  - \$$\text{root} = \frac{1}{2}(3 + \frac{8}{3}) \approx 2.8 \overline{3}$$
  - Since $$\lvert \text{prev} - \text{root} \rvert \approx 0.1 \overline{6} \not \le 0.001$$, continue
- Iteration 3:
  - \$$\text{prev} = 2.8 \overline{3}$$
  - \$$\text{root} = \frac{1}{2}(2.8 \overline{3} + \frac{8}{2.8 \overline{3}}) \approx 2.82843$$
  - Since $$\lvert \text{prev} - \text{root} \rvert \approx 0.005 \not \le 0.001$$, continue
- Iteration 4:
  - \$$\text{prev} = 2.82843$$
  - \$$\text{root} = \frac{1}{2}(2.82843 + \frac{8}{2.82843}) \approx 2.82842$$
  - Since $$\lvert \text{prev} - \text{root} \rvert \approx 0.00001 \le 0.001$$, return `int(root) = 2`.

### Time complexity

If a result with a precision of $$n$$ digits is required, Newton's Method has a time complexity of $$\mathcal{O}(\log{}n)$$, provided the initial guess is a good guess.
