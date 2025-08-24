def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])

    max_area = 0
    heights = [0 for _ in range(n+1)]

    for i in range(m):
        for j in range(n):
            if matrix[i][j]:
                heights[j] += 1
            else:
                heights[j] = 0
        stack = []
        area = 0
        print(heights)
        for j, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = j if not stack else j - stack[-1] - 1
                area = max(area, height * width)
            stack.append(j)
        max_area = max(max_area, area)
    
    return max_area

print(maximalRectangle([[1,0,1,0,0],
                        [1,0,1,1,1],
                        [1,1,1,1,1],
                        [1,0,0,1,0]]))  # Output: 6
