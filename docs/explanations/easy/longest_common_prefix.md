---
layout: default
parent: Easy Problems
grand_parent: Explanations
has_toc: false
---
# <!-- omit in toc --> Problem 4 - Longest Common Prefix

> Leetcode Link: [Longest Common Prefix](https://leetcode.com/submissions/detail/730808235/).

- [Statement](#statement)
- [Examples](#examples)
- [Solution 1 - Vertical Scanning](#solution-1---vertical-scanning)
  - [Concept](#concept)
  - [Implementation Details](#implementation-details)
  - [Example](#example)
  - [Time complexity](#time-complexity)
- [Solution 2 - Use a Trie](#solution-2---use-a-trie)
  - [Concept](#concept-1)
  - [Implementation Details](#implementation-details-1)
  - [Example](#example-1)
  - [Time complexity](#time-complexity-1)

## Statement

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Examples

```block
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

```block
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

## Solution 1 - Vertical Scanning

### Concept

> **Assertion**: If two or more strings have a common prefix, then they have the same character at the same index until the end of the of common prefix.

Let $$\text{first}$$ be the first string in $$\text{strs}$$.

For each character $$\text{first[i]}$$ in the first string and for each string $$\text{string}$$ in the remaining strings:

- If $$\text{string[i]} \not ={\text{first[i]}}$$, return $$\text{first}[:i]$$

If no return occurs in this loop, return $$\text{first}$$ since it is the longest common prefix.

### Implementation Details

It may be that a string in the remaining strings is smaller than the first string.

In this case, we do not need to compare any more strings since the longest common prefix cannot be longer than the length of the smallest string.

Thus, the actual return condition in the loop checks:

- Index of the current character is `>=` length of the current string or,
- The current character does not match the corresponding character in the current string.

```python
if idx >= len(string) or string[idx] != char:
```

If either are true, the algorithm can return.

### Example

**Input**

```block
strs = ["flower","flow","flight"]
```

**Procedure**

- \$$\text{first} = \text{flower}$$
- \$$\text{remaining} = [\text{flow}, \text{flight}]$$
- Iteration 1:
  - \$$i = 0$$
  - \$$\text{char} = f$$
  - Iteration 1:
    - \$$\text{string} = \text{flow}$$
    - Since $$i \lt len(\text{flow})$$ and $$\text{string}[0] = f$$, continue
  - Iteration 2:
    - \$$\text{string} = \text{flight}$$
    - Since $$i \lt len(\text{string})$$ and $$\text{string}[0] = f$$, continue
- Iteration 2:
  - \$$i = 1$$
  - \$$\text{char} = l$$
  - Iteration 1:
    - \$$\text{string} = \text{flow}$$
    - Since $$i \lt len(\text{flow})$$ and $$\text{string}[1] = l$$, continue
  - Iteration 2:
    - \$$\text{string} = \text{flight}$$
    - Since $$i \lt len(\text{string})$$ and $$\text{string}[1] = l$$, continue
- Iteration 3:
  - \$$i = 2$$
  - \$$\text{char} = o$$
  - Iteration 1:
    - \$$\text{string} = \text{flow}$$
    - Since $$i \lt len(\text{flow})$$ and $$\text{string}[2] = o$$, continue
  - Iteration 2:
    - \$$\text{string} = \text{flight}$$
    - Since $$i \lt len(\text{string})$$ but $$\text{string}[2] = i \not = {o}$$, return $$\text{first}[:2] = fl$$.

### Time complexity

The solution loops over each character in the first string and for each character, loops over the list of remaining strings.

In general, the time-complexity is $$\mathcal{O}(S)$$ where $$S$$ is the sum of lengths of all strings.

In the worst-case, all $$n$$ strings have the same length $$m$$, giving a complexity of $$\mathcal{O}(n*m).$$

In the best case, the time complexity is $$\mathcal{O}(n*m_{min})$$, where $$m_{min}$$ is the minimum length of a string.

## Solution 2 - Use a Trie

### Concept

> Note: To learn about the Trie data structure, see [Trie](https://en.wikipedia.org/wiki/Trie).

A trie node has the following structure:

```python
class Node:
    value: str | None
    is_leaf: bool
    children: dict[int, str]
```

Build a trie for the list of strings by inserting each string one by one in the trie using the standard trie insertion procedure ([source](https://en.wikipedia.org/wiki/Trie#Insertion)):

```python
def trie_insert(
    root: Node,
    key: str,
    value: str = None
):
    x = root

    for char in key:
        i = ord(char.lower()) - ord("a")
        if x.children[i] is None:
            x.children[i] = Node()
        x = x.children[i]

    x.value = value
    x.is_leaf = True
```

Let the trie be $$\text{trie}$$.

Initialize $$\text{prefix}$$ to an empty string. It will store the final prefix.

Starting at $$\text{node}=\text{trie}.\text{root}$$, while $$\text{node}$$ has a single child and is not a leaf node:

- Update $$\text{node}$$ so that it is now the only child
- Update $$\text{prefix}$$ as $$\text{prefix} = \text{prefix} + \text{node}.\text{value}$$

Return $$\text{prefix}$$.

### Implementation Details

When the `value` argument is not provided to the insertion procedure and the string being inserted is not empty, `x.value` at the end of the loop is set to the last character.

```python
def trie_insert(
    root: Node,
    key: str,
    value: str = None
):
    x = root

    for char in key:
        i = ord(char.lower()) - ord("a")
        if x.children[i] is None:
            x.children[i] = Node(value=char)
        x = x.children[i]

    if value is None and len(key) != 0:
        value = char

    x.value = value
    x.is_leaf = True
```

### Example

**Input**

```block
strs = ["flower","flow","flight"]
```

**Procedure**

- Build the trie. The filled in nodes represent leaf nodes. Let the trie be called `trie`.

![Example Trie]({{ site.baseurl }}/assets/imgs/example_trie.png)

- \$$\text{prefix} = \epsilon$$
- \$$\text{node} = \text{trie}.\text{root}$$
- Iteration 1:
  - Since $$\text{node}$$ has a single child and is not a leaf, change $$\text{node}$$ to the single child
  - \$$\text{prefix} = \epsilon + \text{node}.\text{value} = f$$
- Iteration 2:
  - Since $$\text{node}$$ has a single child and is not a leaf, change $$\text{node}$$ to the single child
  - \$$\text{prefix} = f + \text{node}.\text{value} = fl$$
- Since $$\text{node}$$ has more than one child, stop
- Return $$\text{prefix} = fl$$

### Time complexity

The trie can be built in time $$\mathcal{O}(S)$$, where $$S$$ is defined same as above.

In the worst-case, all $$n$$ strings are equal and have the same length $$m$$. Thus, $$S=n*m$$ and the trie will be traversed to a depth of $$m$$. This gives an overall worst-case time complexity of $$\mathcal{O}(n*m)$$.

The space complexity is $$O(S)$$.
