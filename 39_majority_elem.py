def majorityElement(nums):
    num_count = {}
    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1
        if num_count[num] > len(nums) // 2:
            return num
    return None

def majorityElementBMV(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

# print(majorityElement([3, 2, 3]))
# print(majorityElement([2, 2, 1, 1, 1, 2, 2]))

print(majorityElementBMV([3, 2, 3]))
print(majorityElementBMV([2, 2, 1, 1, 1, 2, 2]))