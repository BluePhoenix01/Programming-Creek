def addBinary(a, b):
    if len(a) < len(b):
        a, b = b, a
    c = ""
    a = a[::-1]
    b = b[::-1]
    parry_bit = 0
    i = 0
    while i < len(b):
        c += str((parry_bit + int(a[i]) + int(b[i]))%2)
        parry_bit = 1 if parry_bit + int(a[i]) + int(b[i]) > 0 else 0
        i += 1
    while i < len(a):
        c += str((parry_bit + int(a[i])) % 2)
        parry_bit = parry_bit + int(a[i]) // 2
        i += 1
    if parry_bit:
        c += str(parry_bit)
    return c[::-1]

print(addBinary("10", "111"))
