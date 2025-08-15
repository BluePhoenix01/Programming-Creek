def largestNum(nums):
    if not nums:
        return "0"
    nums = [str(num) for num in nums]
    nums.sort(reverse=True)
    right = 1
 
    while right < len(nums):
        while int(nums[right - 1] + nums[right]) < int(nums[right] + nums[right - 1]):
            nums[right - 1], nums[right] = nums[right], nums[right - 1]
            right -= 1
        right += 1    
    max_num = ''.join(nums)
    return max_num
def largestNumLambda(nums):
    return (lambda nums: ''.join(sorted(map(str, nums), key=lambda x: x*10, reverse=True)))(nums)

print(largestNum([30, 3, 30, 34, 5, 9]))  # Output: "9534330"
