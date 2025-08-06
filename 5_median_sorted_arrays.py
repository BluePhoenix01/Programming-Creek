def median_sorted_arrays(nums1, nums2):
    merged = nums1 + nums2
    merged.sort()
    n = len(merged)
    if n % 2 == 0:
        return (merged[n // 2] + merged[n // 2 - 1]) / 2
    else:
        return merged[n // 2]
    

    
    
print(median_sorted_arrays([1, 3], [2]))
print(median_sorted_arrays([1, 2], [3, 4]))

