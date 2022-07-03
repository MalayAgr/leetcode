---
layout: default
parent: Easy Problems
grand_parent: Explanations
has_toc: false
---
# <!-- omit in toc --> Problem 5 - Valid Parentheses

> Leetcode Link: [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/).

- [Statement](#statement)
- [Examples](#examples)
- [Solution - Use a Stack](#solution---use-a-stack)
  - [Concept](#concept)
  - [Example](#example)
  - [Time Complexity](#time-complexity)

## Statement

Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

## Examples

```block
Input: s = "()"
Output: true
```

```block
Input: s = "()[]{}"
Output: true
```

```block
Input: s = "(]"
Output: false
```

## Solution - Use a Stack

### Concept

> **Assertion 1**: If a string of parentheses is valid and:
>
> - Each opening bracket encountered is pushed onto a stack while,
> - The stack is popped on encountering a closing bracket,
>
> The result of the pop operation is always the opening bracket corresponding to the closing bracket that led to the pop operation. This is due to the nesting nature of brackets.
>
> **Assertion 2**: If a string of parentheses is valid, the stack should be empty after the entire string has been processed according to the above assertion. This is because there is one closing bracket for each opening bracket.

Create an empty stack.

For each character in the string:

- If it is an opening bracket, push it on the stack.
- If it is a closing bracket, perform a pop on the stack to get the last seen opening bracket. If this opening bracket is not of the same type as the closing bracket, return `False`.

After the string is exhausted, return `True` if the stack is empty. Otherwise, return `False`.

### Example

**Input**

```block
s = ([]){}
```

**Procedure**

> Note: TOS is the last element.

- `stack = []`
- Iteration 1:
  - Since `(` is an opening bracket, push it onto the stack.
  - `stack = [(]`
- Iteration 2:
  - Since `[` is an opening bracket, push it onto the stack.
  - `stack = [(, []`
- Iteration 3:
  - Since `]` is a closing bracket, pop the stack to get `[`, which is the correct opening bracket
  - `stack = [(]`
- Iteration 4:
  - Since `)` is a closing bracket, pop the stack to get `(`, which is the correct opening bracket
  - `stack = []`
- Iteration 5:
  - Since `{` is an opening bracket, push it onto the stack.
  - `stack = [{]`
- Iteration 6:
  - Since `}` is a closing bracket, pop the stack to get `}`, which is the correct opening bracket
  - `stack = []`
- Since the the stack is empty, return `True`

### Time Complexity

In the worst-case, the entire string will be looped over before getting the answer. Thus, the time complexity is $$\mathcal{O}(n)$$.
