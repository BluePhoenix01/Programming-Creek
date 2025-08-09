def zigzagConversion(s, rows):
    if rows == 1:
        return s
    zigzag = ""
    for row in range(rows):
        i = row
        if row == 0 or row == rows-1:
            while i < len(s):
                zigzag += s[i]
                i += (rows-1)*2
        
        else:
            change = (rows - (i+1))*2
            while i < len(s):
                zigzag += s[i]
                i += change
                change = abs(change - (rows-1)*2)
        # print(f"Row {row}: {zigzag}")

    return zigzag

print(zigzagConversion("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(zigzagConversion("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(zigzagConversion("12345432123454321", 5)) 
