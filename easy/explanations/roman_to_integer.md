# <!-- omit in toc --> Problem 3: Roman to Integer

> Leetcode Link: [Roman to Integer](https://leetcode.com/problems/roman-to-integer/).

- [Statement](#statement)
- [Examples](#examples)
- [Solution - Simple loop](#solution---simple-loop)
  - [Concept](#concept)
  - [Example](#example)
  - [Time Complexity](#time-complexity)

## Statement

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

| Symbol | Value |
|---|---|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

`I` can be placed before `V` (`5`) and `X` (`10`) to make `4` and `9`.
`X` can be placed before `L` (`50`) and `C` (`100`) to make `40` and `90`.
`C` can be placed before `D` (`500`) and `M` (`1000`) to make `400` and `900`.

Given a roman numeral, convert it to an integer.

## Examples

```block
Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:
```

```block
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:
```

```block
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

## Solution - Simple loop

### Concept

Create two dictionatries. The first one maps a roman symbol to its numeric value. The second maps `I`, `X` and `C` to their respective pairs.

Create a variable to store the final result, initialized to $0$.

While an index varible `i` which is initialized to $0$ is less than the length of the roman numeral:

- Get the digit at index `i`.
- Get its value from the value map.
- Set a variable `increment` as 1.
- Check if the digit is in the second dictionary as a key.
  - If it is, check the next digit to see if it is in the corresponding pair.
    - If it is, set the value to the difference between the values of the two digits.
    - Change `increment` to 2.
- Add the value to the result.
- Increment `i` by `increment`.

Finally, return the result.

### Example

**Input**

```block
s = "MCMXCIV"
```

**Procedure**

Let the maps be called `VALUES` and `SUB_PAIRS`.

- Iteration 1:
  - `digit = s[0] = M`
  - `value = VALUES["M"] = 1000`, `increment = 1`
  - Since `M` is not in `SUB_PAIRS`, `result = 0 + 1000 = 1000`
  - `i = 0 + 1 = 1`
- Iteration 2:
  - `digit = s[1] = C`
  - `value = VALUES["C"] = 100`, `increment = 1`
  - Since `C` is in `SUB_PAIRS` and the next digit `M` is in the corresponding pair, `value = VALUES["M"] - 100 = 900`, `increment = 2`
  - `result = 1000 + 900 = 1900`
  - `i = 1 + 2 = 3`
- Iteration 3:
  - `digit = s[3] = X`
  - `value = VALUES["X"] = 10`, `increment = 1`
  - Since `X` is in `SUB_PAIRS` and the next digit `C` is in the corresponding pair, `value = VALUES["C"] - 10 = 90`, `increment = 2`
  - `result = 1900 + 90 = 1990`
  - `i = 3 + 2 = 5`
- Iteration 4:
  - `digit = s[5] = I`
  - `value = VALUES["I"] = 1`, `increment = 1`
  - Since `I` is in `SUB_PAIRS` and the next digit `V` is in the corresponding pair, `value = VALUES["V"] - 1 = 4`, `increment = 2`
  - `result = 1990 + 4 = 1994`
  - `i = 5 + 2 = 7`. This is not less than the length and hence loop ends.
- Return `result = 1994`.

### Time Complexity

Since there is a simple loop through the entire numeral, the time complexity is $\mathcal{O}(n)$.
