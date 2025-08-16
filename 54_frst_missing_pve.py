def firstMissingPositiveSet(nums):
    num_set = set(nums)
    i = 1
    while i in num_set:
        i += 1
    return i

def firstMissingPositive(nums):
    n = len(nums)

    # Place numbers in correct index if possible
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]  # swap
    # Scan for first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1

print(firstMissingPositive([3, 4, -1, 1]))  # Output: 2
print(firstMissingPositive([1, 2, 0]))      # Output: 3