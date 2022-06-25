def remove_duplicates_sol1(nums: list[int]) -> int:
    curr = nums[0]
    count = 0
    k = 1

    for i in range(1, len(nums)):
        val = nums[i]

        if val == curr:
            count += 1
            continue

        nums[i - count + 1 : i + 1] = nums[i - count : i]
        nums[i - count] = val
        curr = val
        k += 1

    return k


def remove_duplicates_sol2(nums: list[int]) -> int:
    curr = nums[0]
    k = 1
    count = 0

    for i in range(1, len(nums)):
        val = nums[i]

        if val == curr:
            count += 1
            continue

        nums[i - count] = val
        curr = val
        k += 1

    return k


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 3, 3, 4, 5, 5, 6]

    print(remove_duplicates_sol1(nums=nums))
    print(nums)

    print(remove_duplicates_sol2(nums=nums))
    print(nums)
