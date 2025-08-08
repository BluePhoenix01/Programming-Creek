def search_insert(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def search_insert_recursive(nums, target, right, left = 0):
    if left > right:
        return left
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return search_insert_recursive(nums, target, right, mid + 1)
    else:
        return search_insert_recursive(nums, target, mid - 1, left) 
    
# print(search_insert([1, 3, 5, 6], 5))  # Output: 2
# print(search_insert([1, 3, 5, 6], 2))  # Output: 1
# print(search_insert([1, 3, 5, 6], 7))  # Output: 4

print(search_insert_recursive([1, 3, 5, 6], 5, len([1, 3, 5, 6]) - 1))  # Output: 2
print(search_insert_recursive([1, 3, 5, 6], 2, len([1, 3, 5, 6]) - 1))  # Output: 1
print(search_insert_recursive([1, 3, 5, 6], 7, len([1, 3, 5, 6]) - 1))  # Output: 4
