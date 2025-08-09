def is_palindrome(s):
    pal_str = ("".join(char for char in s if char.isalpha()).lower())
    left = 0
    right = len(pal_str) - 1

    while left < right:
        if pal_str[left] != pal_str[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("race a car"))  # Output: False