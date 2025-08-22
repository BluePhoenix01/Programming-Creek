def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    top, bottom = 0, rows - 1
    while top <= bottom:
        mid = (top + bottom) // 2
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            # Target is in this row
            left, right = 0, cols - 1
            while left <= right:
                mid_col = (left + right) // 2
                if matrix[mid][mid_col] == target:
                    return True
                elif matrix[mid][mid_col] < target:
                    left = mid_col + 1
                else:
                    right = mid_col - 1
            return False
        elif matrix[mid][0] < target:
            top = mid + 1
        else:
            bottom = mid - 1
    return False

print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))