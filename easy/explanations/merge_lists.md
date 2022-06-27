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

Copy the heads of the two lists. Let these copies be $curr_a$ and $curr_b$ respectively.

If $curr_a$ has no elements, return $curr_b$.

Otherwise, create a new linked list $result$ with a dummy head node with any random value.

Copy the head of $result$. Let the copy be $curr_{res}$.

Until either $curr_a$ or $curr_b$ reach the end of their respective lists, do the following:

- If $curr_a.val \le curr_b.val$:
  - Set $curr_{res}.next$ to $curr_a$
  - Advance $curr_{res}$ to $curr_{res}.next$
  - Advance $curr_a$ to $curr_a.next$.
- Otherwise:
  - Set $curr_{res}.next$ to $curr_b$
  - Advance $curr_{res}$ to $curr_{res}.next$
  - Advance $curr_b$ to $curr_b.next$.

Set $curr_{res}.next$ to either $curr_a$ or $curr_b$, whichever hasn't reached the end of its list.

Since the first node in $result$ is a dummy head node, advance $result$ to $result.next$ so that it is at the correct head node.

Return $result$.

### Examples

> **Note**: Each number here is actually a `ListNode` with `val` set to the number and `next` set to a `ListNode` with the next number.

**Input**

```block
list1 = [1,2,4], list2 = [1,3,4]
```

**Procedure**

- `curr_a = 1` and `curr_b = 1`.
- Since neither is `None`, continue.
- `result = -1` and `curr_res = -1`.
- Iteration 1. Since `curr_a.val = 1 <= curr_b.val = 1`:
  - Set `curr_res.next = 1`.
  - Set `curr_res = curr_res.next = 1`.
  - Set `curr_a = curr_a.next = 2`.
- Iteration 2. Since `curr_b.val = 1 <= curr_a.val = 2`:
  - Set `curr_res.next = 1`.
  - Set `curr_res = curr_res.next = 1`.
  - Set `curr_b = curr_b.next = 3`.
- Iteration 3. Since `curr_a.val = 2 <= curr_b.val = 3`:
  - Set `curr_res.next = 2`.
  - Set `curr_res = curr_res.next = 2`.
  - Set `curr_a = curr_a.next = 4`.
- Iteration 4. Since `curr_b.val = 4 <= curr_a.val = 4`:
  - Set `curr_res.next = 4`.
  - Set `curr_res = curr_res.next = 4`.
  - Set `curr_a = curr_a.next = None`.
- Since `curr_a` is `None`, set `curr_res.next = curr_b = 4`.
- Set `result = result.next = 1`
- Return `result`.

### Time Complexity

In the worst-case, neither of the lists will run out first and both the lists will be processed till the end. Thus, the time-complexity is $\mathcal{O}(m+n)$.
