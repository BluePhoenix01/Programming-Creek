def genPascalTriangle(n):
    triangle = [[1]]
    for i in range(1, n):
        triangle.append([1])
        for j in range(1, i):
            triangle[i].append(triangle[i-1][j] + triangle[i-1][j-1])
        triangle[i].append(1)
    
    return triangle

print(genPascalTriangle(5))
