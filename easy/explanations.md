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
    - [Time Complexity](#time-complexity-1)
- [Problem 2 - Palindrome Number](#problem-2---palindrome-number)
  - [Statement](#statement-1)
  - [Examples](#examples-1)
  - [Solution 1 - Convert Number to a String](#solution-1---convert-number-to-a-string)
    - [Concept](#concept-2)
    - [Example](#example-2)
    - [Time Complexity](#time-complexity-2)
  - [Solution 2 - Construct Reverse Using Mod 10](#solution-2---construct-reverse-using-mod-10)
    - [Concept](#concept-3)
    - [Example](#example-3)
    - [Time Complexity](#time-complexity-3)

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

For each element $a$ in the array, calculate $b=target-a$. Check if $b$ exists in the dictionary and if it does, return the index of $a$ and $b$.

Otherwise, add $a$ with its index to the dictionary.

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

#### Time Complexity

Since this is a simple loop over the entire array, the time complexity is $\mathcal{O}(n)$.

## Problem 2 - Palindrome Number

### Statement

Given an integer `x`, return true if `x` is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

### Examples

```block
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

```block
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

```block
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

### Solution 1 - Convert Number to a String

#### Concept

Convert number to a string and compare it with its reverse.

#### Example

**Input**

```block
x = 121
```

**Procedure**

- Use `str()` to convert `121` to a string.
- Compare `'121'` with `'121'` and return the result.

#### Time Complexity

Since the number is converted to a string and then reversed, the time complexity is $\mathcal{O}(k)$, where $k$ is the number of digits in the number.

### Solution 2 - Construct Reverse Using Mod 10

#### Concept

> **Assertion 1**: If a number is divided by $10$, the remainder is the last digit of the number. Example: $134\bmod10=4$.
>
> **Assertion 2**: If a number is divided by $10$, the quotient is the number formed by all digits of the number except the last one. Example: $134\div10=13$.
>
> **Assertion 3**. Consider a number $d_1d_2...d_n$, where $d_i$ is a digit of the number. If the reverse of the number so far is $d_nd_{n-1}...d_{i+1}$ and the current digit from the right is $d_i$, then the new reverse is $d_nd_{n-1}...d_{i+1}*10+d_i$.

If $x$ negative, return `False` since no negative number can be a palindrome due to the negative sign.

Otherwise, initialize $reverse$ as $0$ to store the reverse of $x$. Create a copy of $x$ and do the following using the copy:

1. Get the remainder when $x$ is divided by $10$. This will give the last digit of the number.
2. Update the reverse so that the last digit will be in the correct position. This is done as $reverse=reverse*10+remainder$.
3. Update $x$ by dividing it by $10$ so that the last digit is dropped.

Repeat this until the copy becomes $0$. At the end, $reverse$ will have the reverse of $x$.

Return the result of $reverse==x$.

#### Example

**Input**

```block
x = 121
```

**Procedure**

- `reverse = 0` and `temp_x = x = 121`.
- Iteration 1:
  - `remainder = 121 % 10 = 1`
  - `reverse = 0 * 10 + 1 = 1`
  - `temp_x = 121 // 10 = 12`
- Iteration 2:
  - `remainder = 12 % 10 = 2`
  - `reverse = 1 * 10 + 2 = 12`
  - `temp_x = 12 // 10 = 1`
- Iteration 3:
  - `remainder = 1 % 10 = 1`
  - `reverse = 12 * 10 + 1 = 121`.
  - `temp_x = 1 // 10 = 0`
- Since `reverse = 121 = x`, return `True`.

#### Time Complexity

Since the reverse is built one digit at a time, the time complexity is $\mathcal{O}(k)$, where $k$ is the number of digits in the number.
