def removeDuplicates(nums):
    j = 0
    count = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j] and count >= 1:
            j += 2
            nums[j] = nums[i]
            count = 0
        count += 1
        
    return nums[:j+1], j+1

print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  
print(removeDuplicates([1, 1, 1, 2, 2, 3]))
print(removeDuplicates([1, 2, 3, 4, 5, 6, 7, 8, 9]))