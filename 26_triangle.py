def minTriangleSum(triangle, top = [0, 0]):
    print("Current top:", triangle[top[0]][top[1]])
    if len(triangle) - 1 == top[0]:
        return triangle[top[0]][top[1]]
    i, j = top
    return triangle[i][j] + min(minTriangleSum(triangle, [i + 1, j+1]), minTriangleSum(triangle, [i+1, j]))  

def minTriangleSumDP(triangle):
    if not triangle:
        return 0

    dp = triangle[-1].copy()
    for row in range(len(triangle) - 2, -1, -1):
        for i in range(row+1):
            dp[i] = triangle[row][i] + min(dp[i], dp[i+1])

    return dp[0]

print(minTriangleSumDP([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # Output: 11
print(minTriangleSumDP([[1], [2, 3], [4, 5, 6]]))  # Output: 7
