# <!-- omit in toc --> Problem 6 - Merge Two Sorted Lists

> Leetcode Link: [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/).

- [Statement](#statement)
- [Examples](#examples)
- [Solution - Adat Merging From Merge Sort](#solution---adat-merging-from-merge-sort)
  - [Concept](#concept)
  - [Examples](#examples-1)
  - [Time Complexity](#time-complexity)

## Statement

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## Examples

```block
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

```block
Input: list1 = [], list2 = []
Output: []
```

```block
Input: list1 = [], list2 = [0]
Output: [0]
```

## Solution - Adat Merging From Merge Sort

### Concept

> **Assertion 1**: Let the two lists to be merged be $a[m]$ and $b[n]$ and the merged list be $c[m + n]$. Consider the two lists as two stacks $s_a$ and $s_b$ with the TOS being the first element. Then:
> $$c_i=\min\{TOS(s_a),TOS(s_b)\}$$
> Provided that the respective stack is popped after each $c_i$ is assigned and neither of the stacks run out.
>
> **Assertion 2**: If either of the stacks runs out first and $s$ is the other stack, $c_i=TOS(s)$ for all $i$ until $s$ is empty.

**List node**:

```python
class ListNode:
    val: int
    next: ListNode
```

Copy the heads of the two lists. Let these copies be $\text{curr}_a$ and $\text{curr}_b$ respectively.

If $\text{curr}_a$ has no elements, return $\text{curr}_b$.

Otherwise, create a new linked list $\text{result}$ with a dummy head node with any value.

Copy the head of $\text{result}$. Let the copy be $\text{curr}_{\text{res}}$.

Until either $\text{curr}_a$ or $\text{curr}_b$ reach the end of their respective lists, do the following:

- If $\text{curr}_a.\text{val} \le \text{curr}_b.\text{val}$:
  - Set $\text{curr}_{\text{res}}.\text{next}$ to $curr_a$
  - Advance $\text{curr}_{\text{res}}$ to $\text{curr}_{\text{res}}.\text{next}$
  - Advance $\text{curr}_a$ to $\text{curr}_a.\text{next}$.
- Otherwise:
  - Set $\text{curr}_{\text{res}}.\text{next}$ to $\text{curr}_b$
  - Advance $\text{curr}_{\text{res}}$ to $\text{curr}_{\text{res}}.\text{next}$
  - Advance $\text{curr}_b$ to $\text{curr}_b.\text{next}$.

Set $\text{curr}_{\text{res}}.\text{next}$ to either $\text{curr}_a$ or $\text{curr}_b$, whichever hasn't reached the end of its list.

Since the first node in $\text{result}$ is a dummy head node, advance $\text{result}$ to $\text{result}.\text{next}$ so that it is at the correct head node.

Return $\text{result}$.

### Examples

> **Note**: Each number here is actually a `ListNode` with `val` set to the number and `next` set to a `ListNode` with the next number.

**Input**

```block
list1 = [1,2,4], list2 = [1,3,4]
```

**Procedure**

- $\text{curr}_a = 1$ and $\text{curr}_b = 1$.
- Since neither is `None`, continue.
- $\text{result} = -1$ and $\text{curr}_{\text{res}} = -1$.
- Iteration 1. Since $\text{curr}_a.\text{val} = 1 \le \text{curr}_b.\text{val} = 1$:
  - Set $\text{curr}_{\text{res}}.\text{next} = 1$.
  - Set $\text{curr}_{\text{res}} = \text{curr}_{\text{res}}.\text{next} = 1$.
  - Set $\text{curr}_a = \text{curr}_a.\text{next} = 2$.
- Iteration 2. Since $\text{curr}_b.\text{val} = 1 \le \text{curr}_a.\text{val} = 2$:
  - Set $\text{curr}_{\text{res}}.\text{next} = 1$.
  - Set $\text{curr}_{\text{res}} = \text{curr}_{\text{res}}.\text{next} = 1$.
  - Set $\text{curr}_b = \text{curr}_b.\text{next} = 3$.
- Iteration 3. Since $\text{curr}_a.\text{val} = 2 \le \text{curr}_b.\text{val} = 3$:
  - Set $\text{curr}_{\text{res}}.\text{next} = 2$.
  - Set $\text{curr}_{\text{res}} = \text{curr}_{\text{res}}.\text{next} = 2$.
  - Set $\text{curr}_a = \text{curr}_a.\text{next} = 4$.
- Iteration 4. Since $\text{curr}_b.\text{val} = 4 \le \text{curr}_a.\text{val} = 4$:
  - Set $\text{curr}_{\text{res}}.\text{next} = 4$.
  - Set $\text{curr}_{\text{res}} = \text{curr}_{\text{res}}.\text{next} = 4$.
  - Set $\text{curr}_a = \text{curr}_a.\text{next} = \text{None}$.
- Since $\text{curr}_a$ is `None`, set $\text{curr}_{\text{res}}.\text{next} = \text{curr}_b = 4$.
- Set $\text{result} = \text{result}.\text{next} = 1$
- Return $\text{result}$.

$\text{result}$ at the end:

$$1 \rightarrow 1  \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 4 \rightarrow \text{None}$$

### Time Complexity

In the worst-case, neither of the lists will run out first and both the lists will be processed till the end. Thus, the time-complexity is $\mathcal{O}(m+n)$.
