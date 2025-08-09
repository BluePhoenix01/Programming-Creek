def lengthLastWord(s):
    if s is None:
        return 0
    flag = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] != " ":
            flag = i
        if s[i] == " " and flag:
            return flag - i - 1
    return 0

print(lengthLastWord("Hello World"))
print(lengthLastWord("   fly me   to   the moon  "))
print(lengthLastWord("luffy is still joyboy"))