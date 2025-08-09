def isInteger(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def evalRPN(tokens):
    stack = []
    for token in tokens:
        if isInteger(token):
            stack.append(int(token))
        else:
            a = stack.pop()
            b = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(b - a)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(b / a))

    return stack[0]            

tokens = ["10", "6", "9", "3", "+", "-11", "*", "+", "*", "17", "+", "5", "+"]
result = evalRPN(tokens)
print(result)