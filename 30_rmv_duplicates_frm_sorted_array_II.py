def removeDuplicates2(nums):
    j = 0
    count = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j] and count >= 1:
            j += 2
            nums[j] = nums[i]
            count = 0
        count += 1

    return nums[: j + 1], j + 1


def removeDuplicates2Better(nums):
    if not nums:
        return 0
    j = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[j - 2]:
            nums[j] = nums[i]
            j += 1
    return nums[:j], j


# print(removeDuplicates2([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
# print(removeDuplicates2([1, 1, 1, 2, 2, 3]))
# print(removeDuplicates2([1, 1, 2, 2, 2, 3]))

print(removeDuplicates2Better([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(removeDuplicates2Better([1, 1, 1, 2, 2, 3]))
print(removeDuplicates2Better([1, 1, 2, 2, 2, 3]))