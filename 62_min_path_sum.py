def minPathSum(grid):
    # Using DFS
    # return dfs(0, 0, grid)
    dp = [0]*len(grid[0])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0:
                dp[j] = grid[i][j]
            elif i == 0:
                dp[j] = dp[j-1] + grid[i][j]
            elif j == 0:
                dp[j] = dp[j] + grid[i][j]
            else:
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]

    return dp[-1]

def dfs(i, j, grid):
    if i == len(grid) - 1 and j == len(grid[0]) - 1:
        return grid[i][j]
    if i == len(grid) - 1:
        return grid[i][j] + dfs(i, j+1, grid) 
    if j == len(grid[0]) - 1:
        return grid[i][j] + dfs(i+1, j, grid) 

    return grid[i][j] + min(dfs(i+1, j, grid), dfs(i, j+1, grid)) 

print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(minPathSum([[1,2,3],[4,5,6]]))


