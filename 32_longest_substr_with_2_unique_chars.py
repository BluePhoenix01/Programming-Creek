def longestSubstr2UniqueChars(s):
    seen = set()
    left = 0
    max_len = 0
    longest_substr = ""

    for right in range(len(s)):
        seen.add(s[right])
        while len(seen) > 2:
            seen.remove(s[left])
            left += 1
        if right - left + 1 > max_len:
            max_len = right - left + 1
            longest_substr = s[left:right + 1]

    return longest_substr

print(longestSubstr2UniqueChars("abcabcbb"))  
print(longestSubstr2UniqueChars("bbbbb"))     
print(longestSubstr2UniqueChars("pwwkew"))    

