def containsDuplicate(nums, k):
    duplicateSet = {}

    for i in range(len(nums)):
        if nums[i] in duplicateSet and i - duplicateSet[nums[i]] <= k :
            return True
        duplicateSet[nums[i]] = i
    
    return False

print(containsDuplicate([1, 2, 3, 1], 3))  # True
print(containsDuplicate([1, 2, 3, 1], 2))  # False
print(containsDuplicate([1, 0, 1, 1], 1))  # True