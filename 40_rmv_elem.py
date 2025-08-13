def removeElement(nums, val):
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1

    return j

print(removeElement([3, 2, 2, 3], 3))  # Output: 2
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))  # Output: 5