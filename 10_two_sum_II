def twoSum2(nums, target):
    l , r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s < target:
            l += 1
        elif s > target:
            r -= 1
        else:
            return [l + 1, r + 1]

print(twoSum2([2, 7, 11, 15], 9))
print(twoSum2([3, 2, 4], 6))
print(twoSum2([3, 3], 6))