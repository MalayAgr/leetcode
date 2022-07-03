---
layout: default
parent: Easy Problems
grand_parent: Explanations
has_toc: false
---
# <!-- omit in toc --> Problem 8 - Remove Element

- [Statement](#statement)
- [Examples](#examples)
- [Solution - Adapt the Partition Function Used in Quicksort](#solution---adapt-the-partition-function-used-in-quicksort)
  - [Concept](#concept)
  - [Example](#example)
  - [Time Complexity](#time-complexity)

## Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with $$O(1)$$ extra memory.

## Examples

```block
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

```block
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

## Solution - Adapt the Partition Function Used in Quicksort

### Concept

> The [partition function](https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme) in [quicksort](https://en.wikipedia.org/wiki/Quicksort) is a linear-time procedure used to partition an array $$a$$ around a pivot element $$a[q]$$ with the property that:
>
> > Each element in $$a[0...q]$$ is less than or equal to $$a[q]$$ and each element in $$a[q+1...n]$$ is greater than $$a[q]$$.
>
> Conventionally, $$a[q]$$ is chosen to be the last element in the array.
>
> After the partition step, $$a[q]$$ is at the position it would be in if the array were sorted.
>
> For example, if the array is $$[3, 6, 4, 2, 1, 5]$$, then after partitioning the array will be $$[3, 4, 2, 1, 5, 6]$$.
>
> This solution partitions the array around $$a[q]=\text{val}$$ such that:
>
> > Each element in $$a[0...q]$$ is not equal to $$a[q]$$ and each element in $$a[q+1...n]$$ is equal to $$a[q]$$.

If the last value in $$\text{nums}$$ is not $$\text{val}$$, find the first occurence of $$\text{val}$$ in $$\text{nums}$$ and exchange it with the last element.

Initialize an index variable $$i$$ to $$-1$$. It will always be the index of the last element in the left partition.

Initialize $$k$$, the return value, to $$0$$.

For each $$0 \le j \lt len(nums)-1$$:

- If $$\text{nums}[j]\not ={\text{val}}$$:
  - Increment $$i$$ by $$1$$, thus advancing the end of the left partition by $$1$$.
  - Increment $$k$$ by $$1$$ since a new value has been found.
  - Exchange $$\text{nums}[i]$$ and $$\text{nums}[j]$$ so that $$\text{nums}[j]$$ is the new last element in the left partition and $$\text{nums}[i]$$ goes to the right partition.

At the end, $$i + 1$$ is the position where the pivot should be be. So, exchange $$\text{nums}[i + 1]$$ and $$\text{nums}[-1]$$.

Return $$k$$.

### Example

**Input**

```block
nums = [0,1,2,2,3,0,4,2]
val = 2
```

**Procedure**

- Since $$\text{nums}[-1] = 2$$, no exchange is required
- $$i = -1$$, $$k = 0$$
- Iteration 1:
  - \$$j = 0$$
  - Since $$\text{nums}[0] = 0 \not = 2$$:
    - \$$i = -1 + 1 = 0$$
    - \$$k = 0 + 1 = 1$$
    - Exchange $$\text{nums}[0]$$ with $$\text{nums}[0]$$
    - Now, $$\text{nums} = [0, 1, 2, 2, 3, 0, 4, 2]$$
- Iteration 2:
  - \$$j = 1$$
  - Since $$\text{nums}[1] = 1 \not = 2$$:
    - \$$i = 0 + 1 = 1$$
    - \$$k = 1 + 1 = 2$$
    - Exchange $$\text{nums}[1]$$ with $$\text{nums}[1]$$
    - Now, $$\text{nums} = [0, 1, 2, 2, 3, 0, 4, 2]$$
- Iteration 3:
  - $$j = 2$$ and since $$\text{nums}[2] = 2$$, continue
- Iteration 4:
  - $$j = 3$$ and since $$\text{nums}[3] = 2$$, continue
- Iteration 5:
  - \$$j = 4$$
  - Since $$\text{nums}[4] = 3 \not = 2$$:
    - \$$i = 1 + 1 = 2$$
    - \$$k = 2 + 1 = 3$$
    - Exchange $$\text{nums}[2]$$ with $$\text{nums}[4]$$
    - Now, $$\text{nums} = [0, 1, 3, 2, 2, 0, 4, 2]$$
- Iteration 6:
  - \$$j = 5$$
  - Since $$\text{nums}[5] = 0 \not = 2$$:
    - \$$i = 2 + 1 = 3$$
    - \$$k = 3 + 1 = 4$$
    - Exchange $$\text{nums}[3]$$ with $$\text{nums}[5]$$
    - Now, $$\text{nums} = [0, 1, 3, 0, 2, 2, 4, 2]$$
- Iteration 7:
  - \$$j = 6$$
  - Since $$\text{nums}[6] = 4 \not = 2$$:
    - \$$i = 3 + 1 = 4$$
    - \$$k = 4 + 1 = 5$$
    - Exchange $$\text{nums}[4]$$ with $$\text{nums}[6]$$
    - Now, $$\text{nums} = [0, 1, 3, 0, 4, 2, 2, 2]$$
- Exchange $$\text{nums}[5]$$ with $$\text{nums}[-1]$$
- Return $$k = 5$$

At the end, $$\text{nums} = [0, 1, 3, 0, 4, 2, 2, 2]$$.

### Time Complexity

The solution loops over the entire array, giving a time complexity of $$\mathcal{O}(n)$$.
