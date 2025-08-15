def genPascalTriangleII(rowIndex):
    row = [1]
    for i in range(1, rowIndex+1):
        row.append(0)  # extend the row for the new element
        # update from end to start
        for j in range(i, 0, -1):
            row[j] = row[j] + row[j-1]
    
    return row

print(genPascalTriangleII(5))
