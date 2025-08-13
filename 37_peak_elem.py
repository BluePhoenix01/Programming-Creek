def findPeakElement(nums):
    if not nums:
        return None
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i
    if nums[0] > nums[-1]:
        return 0
    return len(nums) - 1

print(findPeakElement([1, 2, 3, 1]))
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print(findPeakElement([1, 2, 3, 4, 5, 6, 7]))