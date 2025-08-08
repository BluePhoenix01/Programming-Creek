class TwoSum(object):
    nums: list = [] 
    target = 0
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target    
    def twoSum(self):
        num_map = {}
        for i in range(len(self.nums)):
            complement = self.target - self.nums[i]
            if complement in num_map:
                return [num_map[complement], i]
            num_map[self.nums[i]] = i