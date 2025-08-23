from collections import deque

def solve(board):
    if not board or not board[0]:
        return

    m, n = len(board), len(board[0])

    def bfs(x, y):
        queue = deque([(x, y)])
        board[x][y] = '#'   # mark safe
        while queue:
            i, j = queue.popleft()
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                    board[ni][nj] = '#'
                    queue.append((ni, nj))
    
    # Step 1: Mark border-connected 'O's
    for i in range(m):
        if board[i][0] == 'O':
            bfs(i, 0)
        if board[i][n-1] == 'O':
            bfs(i, n-1)
    for j in range(n):
        if board[0][j] == 'O':
            bfs(0, j)
        if board[m-1][j] == 'O':
            bfs(m-1, j)
    
    # Step 2: Flip captured + restore safe
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] = 'O'

    return board

print(solve([["X","X","X","X"],
              ["X","O","O","X"],
              ["X","X","O","X"],
              ["X","O","X","X"]]))
