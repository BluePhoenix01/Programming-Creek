def findMinInRotatedSortedArrayII(nums):
    if not nums:
        return None
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return nums[i]
    return nums[0]

def findMinInRotatedSortedArrayBinarySearch(nums):
    if not nums:
        return None
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[right] == nums[left]:
            left += 1
        elif nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

def findMinInRotatedSortedArrayRecursive(nums):
    if not nums:
        return None
    return findMin(nums, 0, len(nums) - 1)

def findMin(nums, left, right):
    if left == right:
        return nums[left]
    mid = (left + right) // 2
    if nums[mid] > nums[right]:
        return findMin(nums, mid + 1, right)
    elif nums[mid] < nums[right]:
        return findMin(nums, left, mid)

    return findMin(nums, left + 1, right)

# print(findMinInRotatedSortedArray([3, 4, 5, 1, 2]))
# print(findMinInRotatedSortedArray([4, 5, 6, 7, 0, 1, 2])) # Output: 0

# print(findMinInRotatedSortedArrayBinarySearch([3, 4, 5, 1, 2]))
# print(findMinInRotatedSortedArrayBinarySearch([4, 4, 5, 6, 7, 0, 1, 2, 4])) # Output: 0

print(findMinInRotatedSortedArrayRecursive([3, 4, 5, 5, 1, 2, 3]))
print(findMinInRotatedSortedArrayRecursive([4, 5, 6, 7, 0, 0, 1, 2, 4])) # Output: 0