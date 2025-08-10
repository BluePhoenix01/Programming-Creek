def containsDuplicate(nums):
    duplicateSet = set()

    for num in nums:
        if num in duplicateSet:
            return True
        duplicateSet.add(num)
    
    return False

print(containsDuplicate([1, 2, 3, 1]))  # Output: True
print(containsDuplicate([1, 2, 3, 4]))  # Output: False