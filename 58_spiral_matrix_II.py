def spiralMatrixII(n):
    if n <= 0:
        return []
    spiral_matrix = []
    for i in range(n):
        spiral_matrix.append([])
        for j in range(n):
            spiral_matrix[i].append(0)
    left, right = 0, n - 1
    top, bottom = 0, n - 1 
    count = 1
    while count < n*n+1:
        for i in range(left, right+1):
            spiral_matrix[top][i] = count
            count += 1
        top += 1

        for i in range(top, bottom+1):
            spiral_matrix[i][right] = count
            count += 1
        right -= 1

        for i in range(right, left-1, -1):
            spiral_matrix[bottom][i] = count
            count += 1
        bottom -= 1

        for i in range(bottom, top-1, -1):
            spiral_matrix[i][left] = count
            count += 1
        left += 1

    return spiral_matrix

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print()
            
           
printMatrix(spiralMatrixII(5))