def countAndSay(n):
    if n == 1:
        return '1'
    prev = countAndSay(n-1)
    char_count = 0
    current_char = prev[0]
    count_str = ""
    for c in prev:
        if current_char != c:
            count_str += str(char_count) + current_char
            current_char = c
            char_count = 0
        char_count += 1

    return count_str + str(char_count) + current_char

print(countAndSay(6))  # Example usage

        


        