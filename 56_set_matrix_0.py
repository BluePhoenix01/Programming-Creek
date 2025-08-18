# m*n space complexity
def setZeroes(matrix):
    zeroes = []
    rows = len(matrix)
    cols = len(matrix[0]) 
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zeroes.append((i, j))
        
    if not zeroes:
        return matrix
    
    for i, j in zeroes:
        for k in range(rows):
            matrix[k][j] = 0
        for k in range(cols):
            matrix[i][k] = 0
    return matrix

# m+n space complexity
def setZeroesConstant(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    row_zero = False
    col_zero = False

    for i in range(rows):
        if matrix[i][0] == 0:
            col_zero = True
    for j in range(cols):
        if matrix[0][j] == 0:
            row_zero = True
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
        
    for i in range(1, rows):
        if matrix[i][0] == 0:
            for j in range(1, cols):
                matrix[i][j] = 0
            
    for j in range(1, cols):
        if matrix[0][j] == 0:
            for i in range(1, rows):
                matrix[i][j] = 0

    if row_zero == True:
        for col in range(cols):
            matrix[0][col] = 0
    
    if col_zero == True:
        for row in range(rows):
            matrix[row][0] = 0

    return matrix
print(setZeroesConstant([[1,1,1],[1,0,1],[1,1,1]]))  # Example usage
print(setZeroesConstant([[0,1,2],[3,4,5],[6,7,8]]))
