def isIsomorphic(s, t):
    if s == t:
        return True
    if len(s) != len(t):
        return False
    if s is None or t is None:
        return False
    if len(set(s)) != len(set(t)):
        return False
    return True

print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))