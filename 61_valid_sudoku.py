def isValidSudoku(board):
    if not board or len(board) != 9 or len(board[0]) != 9:
        return False
    
    def colCheck(board, col):
        numbers = set()
        for i in range(9):
            if board[i][col] in numbers:
                return False
            elif board[i][col] != ".":
                numbers.add(board[i][col])
        return True
    def rowCheck(board, row):
        numbers = set()
        for i in range(9):
            if board[row][i] in numbers:
                return False
            elif board[row][i] != ".":
                numbers.add(board[row][i])
        return True
        
    def boxCheck(board, row, col):
        numbers = set()
        for i in range(row*3, row*3+3):
            for j in range(col*3, col*3+3):
                if board[i][j] in numbers:
                    return False
                elif board[i][j] != ".":
                    numbers.add(board[i][j])
        return True
    
    for i in range(9):
        if not (rowCheck(board, i) and colCheck(board, i)):
            return False
    
    for i in range(3):
        for j in range(3):
            if not boxCheck(board, i, j):
                return False
            
    return True

print(isValidSudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]))
# True