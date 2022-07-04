---
layout: default
parent: Easy Problems
grand_parent: Explanations
has_toc: false
nav_order: 10
---

# <!-- omit in toc --> Problem 10 - Search Insert Position

> Leetcode Link: [Search Insert Position](https://leetcode.com/problems/search-insert-position).

- [Statement](#statement)
- [Examples](#examples)
- [Solution - Use Binary Search](#solution---use-binary-search)
  - [Concept](#concept)
  - [Example](#example)
  - [Time complexity](#time-complexity)

## Statement

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with $$\mathcal{O}(\log{} n)$$ runtime complexity.

## Examples

```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

## Solution - Use Binary Search

### Concept

> Words of a wise man: Sorted array? Consider binary search first.
>
> **Assertion 1**: Consider a sorted array $$a[1...n]$$ and a target value $$\text{target}$$ which is not present in $$a$$. If binary search is used on $$a$$ to find $$\text{target}$$, then the position where $$\text{target}$$ should be inserted in $$a$$ is $$\text{high} + 1$$, where $$\text{high}$$ is the last value at the end of search for the upper end of the array.

Execute binary search on the array with the target value as the key. Return either the index of the middle element where the target value is present or $$\text{high} + 1$$.

### Example

**Input**

```
nums = [1,3,5,6]
target = 2
```

**Procedure**

- $$\text{low} = 0$$ and $$\text{high} = 3$$
- Iteration 1:
  - \$$\text{mid} = \lfloor \frac{0 + 3}{2} \rfloor = 1$$
  - Since $$\text{nums}[1] = 3 \gt \text{target}$$, $$\text{high} = \text{high} - 1 = 2$$
- Iteration 2:
  - \$$\text{mid} = \lfloor \frac{0 + 2}{2} \rfloor = 1$$
  - Since $$\text{nums}[1] = 3 \gt \text{target}$$, $$\text{high} = \text{high} - 1 = 1$$
- Iteration 3:
  - \$$\text{mid} = \lfloor \frac{0 + 1}{2} \rfloor = 0$$
  - Since $$\text{nums}[0] = 1 \lt \text{target}$$, $$\text{low} = \text{low} + 1 = 1$$
- Iteration 4:
  - \$$\text{mid} = \lfloor \frac{1 + 1}{2} \rfloor = 1$$
  - Since $$\text{nums}[1] = 3 \gt \text{target}$$, $$\text{high} = \text{high} - 1 = 0$$
- Since $$\text{high} \lt \text{low}$$, stop
- Return $$\text{high} + 1$$, which is $$1$$

### Time complexity

Since the solution uses binary search, the time complexity is $$\mathcal{O}(\log{} n)$$.
