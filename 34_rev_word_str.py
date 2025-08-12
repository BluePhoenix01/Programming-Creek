def reverseWords(s):
    reversed_words = ""
    j = len(s)
    for i in range(len(s) - 1, -1, -1):
        if s[i] == " " or i == 0:
            start = i if i == 0 else i + 1
            word = s[start:j]
            if word:  # skip empty segments from multiple spaces
                if reversed_words:
                    reversed_words += " "
                reversed_words += word
            j = i
    return reversed_words

print(reverseWords("  Hello World  "))
print(reverseWords("Python is fun"))