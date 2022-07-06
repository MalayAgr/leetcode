---
layout: default
parent: Easy Problems
grand_parent: Explanations
has_toc: false
nav_order: 16
---

# <!-- omit in toc --> Problem 16 - Remove Duplicates from Sorted List

> Leetcode Link: [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list).

- [Statement](#statement)
- [Examples](#examples)
- [Solution - Simple Loop](#solution---simple-loop)
  - [Concept](#concept)
  - [Example](#example)
  - [Time complexity](#time-complexity)

## Statement

Given the `head` of a sorted linked list, *delete all duplicates such that each element appears only once*. Return *the linked list **sorted** as well*.

## Examples

```
Input: 1 -> 1 -> 2
Output: 1 -> 2
```

```
Input: 1 -> 1 -> 2 -> 3 -> 3
Output: 1 -> 2 -> 3
```

## Solution - Simple Loop

### Concept

> **Assertion**: In a sorted list, duplicates of a number will form a consecutive chain of nodes.

**List node**:

```python
class ListNode:
    val: int
    next: ListNode
```

If $$\text{head}$$ is `None`, return $$\text{head}$$.

Initialize $$\text{curr}$$ to $$\text{head}.\text{val}$$.

Initialize $$\text{prev}$$ to $$\text{head}$$. At all times, $$\text{prev}$$ will point to the last non-duplicate node in the list.

$$\text{node}$$ to $$\text{head}.\text{next}$$.

While $$\text{node}$$ is not `None`:

- If $$\text{curr} \not = \text{node}.\text{val}$$:
  - Set $$\text{curr}$$ to $$\text{node}.\text{val}$$
  - Since this is a non-duplicate node, set $$\text{prev}.\text{next}$$ to $$\text{node}$$.
  - Advance $$\text{prev}$$ to $$\text{prev}.\text{next}$$
  - Advance $$\text{node}$$ to $$\text{prev}.\text{next}$$ to skip over this node and go to the next one
  - Continue to the next iteration
- Otherwise, advance $$\text{node}$$ to $$\text{node}.\text{next}$$ to skip over the duplicate

Set $$\text{prev}.\text{next}$$ to `None` to mark the end of the list.

Return $$\text{head}$$.

### Example

**Input**

```
Input: 1 -> 1 -> 2 -> 3 -> 3
```

**Procedure**

- Since $$\text{head}$$ is not `None`, continue
- \$$\text{curr} = 1$$
- \$$\text{prev} = \text{head} = \text{ListNode}(1)$$
- \$$\text{node} = \text{head}.\text{next} = \text{ListNode}(1)$$
- Iteration 1 - Since $$\text{curr} = \text{node}.\text{val} = 1$$:
  - Set $$\text{node}$$ to $$\text{node}.\text{next} = \text{ListNode}(2)$$
- Iteration 2 - Since $$\text{curr} \not = \text{node}.\text{val} = 2$$:
  - Set $$\text{curr}$$ to $$2$$
  - Set $$\text{prev}.\text{next}$$ to $$\text{node} = \text{ListNode}(2)$$
  - Set $$\text{prev}$$ to $$\text{prev}.\text{next} = \text{ListNode}(2)$$
  - Set $$\text{node}$$ to $$\text{prev}.\text{next} = \text{ListNode}(3)$$
- Iteration 3 - Since $$\text{curr} \not = \text{node}.\text{val} = 3$$:
  - Set $$\text{curr}$$ to $$3$$
  - Set $$\text{prev}.\text{next}$$ to $$\text{node} = \text{ListNode}(3)$$
  - Set $$\text{prev}$$ to $$\text{prev}.\text{next} = \text{ListNode}(3)$$
  - Set $$\text{node}$$ to $$\text{prev}.\text{next} = \text{ListNode}(3)$$
- Iteration 4 - Since $$\text{curr} = \text{node}.\text{val} = 3$$:
  - Set $$\text{node}$$ to $$\text{node.next}$$, which is `None`.
- Set $$\text{prev}.\text{next}$$ to `None`
- Return $$\text{head}$$

List at the end:

$$1 \rightarrow 2 \rightarrow 3 \rightarrow \text{None}$$

### Time complexity

In the worst-case, the solution will have to loop over the entire list. Thus, the time complexity is $$\mathcal{O}(n)$$.
