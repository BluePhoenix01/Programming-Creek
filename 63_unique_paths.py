def uniquePathsDP(m, n):
    dp = [[1]*n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

def nCr(n, r):
    r = min(r, n-r)  # take advantage of symmetry nCr = nC(n-r)
    result = 1
    for i in range(1, r+1):
        result = result * (n - r + i) // i
    return result

def uniquePaths(m, n):
    return nCr(m+n-2, m-1)

print(uniquePathsDP(3, 2))  # Output: 3
print(uniquePathsDP(7, 3))  # Output: 28
