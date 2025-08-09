def merge(arr1, arr2):
    merged = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        print(f"Merging {arr1[i]} and {arr2[j]}")
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
        print(f"Merged array: {merged}")
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    return merged

def mergeSortedArrays(arr1, arr2):
    i = len(arr1) - 1
    j = len(arr2) - 1
    k = i + j + 1
    merged = [0] * (k + 1)
    while k >= 0:
        print(f"Comparing {arr1[i]} and {arr2[j]}")
        if j < 0 or (i >= 0 and arr1[i] > arr2[j]):
            merged[k] = arr1[i]
            i -= 1
        else:
            merged[k] = arr2[j]
            j -= 1
        k -= 1
        print(f"Merged array: {merged}")
    return merged

# print(merge([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
print(mergeSortedArrays([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
