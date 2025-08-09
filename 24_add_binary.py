def addBinary(a, b):
    if len(a) < len(b):
        a, b = b, a
    c = ""
    a = a[::-1]
    b = b[::-1]
  
    carry_bit = 0
    i = 0
    while i < len(b):
        c += str((carry_bit + int(a[i]) + int(b[i]))%2)
        carry_bit = (carry_bit + int(a[i]) + int(b[i])) // 2
        i += 1
    while i < len(a):
        c += str((carry_bit + int(a[i])) % 2)
        carry_bit = (carry_bit + int(a[i])) // 2
        i += 1
    if carry_bit:
        c += str(carry_bit)
    return c[::-1]

def addBinaryInt(a, b):
    c = ""
    carry_bit = 0
    for i in range(max(len(a), len(b))):
        bit_a = int(a[-1-i]) if i < len(a) else 0
        bit_b = int(b[-1-i]) if i < len(b) else 0
        c += str((carry_bit + bit_a + bit_b) % 2)
        carry_bit = (carry_bit + bit_a + bit_b) // 2
    if carry_bit:
        c += str(carry_bit)
    return c[::-1]

print(addBinary("10", "111"))
print(addBinaryInt("10", "111"))
