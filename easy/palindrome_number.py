"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Examples:

    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
                 Therefore it is not a palindrome.

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Solution 1:

    Convert the number to a string and compare the reverse.

Solution 2:
    If the number is negative, return False since it cannot be a palindrome.
    Initialize reverse as 0, which will hold the final reversed number.
    Create a copy of the number and do the following:
    1. Find the remainder when it is divided by 10.
    2. Update reverse as reverse * 10 + remainder
    3. Update the number as number // 10 so that there is one less digit.
    Repeat this until the number becomes 0.
    Return the result of number == reverse.

    Example:
    Let number be 121.
    reverse = 0
    Step 1:
        - Remainder = 121 % 10 = 1
        - Reverse = 0 * 10 + 1 = 1
        - Number = 121 // 10 = 12
    Step 2:
        - Remainder = 12 % 10 = 2
        - Reverse = 1 * 10 + 2 = 12
        - Number = 12 // 10 = 1
    Step 3:
        - Remainder = 
"""


def palindrome_number_sol1(x: int) -> bool:
    x = str(x)
    return x == x[::-1]


def palindrome_number_sol2(x: int) -> bool:
    if x < 0:
        return False

    temp_x, reverse = x, 0

    while temp_x != 0:
        reverse = reverse * 10 + temp_x % 10
        temp_x = temp_x // 10

    return x == reverse


if __name__ == "__main__":
    x = 121

    result = palindrome_number_sol1(x)
    print(result)

    result = palindrome_number_sol2(x)
    print(result)
