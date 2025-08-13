def largestRectAreaRecursive(height):
    def maxAreaHelper(height, left=0, right=1):
        if right == len(height):
            return min(height[left:right])*(right-left)
        if left == right:
            return 1*height[left]
        return max(min(height[left:right])*(right-left), maxAreaHelper(height, left, right + 1), maxAreaHelper(height, left + 1, right))
    
    return maxAreaHelper(height)
    

print(largestRectAreaRecursive([2, 1, 5, 6, 7, 3, 2, 2, 2]))
print(largestRectAreaRecursive([2, 4]))
print(largestRectAreaRecursive([1, 2, 3, 4, 5, 6]))