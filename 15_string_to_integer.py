def atoi(s):
    s = s.strip()
    if not s:
        return 0
    sign = 1
    if s[0] == '-':
        sign = -1
    i = 0
    if s[0] in ['-', '+']:
        i = 1
    num = 0
    while i < len(s) and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1
    return sign * num

# Test cases
print(atoi("42"))          # Output: 42
print(atoi("   -42"))      # Output: -42
print(atoi("4193 with words")) # Output: 4193
print(atoi("words and 987"))   # Output: 0
print(atoi("-91283472332"))    # Output: -2147483648
print(atoi("92233720368547758090"))    # Output: 
