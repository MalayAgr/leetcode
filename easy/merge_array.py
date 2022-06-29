import itertools


def binary_search(nums, key, low, high):
    while high >= low:
        mid = (high + low) // 2

        if nums[mid] == key:
            return mid

        if key > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return high + 1


def merge_sol1(nums1, m, nums2, n):
    high = m - 1
    for num in nums2:
        idx = binary_search(nums1, key=num, low=0, high=high)
        i = high
        while i >= idx:
            nums1[i + 1] = nums1[i]
            i -= 1

        nums1[idx] = num

        high += 1


def merge_sol2(nums1, m, nums2, n):
    if m + n == 0:
        return

    idx_map = {idx: val for idx, val in enumerate(itertools.islice(nums1, None, m))}

    i = j = k = 0

    while i != m and j != n:
        value = idx_map[i]

        if value <= nums2[j]:
            nums1[k] = value
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1

        k += 1

    left, idx = (nums2, j) if i == m else (idx_map, i)

    while k < m + n:
        nums1[k] = left[idx]
        idx += 1
        k += 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    merge_sol1(nums1=nums1, m=m, nums2=nums2, n=n)
    print(nums1)

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    merge_sol2(nums1=nums1, m=m, nums2=nums2, n=n)
    print(nums1)
