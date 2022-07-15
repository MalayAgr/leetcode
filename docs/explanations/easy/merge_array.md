---
layout: default
parent: Easy Problems
grand_parent: Explanations
has_toc: false
nav_order: 17
---

# <!-- omit in toc --> Problem 17 - Merge Sorted Array

> Leetcode Link: [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array).

- [Statement](#statement)
- [Examples](#examples)
- [Solution 1 - Use Binary Search](#solution-1---use-binary-search)
  - [Concept](#concept)
  - [Example](#example)
  - [Time complexity](#time-complexity)
- [Solution 2 - Use a Dictionary and the Merge Procedure from Merge Sort](#solution-2---use-a-dictionary-and-the-merge-procedure-from-merge-sort)
  - [Concept](#concept-1)
  - [Example](#example-1)
  - [Time complexity](#time-complexity-1)
- [Solution 3 - Merge in Reverse Order](#solution-3---merge-in-reverse-order)
  - [Concept](#concept-2)
  - [Example](#example-2)
  - [Time complexity](#time-complexity-2)

## Statement

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

## Examples

```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
```

```
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
```

## Solution 1 - Use Binary Search

### Concept

Initialize $$\text{high}$$ to $$m - 1$$.

For each element $$b$$ in $$\text{nums}_2$$:

- Find the index $$i$$ where $$b$$ should be inserted into $$\text{nums}_1$$ using binary search with $$\text{low} = 0$$ and $$\text{high}=\text{high}$$
- For $$j=\text{high},\text{high} - 1, \dots, i$$, shift $$\text{nums}_1[j]$$ to $$\text{nums}_1[j + 1]$$
- Insert $$b$$ at $$\text{nums}_1[i]$$
- Increment $$\text{high}$$ by $$1$$ since one more element has been added into $$\text{nums}_1$$

### Example

**Input**

```
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
```

**Procedure**

- \$$\text{high} = 3 - 1 = 2$$
- Iteration 1:
  - \$$b = 2$$
  - After binary search, $$i = 1$$
  - After shifting, $$\text{nums}_1 = [1, 2, 2, 3, 0, 0]$$
  - Set $$\text{nums}_1[1] = 2$$ so that $$\text{nums}_1 = [1, 2, 2, 3, 0, 0]$$
  - \$$\text{high} = 2 + 1 = 3$$
- Iteration 2:
  - \$$b = 5$$
  - After binary search, $$i = 4$$
  - No shifting will occur since $$i \gt \text{high}$$
  - Set $$\text{nums}_1[4] = 5$$ so that $$\text{nums}_1 = [1, 2, 2, 3, 5, 0]$$
  - \$$\text{high} = 3 + 1 = 4$$
- Iteration 3:
  - \$$b = 6$$
  - After binary search, $$i = 5$$
  - No shifting will occur since $$i \gt \text{high}$$
  - Set $$\text{nums}_1[5] = 6$$ so that $$\text{nums}_1 = [1, 2, 2, 3, 5, 6]$$
  - \$$\text{high} = 4 + 1 = 5$$
- Since there are no more elements in $$\text{nums}_2$$, end

At the end, $$\text{nums}_1 = [1, 2, 2, 3, 5, 6]$$.

### Time complexity

For each element in $$\text{nums}_2$$, there is one call to binary search and then a rightward shift of elements in $$\text{nums}_1$$. Thus, the time complexity is $$\mathcal{O}(m*n*\log{} m)$$.

## Solution 2 - Use a Dictionary and the Merge Procedure from Merge Sort

### Concept

If $$m + n = 0$$, do nothing and return.

Otherwise, create a dictionary which maps indices to values for $$\text{nums}_1$$. Let this dictionary be $$M$$.

Initialize $$i$$, $$j$$ and $$k$$ to $$0$$.

While $$i \not = m$$ and $$j \not = n$$:

- If $$M[i] \le \text{nums}_2[j]$$:
  - Set $$\text{nums}_1[k]$$ to $$M[i]$$
  - Increment $$i$$ by $$1$$
- Otherwise:
  - Set $$\text{nums}_1[k]$$ to $$\text{nums}_2[j]$$
  - Increment $$j$$ by $$1$$
- Increment $$k$$ by $$1$$

If $$i = m$$, let $$\text{left} = \text{nums}_2$$ and $$\text{idx} = j$$. Otherwise, let $$\text{left} = M$$ and $$\text{idx} = i$$.

While $$k \lt m + n$$:

- Set $$\text{nums}_1[k]$$ to $$\text{left}[\text{idx}]$$
- Increment $$\text{idx}$$ by $$1$$
- Increment $$k$$ by $$1$$

### Example

**Input**

```
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
```

**Procedure**

```python
M = {
  0: 1,
  1: 2,
  2: 3,
}
```

- \$$i = j = k = 0$$
- Iteration 1 - Since $$M[0] \le \text{nums}_2[0]$$:
  - Set $$\text{nums}_1[0]$$ to $$M[0] = 1$$ so that $$\text{nums}_1 = [1, 2, 3, 0, 0, 0]$$
  - \$$i = 0 + 1 = 1$$
  - \$$k = 0 + 1 = 1$$
- Iteration 2 - Since $$M[1] \le \text{nums}_2[0]$$:
  - Set $$\text{nums}_1[1]$$ to $$M[1] = 2$$ so that $$\text{nums}_1 = [1, 2, 3, 0, 0, 0]$$
  - \$$i = 1 + 1 = 2$$
  - \$$k = 1 + 1 = 2$$
- Iteration 3 - Since $$\text{nums}_2[0] \lt  M[2]$$:
  - Set $$\text{nums}_1[2]$$ to $$\text{nums}_2[0] = 2$$ so that $$\text{nums}_1 = [1, 2, 2, 0, 0, 0]$$
  - \$$j = 0 + 1 = 1$$
  - \$$k = 2 + 1 = 3$$
- Iteration 4 - Since $$M[2] \le \text{nums}_2[1]$$:
  - Set $$\text{nums}_1[3]$$ to $$M[2] = 3$$ so that $$\text{nums}_1 = [1, 2, 2, 3, 0, 0]$$
  - \$$i = 2 + 1 = 3$$
  - \$$k = 3 + 1 = 4$$
- Since $$i = 3$$, $$\text{left} = \text{nums}_2$$ and $$\text{idx} = j = 1$$
- After the second loop, $$\text{nums}_1 = [1, 2, 2, 3, 5, 6]$$

At the end, $$\text{nums}_1 = [1, 2, 2, 3, 5, 6]$$.

### Time complexity

The time complexity is similar to the merge procedure in merge sort. That is, the time complexity is $$\mathcal{O}(m + n)$$.

It takes $$\mathcal{O}(m)$$ amount of extra space.

## Solution 3 - Merge in Reverse Order

### Concept

> **Note**: This solution uses the negative indexing feature of Python. It requires only small changes to work in other languages.

If $$m + n = 0$$, do nothing and return.

Initialize $$j$$ to $$-1$$. This is always equal to the last index in $$\text{nums}_1$$ from the end where an element should be placed.

Initialize $$i_1$$ to $$m$$ and $$i_2$$ to $$n$$. These are always equal to one more than the index of the current candidate elements in $$\text{nums}_1$$ and $$\text{nums}_2$$ that should be considered for placement in $$\text{nums}_1$$ respectively.

While $$i_1 \gt 0$$ and $$i_2 \gt 0$$:

- Let $$a = \text{nums}_1[i_1 - 1]$$ and $$b = \text{nums}_2[i_2 - 1]$$
- If $$a \ge b$$:
  - Set $$\text{nums}_1[j]$$ to $$\text{nums}_1[i_1 - 1]$$
  - Decrement $$i_1$$ by $$1$$
- Otherwise:
  - Set $$\text{nums}_1[j]$$ to $$\text{nums}_2[i_2 - 1]$$
  - Decrement $$i_2$$ by $$1$$
- Decrement $$j$$ by $$1$$

While $$i_2 \gt 0$$:

- Set $$\text{nums}_1[j]$$ to $$\text{nums}_2[i_2 - 1]$$
- Decrement $$i_2$$ by $$1$$
- Decrement $$j$$ by $$1$$

### Example

**Input**

```
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
```

**Procedure**

- \$$j = -1$$
- $$i_1 = 3$$, $$i_2 = 3$$
- Iteration 1:
  - $$a = 3$$, $$b = 6$$
  - Since $$b \gt a$$:
    - Set $$\text{nums}_1[-1]$$ to $$6$$ so that $$\text{nums}_1 = [1, 2, 3, 0, 0, 6]$$
    - \$$i_2 = 3 - 1 = 2$$
  - \$$j = -1 - 1 = -2$$
- Iteration 2:
  - $$a = 3$$, $$b = 5$$
  - Since $$b \gt a$$:
    - Set $$\text{nums}_1[-2]$$ to $$5$$ so that $$\text{nums}_1 = [1, 2, 3, 0, 5, 6]$$
    - \$$i_2 = 2 - 1 = 1$$
  - \$$j = -2 - 1 = -3$$
- Iteration 3:
  - $$a = 3$$, $$b = 2$$
  - Since $$a \ge b$$:
    - Set $$\text{nums}_1[-3]$$ to $$3$$ so that $$\text{nums}_1 = [1, 2, 3, 3, 5, 6]$$
    - \$$i_1 = 3 - 1 = 2$$
  - \$$j = -3 - 1 = -4$$
- Iteration 4:
  - $$a = 2$$, $$b = 2$$
  - Since $$a \ge b$$:
    - Set $$\text{nums}_1[-4]$$ to $$2$$ so that $$\text{nums}_1 = [1, 2, 2, 3, 5, 6]$$
    - \$$i_1 = 2 - 1 = 1$$
  - \$$j = -4 - 1 = -5$$
- Iteration 5:
  - $$a = 1$$, $$b = 2$$
  - Since $$b \gt a$$:
    - Set $$\text{nums}_1[-5]$$ to $$2$$ so that $$\text{nums}_1 = [1, 2, 2, 3, 5, 6]$$
    - \$$i_2 = 1 - 1 = 0$$
  - \$$j = -5 - 1 = -6$$
- Since $$i_2 = 0$$, stop

At the end, $$\text{nums}_1 = [1, 2, 2, 3, 5, 6]$$.

### Time complexity

Since each element of $$\text{nums}_1$$ and $$\text{nums}_2$$ is processed once in the worst-case, the time complexity is $$\mathcal{O}(m + n)$$.
