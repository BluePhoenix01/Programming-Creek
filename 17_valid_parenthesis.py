def isValidParenthesis(s):
    stack = []
    mapping = {'(': ')', '[': ']', '{': '}'}
    print(f"Input string: {s}")
    for char in s:
        print(f"Processing character: {char}")
        if char in mapping:
            stack.append(char)
        elif stack and char == mapping[stack[-1]]:
            stack.pop()
        else:
            return False
        print(f"Current stack: {stack}")
    return not stack

# print(is_valid_parenthesis("()[]{}"))  # Output: True
print(isValidParenthesis("(]"))      # Output: False
# print(is_valid_parenthesis("([)]"))    # Output: False
# print(is_valid_parenthesis("{[]}"))    # Output: True
