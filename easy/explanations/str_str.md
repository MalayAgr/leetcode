# <!-- omit in toc --> Problem 9 - Implement strStr()

- [Statement](#statement)
- [Examples](#examples)
- [Solution 1 - Simple Loop](#solution-1---simple-loop)
  - [Concept](#concept)
  - [Example](#example)
  - [Time complexity](#time-complexity)
- [Solution 2 - Use a Deterministic Finite Automata (DFA)](#solution-2---use-a-deterministic-finite-automata-dfa)
  - [Concept](#concept-1)
  - [Example](#example-1)
  - [Time complexity](#time-complexity-1)
- [Solution 3 - Knuth-Morris-Pratt (KMP) Algorithm](#solution-3---knuth-morris-pratt-kmp-algorithm)
  - [Concept](#concept-2)
  - [Example](#example-2)
  - [Time complexity](#time-complexity-2)

## Statement

Implement `strStr()`.

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Clarification:**

What should we return when `needle` is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return `0` when `needle` is an empty string. This is consistent to C's `strstr()` and Java's `indexOf()`.

## Examples

```block
Input: haystack = "hello", needle = "ll"
Output: 2
```

```block
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

## Solution 1 - Simple Loop

### Concept

> **Assertion**: Consider a string $\text{text}$ of length $n$ and a pattern $\text{pattern}$ of length $m \le n$. Then, $\text{pattern}$ can occur in $\text{text}$ starting at any index $i$ such that $0 \le i \le n - m$.

If $\text{needle}$ is an empty string, return $0$.

Let length of $\text{haystack}$ be $n$ and that of $\text{needle}$ be $m$.

For each $0 \le i \le n - m$:

- If $\text{needle} = \text{haystack}[i : i + m]$, return $i$.
- Otherwise, continue.

Return $-1$ by default.

### Example

**Input**

```block
haystack = "hello"
needle = "ll"
```

**Procedure**

- $m = 2$
- Iteration 1:
  - $i = 0$
  - Since $\text{needle} \not = {\text{haystack}[0:2] = \text{he}}$, continue
- Iteration 2:
  - $i = 1$
  - Since $\text{needle} \not = {\text{haystack}[1:3] = \text{el}}$, continue
- Iteration 3:
  - $i = 2$
  - Since $\text{needle} = \text{haystack}[2:4] = \text{ll}$, return $i = 2$

### Time complexity

There are a total of $n - m + 1$ possible values for $i$ and for each $i$, the solution takes out a slice of length $m$. Therefore, the time complexity is $\mathcal{O}((n - m + 1)*m)$.

## Solution 2 - Use a Deterministic Finite Automata (DFA)

### Concept

> To learn about DFAs, see [Deterministic finite automaton](https://en.wikipedia.org/wiki/Deterministic_finite_automaton).
>
> **Assertion 1**: Consider a string $\text{pattern}$ of length $m$. Let $A=(Q, \Sigma, \delta, q_0, F)$ be a DFA such that $L(A)=\{w \mid w \text{ ends with pattern}\}$. Then, $A$ has $m + 1$ states ($|Q| = m$) and a single final state $q_F$ ($|F| = 1$).
>
> For example, if $\text{pattern}=ll$, $Q=\{0, 1, 2\}$, $\Sigma=\{a,b,\dots,z\}$, $q_0=0$ and $F=\{2\}$, then $A$ is as shown:
>
> ![DFA Example](/assets/imgs/dfa_example.png)
>
> **Assertion 2**: Let $A$ be a DFA as mentioned above with $Q=\{0, 1, \dots, m\}$ and $q_F=m$.
>
> Consider a string $\text{text}$ of length $n$.
>
> If $\text{text}$ is processed through $A$ and the final state $q_F=m$ is reached on the character at index $i$, then $\text{pattern}$ exists in $\text{text}$ and starts at index $i - m + 1$.

### Example

### Time complexity

## Solution 3 - Knuth-Morris-Pratt (KMP) Algorithm

### Concept

### Example

### Time complexity
