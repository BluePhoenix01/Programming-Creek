def sum3_closest(nums, target):
    nums.sort()
    diff = float('inf')
    min_set = []
    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1

        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if abs(sum - target) < diff:
                diff = abs(sum - target)
                min_set = [nums[i], nums[j], nums[k]]
            j += 1
            k -= 1

    return min_set

print(sum3_closest([-1, 2, 1, -4], 1))
print(sum3_closest([0, 0, 0], 1))
print(sum3_closest([1, 2, 3, 4], 10))