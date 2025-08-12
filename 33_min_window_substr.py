def minWindowSubstr(s: str, t: str) -> str:
    if not s or not t:
        return ""

    from collections import Counter

    need = Counter(t)  # Count of chars we need
    window: dict = {}
    have = 0            # How many unique chars match the required count
    need_count = len(need)

    res = ""
    res_len = float("inf")
    left = 0

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            have += 1

        while have == need_count:
            # Update result
            if (right - left + 1) < res_len:
                res = s[left:right+1]
                res_len = right - left + 1

            # Shrink window from left
            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1
            left += 1

    return res

print(minWindowSubstr("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(minWindowSubstr("aswschaybjsa", "abc"))