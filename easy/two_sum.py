"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Examples:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]


Solution 1:

    Sort the array but store the indices in the correct order instead of the elements.
    For each index in this sorted array, get the element a at the index and calculate
    The second element as b = target - a. Perform a binary search on the array to find b,
    Returning the index if found.

    Time Complexity:
    O(nlogn)

Solution 2:

    Initialize an empty dictionary which will store a mapping from value to index.
    For each value a in the array, calculate the second element as b = target - a.
    If the value exists in the dictionary, return the idex of a and the index of b.
    Either way, store the index of a in the dictionary.

    Time Complexity:
    O(n)
"""


def binary_search(
    indices: list[int],
    nums: list[int],
    key: int,
    low: int,
    high: int,
    a_idx: int,
) -> int:
    while high >= low:
        mid = (high + low) // 2
        mid_idx = indices[mid]

        if mid_idx != a_idx and nums[mid_idx] == key:
            return mid_idx

        if nums[mid_idx] >= key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def two_sum_sol1(nums: list[int], target: int) -> list[int]:
    indices = sorted(range(len(nums)), key=lambda x: nums[x])

    high = len(nums) - 1

    for idx in indices:
        a = nums[idx]
        b = target - a
        b_idx = binary_search(indices, nums, key=b, low=0, high=high, a_idx=idx)
        if b_idx != -1:
            return [idx, b_idx]


def two_sum_sol2(nums: list[int], target: int) -> list[int]:
    idx_map = {}

    for idx, num in enumerate(nums):
        b = target - num
        if b in idx_map:
            return [idx, idx_map[b]]
        idx_map[num] = idx


if __name__ == "__main__":
    nums = [0, 3, -3, 4, -1]
    target = -1
    result = two_sum_sol1(nums=nums, target=target)

    print(result)

    result = two_sum_sol2(nums=nums, target=target)

    print(result)
