def removeDuplicates(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
        
    return nums[:j+1], j+1

print(removeDuplicates([1, 1, 2]))  # Output: ([1, 2], 2)
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # Output: ([0, 1, 2, 3, 4], 5)