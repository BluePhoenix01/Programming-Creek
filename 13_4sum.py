def sum4(nums, target):
    nums.sort()
    res = []
    existing_set = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            k = j + 1
            l = len(nums) - 1

            while k < l:
                sum = nums[i] + nums[j] + nums[k] + nums[l]
                if sum > target:
                    l -= 1
                elif sum < target:
                    k += 1
                elif sum == target:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    if tuple(temp) not in existing_set:
                        existing_set.add(tuple(temp))
                        res.append([temp])
                    k += 1
                    l -= 1
                
    return res

print(sum4([1, 0, -1, 0, -2, 2], 0))
print(sum4([2, 2, 2, 2, 2], 8))
print(sum4([1, 2, 3, 4, 5], 10))