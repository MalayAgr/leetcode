# <!-- omit in toc --> Problem 6 - Remove Duplicates from Sorted Array

> Leetcode Link: [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/).

- [Statement](#statement)
- [Examples](#examples)
- [Solution - Use Consecutive Nature of Duplicates](#solution---use-consecutive-nature-of-duplicates)
  - [Concept](#concept)
  - [Example](#example)
  - [Time Complexity](#time-complexity)

## Statement

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with $\mathcal{O}(1)$ extra memory.

## Examples

```block
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

```block
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

## Solution - Use Consecutive Nature of Duplicates

### Concept

> **Assertion**: In a sorted array, duplicates of a number will be consecutive.

Set $curr$ to the first element of $nums$. Initialize $count$ to $0$. It will keep track of the total number of duplicates in $nums$.

Initialize $k$, the return value, to $1$.

For each index $1 \le i \lt len(array)$:

- Get the value $val$ at index $i$.
- If the $val == curr$, increment $count$ by $1$ since a duplicate has been encountered and continue.
- Otherwise, the value is not equal to $curr$:
  - Set $nums[i-count]$ to $val$, thus "moving" the non-duplicate to the position immediately after the first index where $curr$ is present.
  - Change $curr$ to $val$.
  - Increment $k$ by $1$ since a non-duplicate has been found.

Finally, return $k$.

### Example

**Input**

```block
nums = [0,0,1,1,1,2,2,3,3,4]
```

**Procedure**

- `curr = nums[0] = 0`, `count = 0`, `k = 1`
- Iteration 1:
  - `i = 1`.
  - `val = nums[1] = 0`.
  - Since `val == curr`, `count = 0 + 1 = 1`.
- Iteration 2:
  - `i = 2`
  - `val = nums[2] = 1`
  - Since `val != curr`:
    - `nums[i - count] = nums[1] = 1` so that `nums = [0, 1, 1, 1, 1, 2, 2, 3, 3]`.
    - `curr = 1`.
    - `k = 1 + 1 = 2`.
- Iteration 3:
  - `i = 3`
  - `val = nums[3] = 1`
  - Since `val == curr`, `count = 1 + 1 = 2`.
- Iteration 4:
  - `i = 4`
  - `val = nums[4] = 1`
  - Since `val == curr`, `count = 2 + 1 = 3`.
- Iteration 5:
  - `i = 5`
  - `val = nums[5] = 2`
  - Since `val != curr`:
    - `nums[i - count] = nums[2] = 2` so that `nums = [0, 1, 2, 1, 1, 2, 2, 3, 3]`.
    - `curr = 2`.
    - `k = 2 + 1 = 3`.
- Iteration 6:
  - `i = 6`
  - `val = nums[6] = 2`
  - Since `val == curr`, `count = 3 + 1 = 4`.
- Iteration 7:
  - `i = 7`
  - `val = nums[7] = 3`
  - Since `val != curr`:
    - `nums[i - count] = nums[3] = 3` so that `nums = [0, 1, 2, 3, 1, 2, 2, 3, 3]`.
    - `curr = 3`.
    - `k = 3 + 1 = 4`.
- Iteration 8:
  - `i = 8`
  - `val = nums[8] = 3`
  - Since `val == curr`, `count = 4 + 1 = 5`.
- Iteration 9:
  - `i = 9`
  - `val = nums[9] = 4`
  - Since `val != curr`:
    - `nums[i - count] = nums[4] = 4` so that `nums = [0, 1, 2, 3, 4, 2, 2, 3, 3]`.
    - `curr = 4`.
    - `k = 4 + 1 = 5`.
- Return `k = 5`.

At the end, `nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]`.

### Time Complexity

The loop goes over each element of $nums$. Thus, the time complexity is $\mathcal{O}(n)$.
