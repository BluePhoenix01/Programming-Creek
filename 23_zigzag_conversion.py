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

    return zigzag

def zigzagConversionFaster(s, rows):
    if rows == 1 or rows >= len(s):
        return s

    lines = [''] * rows
    row, step = 0, 1

    for ch in s:
        lines[row] += ch
        if row == 0 or row == rows - 1:
            step = -step
        row -= step

    return ''.join(lines)

print(zigzagConversion("PAYPALISHIRING", 3))
# print(zigzagConversion("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
# print(zigzagConversion("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(zigzagConversion("12345432123454321", 5)) 

# p   a   h   n
#  a p l s i i g
#   y   i   r
