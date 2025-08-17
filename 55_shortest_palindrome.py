def shortestPalindrome_KMP(s):
    if not s:
        return ""
    rev = s[::-1]
    combined = s + "#" + rev

    lps = [0] * len(combined)
    j = 0
    for i in range(1, len(combined)):
        print(f"i: {i}, j: {j}, combined[i]: {combined[i]}, combined[j]: {combined[j] if j < len(combined) else 'N/A'}")
        while j > 0 and combined[i] != combined[j]:
            j = lps[j - 1]
        if combined[i] == combined[j]:
            j += 1
            lps[i] = j
        print(f"Updated LPS: {lps}") 
    
    longest_prefix = lps[-1]
    suffix = s[longest_prefix:]

    # Append the reverse of the suffix to the original string
    return suffix[::-1] + s

# print(shortestPalindrome("aacecaaa"))  # Output: "aaacecaaa"
# print(shortestPalindrome("axx"))      # Output: "dcbabcd"  

print(shortestPalindrome_KMP("aacecaaa"))  # Output: "aaacecaaa"
print(shortestPalindrome_KMP("axxax"))      