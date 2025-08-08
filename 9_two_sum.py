def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
def twoSumHash(nums, target):
    num_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in num_map:
            return [num_map[complement], i]
        num_map[nums[i]] = i
    
print(twoSumHash([2, 7, 11, 15], 9))
print(twoSumHash([3, 2, 4], 6))
print(twoSumHash([3, 3], 6))