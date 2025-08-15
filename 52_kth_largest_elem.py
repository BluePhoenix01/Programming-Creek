def findKthLargest(nums, k):
    if not nums or k < 1 or k > len(nums):
        return None
    nums.sort()
    return nums[-k]

# QuickSelect Approach
def findKthLargestQS(nums, k):
    return

print(findKthLargest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
print(findKthLargest([3, 2, 1, 5, 6, 4], 6))  # Output: 1