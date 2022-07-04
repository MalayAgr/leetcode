---
layout: default
parent: Easy Problems
grand_parent: Explanations
has_toc: false
nav_order: 11
---

# <!-- omit in toc --> Problem 11 - Length of Last Word

- [Statement](#statement)
- [Examples](#examples)
- [Solution - Use a Reverse Loop](#solution---use-a-reverse-loop)
  - [Concept](#concept)
  - [Example](#example)
  - [Time Complexity](#time-complexity)

## Statement

Given a string s consisting of words and spaces, return *the length of the **last** word in the string*.

A word is a maximal substring consisting of non-space characters only.

## Examples

```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

## Solution - Use a Reverse Loop

### Concept

Initialize a variable $$i$$ as $$len(s) - 1$$.

While $$s[i]$$ is `" "`, decrement $$i$$ by $$1$$.

Initialize a variable $$\text{length}$$ as $$0$$ to store the length of the last word.

While $$s[i]$$ is not `" "`, increment $$\text{length}$$ by $$1$$ and decrement $$i$$ by $$1$$.

Return $$\text{length}$$.

### Example

**Input**

```
s = "   fly me   to   the moon  "
```

**Procedure**

- \$$i = len(s) - 1 = 26$$
- Since $$s[26]$$ is a space, $$i = i - 1 = 25$$
- Since $$s[25]$$ is a space, $$i = i - 1 = 24$$
- \$$\text{length} = 0$$
- Iteration 1:
  - Since $$s[24]$$ is not a space, $$\text{length} = \text{length} + 1 = 1$$
  - \$$i = i - 1 = 23$$
- Iteration 2:
  - Since $$s[23]$$ is not a space, $$\text{length} = \text{length} + 1 = 2$$
  - \$$i = i - 1 = 22$$
- Iteration 3:
  - Since $$s[22]$$ is not a space, $$\text{length} = \text{length} + 1 = 3$$
  - \$$i = i - 1 = 21$$
- Iteration 4:
  - Since $$s[21]$$ is not a space, $$\text{length} = \text{length} + 1 = 4$$
  - \$$i = i - 1 = 20$$
- Since $$s[20]$$ is a space, stop
- Return $$\text{length} = 4$$

### Time Complexity

In Python, the `len()` function is an $$\mathcal{O}(1)$$ operation.

Since the solution simply loops from the end of the string until the first space before the last word, the time complexity is $$\mathcal{O}(k + m)$$, where $$k$$ is the length of the last word and $$m$$ is the number of spaces after the last word.
