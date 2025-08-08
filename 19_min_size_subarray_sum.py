def minSubArrayLen(target, nums):
    if not nums:
        return 0
    left = 0
    current_sum = nums[0]
    min_length = len(nums) + 1
    
    for j in range(len(nums)):
        print(f"i: {left}, j: {j}, current_sum: {current_sum}, min_length: {min_length}")
        if j > 0:
            current_sum += nums[j]
        
        while current_sum >= target:
            min_length = min(min_length, j - left + 1)
            current_sum -= nums[left]
            left += 1
            print(f"Updated i: {left}, j: {j}, current_sum: {current_sum}, min_length: {min_length}")
        print(f"End of iteration i: {left}, j: {j}, current_sum: {current_sum}, min_length: {min_length}")
    return min_length if min_length < len(nums) else 0

print(minSubArrayLen(7, [2,3,1,2,4,3]))  # Output: 2