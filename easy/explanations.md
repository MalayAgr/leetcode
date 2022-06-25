# <!-- omit in toc --> Explanations

- [Problem 1: Two Sum](#problem-1-two-sum)
  - [Statement](#statement)
  - [Examples](#examples)
  - [Solution 1 - Use Binary Search](#solution-1---use-binary-search)
    - [Concept](#concept)
    - [Implementation details](#implementation-details)
    - [Example](#example)
    - [Time Complexity](#time-complexity)
  - [Solution 2 - Use a hash map or dictionary](#solution-2---use-a-hash-map-or-dictionary)
    - [Concept](#concept-1)
    - [Implementation details](#implementation-details-1)
    - [Example](#example-1)
    - [Time complexity](#time-complexity-1)

## Problem 1: Two Sum

### Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Examples

```block
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation*: Because nums[0] + nums[1] == 9, we return [0, 1].
```

```block
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

```block
Input: nums = [3,3], target = 6
Output: [0,1]
```

### Solution 1 - Use Binary Search

#### Concept

> All problems in computer science can be solved by another level of indirection.

Sort the array but store the indices in the correct order instead of the elements themselves.

For each index in the array, use the index to get the element at that index. Let this element be $a$.

Calculate the complement of $a$ as $b=target-a$ since $target=a+b$. Use binary search on the sorted indices to find $b$. If found, return its index with the index of $a$.

#### Implementation details

The statement states that we cannot use the same element twice. Therefore, the loop in binary search is implemented as follows:

```python
mid = (high + low) // 2
mid_idx = indices[mid]

if mid_idx != a_idx and nums[mid_idx] == b:
    return mid_idx

if nums[mid_idx] >= b:
    high = mid - 1
else:
    low = mid + 1
```

#### Example

**Input**:

```block
nums = [2, 7, 11, 5]
target = 9
```

**Procedure**

- Sorted indices: `[0, 3, 1, 2]`
- Iteration 1:
  - `idx = 0`
  - `a = nums[0] = 2`
  - `b = 9 - 2 = 7`
  - Binary search with `low = 0`, `high = 3` and `a_idx = 2`:
    - Iteration 1:
      - `mid = 1`
      - `mid_idx = indices[1] = 3`
      - Since `nums[mid_idx] = 5 < 7`, `low = mid + 1 = 2`
    - Iteration 2:
      - `mid = 2`
      - `mid_idx = indices[2] = 1`
      - Since `a_idx != 1 and nums[mid_idx] = 7 = 7`, return `1`
  - Return `[0, 1]`.
- End

#### Time Complexity

Python sorting is $\mathcal{O}(n\log{}n)$.

Each iteration of the for loop is $\mathcal{O}(\log{}n)$ and the loop runs $n$ times in the worst case.

Thus, the total complexity is $\mathcal{O}(n\log{}n)$.

### Solution 2 - Use a hash map or dictionary

#### Concept

Initialize an empty dictionary which will map elements of the array to their index.

For each element $a$ in the array, calculate $b=target-a$. Check if $b$ exists in the array and if it does, return the index of $a$ and $b$.

Either way, add $a$ with its index to the dictionary.

#### Implementation details

Since an element cannot be reused, the dictionary starts out as empty and the check for $b$ is performed before $a$ is added.

#### Example

**Input**:

```block
nums = [2, 7, 11, 5]
target = 9
```

**Procedure**

- Dictionary = `{}`
- Iteration 1:
  - `a = 2`
  - `b = 9 - 2 = 7`
  - `b` is not in dictionary
  - Dictionary = `{2: 0}`.
- Iteration 2:
  - `a = 7`
  - `b = 9 - 7 = 2`
  - `b` is in the dictionary
  - Return `[1, 0]`.
- End

#### Time complexity

Since this is a simple loop over the entire array, the time complexity is $\mathcal{O}(n)$.
