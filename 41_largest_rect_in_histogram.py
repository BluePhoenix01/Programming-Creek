def largestRectAreaRecursive(height):
    def maxAreaHelper(height, left=0, right=1):
        if right == len(height):
            return min(height[left:right])*(right-left)
        if left == right:
            return 1*height[left]
        return max(min(height[left:right])*(right-left), maxAreaHelper(height, left, right + 1), maxAreaHelper(height, left + 1, right))
    
    return maxAreaHelper(height)
    
def largestRectAreaRecursiveOptimized(heights):
    n = len(heights)
    if n == 0:
        return 0

    # Precompute mins for all ranges
    min_height = [[0] * n for _ in range(n)]
    for i in range(n):
        min_height[i][i] = heights[i]
        for j in range(i + 1, n):
            min_height[i][j] = min(min_height[i][j - 1], heights[j])

    for i in range(n):
        print(f"Min heights from {i}: {min_height[i]}")
    def helper(left, right):
        if left > right:
            return 0
        # Use precomputed min height
        area = min_height[left][right] * (right - left + 1)
        return max(area, helper(left + 1, right), helper(left, right - 1))

    return helper(0, n - 1)

def largestRectangleArea(heights):
    stack = []  # will store indices
    max_area = 0
    heights.append(0)  # sentinel to flush stack at the end

    for i, h in enumerate(heights):
        print(f"Current height: {h}, Stack: {stack}")
        while stack and heights[stack[-1]] > h:
            print(f"Popped {stack[-1]}: {heights[stack[-1]]}")
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area



# Example
# print(largestRectAreaRecursiveOptimized([2, 1, 5, 6, 2, 3]))  # Output: 10

# print(largestRectAreaRecursive([2, 1, 5, 6, 7, 3, 2, 2, 2]))
# print(largestRectAreaRecursive([2, 4]))
# print(largestRectAreaRecursive([1, 2, 3, 4, 5, 6]))

print(largestRectangleArea([2, 1, 5, 6, 2, 3]))  # Output: 10