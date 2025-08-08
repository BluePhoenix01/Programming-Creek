def strStr(haystack, needle):
    if not needle:
        return 0
    needle_length = len(needle)
    for i in range(len(haystack) - needle_length + 1):
        if haystack[i:i + needle_length] == needle:
            return i
    return -1

def strStr_KMP(haystack, needle):
    if not needle:
        return 0
    # Build the longest prefix suffix (LPS) array
    lps = [0] * len(needle)
    for i in range(1, len(needle)):
            
    
print(strStr("hello", "ll"))  # Output: 2
print(strStr("aaaaa", "bba"))  # Output: -1 
