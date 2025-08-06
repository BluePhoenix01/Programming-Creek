def is_isomorphic(s, t):
    if s == t:
        return True
    if len(s) != len(t):
        return False
    if s is None or t is None:
        return False
    if len(set(s)) != len(set(t)):
        return False
    return True

print(is_isomorphic("egg", "add"))
print(is_isomorphic("foo", "bar"))
print(is_isomorphic("paper", "title"))