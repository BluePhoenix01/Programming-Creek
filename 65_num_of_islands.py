from collections import deque

def numIslands(grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    num_islands = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":   # string check
                queue = deque()
                queue.append((i, j))
                grid[i][j] = "0"   # mark visited

                while queue:   # BFS loop
                    x, y = queue.popleft()
                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == "1":
                            grid[new_x][new_y] = "0"
                            queue.append((new_x, new_y))
                
                num_islands += 1
    
    return num_islands

def numIslandsDfs(grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    num_islands = 0

    def dfs(x, y):
        if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
            grid[x][y] = "0"  # mark visited
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(x + dx, y + dy)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                dfs(i, j)
                num_islands += 1

    return num_islands

print(numIslandsDfs([["1","1","0","0"],["1","0","0","1"],["0","0","1","1"],["0","1","1","0"]]))  # Output: 5
print(numIslandsDfs([["1","1","0","0","0"],
                  ["1","1","0","0","0"],
                  ["0","0","1","0","0"],
                  ["0","0","0","1","1"]]))  # Output: 3
