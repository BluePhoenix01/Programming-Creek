def uniquePathsII(matrix):
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [0] * n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                dp[j] = 0
            elif i == 0 and j == 0:
                dp[j] = 1
            elif j > 0:
                dp[j] += dp[j-1]
    
    return dp[-1]

print(uniquePathsII([[0,0,0],[0,1,0],[0,0,0]]))  # Output: 2
print(uniquePathsII([[0,0,0],[0,0,0],[0,0,0]]))  # Output: 6
