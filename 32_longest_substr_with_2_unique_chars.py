def longestSubstr2UniqueChars(s):
    freq = {}
    left = 0
    max_len = 0
    longest_substr = ""

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > 2:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        if right - left + 1 > max_len:
            max_len = right - left + 1
            longest_substr = s[left:right + 1]

    return longest_substr

print(longestSubstr2UniqueChars("abcabcbb"))  
print(longestSubstr2UniqueChars("bbbbb"))     
print(longestSubstr2UniqueChars("pwwkew"))    
print(longestSubstr2UniqueChars("ccaabbb"))

