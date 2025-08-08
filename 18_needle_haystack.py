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
        j = lps[i - 1]
        while j > 0 and needle[i] != needle[j]:
            j = lps[j - 1]
        if needle[i] == needle[j]:
            j += 1
        lps[i] = j
    
    i = 0
    j = 0
    print(f"Initial LPS: {lps}")
    while i < len(haystack):
        print(f"i: {i}, j: {j}, haystack[i]: {haystack[i]}, needle[j]: {needle[j] if j < len(needle) else 'N/A'}")
        if j < len(needle) and haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == len(needle):
                return i - j
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
        print(f"Updated i: {i}, j: {j}")
    return -1

print(strStr("hello", "ll"))  # Output: 2
print(strStr("aaaaa", "bba"))  # Output: -1 
print(strStr_KMP("hello", "ll"))  # Output: 2
print(strStr_KMP("aaaaa", "bba"))  # Output: -1


