def longestCommonPrefix(strs):
    if not strs:
        return ""
    longest_prefix = strs[0]
    for word in strs:
        if not word:
            return ""
        new_prefix = ""
        for i in range(min(len(word), len(longest_prefix))):
            if word[i] != longest_prefix[i]:
                break
            new_prefix += longest_prefix[i]
        longest_prefix = new_prefix
    return longest_prefix

print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))  # Output: ""