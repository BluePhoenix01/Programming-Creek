def isMatch(s, p):
    stack_s = list(s)
    stack_p = list(p)
    def recursiveHelper(stack_s, stack_p):
        match = False
        print(stack_s, stack_p)
        if stack_p == []:
            return stack_s == []
        if stack_s and stack_p[0] in (stack_s[0], '.') :
            match = True
        if len(stack_p) > 1 and stack_p[1] == '?':
            if match:
                return recursiveHelper(stack_s[1:], stack_p[2:])
            return recursiveHelper(stack_s, stack_p[2:])
        if len(stack_p) > 1 and stack_p[1] == '*':
            if recursiveHelper(stack_s, stack_p[2:]):
                return True
            if match:
                return recursiveHelper(stack_s[1:], stack_p)
        
        if len(stack_p) > 1 and stack_p[1] == '+':
            if match:
                return recursiveHelper(stack_s[1:], stack_p)
            return recursiveHelper(stack_s, stack_p[2:])
        
        if match:
            return recursiveHelper(stack_s[1:], stack_p[1:])
        return False

    return recursiveHelper(stack_s, stack_p)


# print(isMatch("aa", "aa"))
# print(isMatch("ab", ".*"))
# print(isMatch("aa", "a*"))
# print(isMatch("aab", "c*a*b"))
# print(isMatch("mississippi", "mis*is*p*."))
            
print(isMatch("aaa", "a*a"))          # True
print(isMatch("ab", ".*"))            # True
print(isMatch("ab", ".*c"))           # False
print(isMatch("mississippi", "mis*io?s+ip*."))  # True
print(isMatch("aaa", "aaaa"))         # False

