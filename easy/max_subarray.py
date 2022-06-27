def maximum_subarray(nums: list[int]) -> int:
    total = 0
    max_sum = nums[0]

    for num in nums:
        total += num

        max_sum = max(total, max_sum)

        total = max(total, 0)

    return max_sum
