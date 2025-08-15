def searchRangeSeparate(nums, target):
    def findLeftIndex(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def findRightIndex(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left_index = findLeftIndex(nums, target)
    right_index = findRightIndex(nums, target)

    if left_index <= right_index:
        return (left_index, right_index)
    else:
        return (-1, -1)
    
def searchRange(nums, target):
    def findBound(is_left):
        lo, hi = 0, len(nums) - 1
        bound = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                bound = mid
                if is_left:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return bound

    left = findBound(is_left=True)
    if left == -1:
        return [-1, -1]
    right = findBound(is_left=False)
    return [left, right]
    
print(searchRange([5, 7, 7, 8, 8, 10], 8))  # Output: (3, 4)
print(searchRange([5, 7, 7, 8, 8, 10], 6))  # Output: (-1, -1)