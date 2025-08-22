import math

def rotateImage(matrix):
    if not matrix or not matrix[0]:
        return

    n = len(matrix)
    # Transpose the matrix
    for i in range(n//2):
        for j in range(math.ceil(n/2)):
            matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]
    
    return matrix

for row in rotateImage([[1,2,3],[4,5,6],[7,8,9]]):
    print(row)

for row in rotateImage([[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]):
    print(row)