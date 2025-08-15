def compareVersion(version1, version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    i = 0
    while i < max(len(v1), len(v2)):
        if len(v1) <= i and len(v1) < len(v2):
            v1.append('0')
        if len(v2) <= i and len(v1) > len(v2):
            v2.append('0')
        if int(v1[i]) > int(v2[i]):
            return 1
        if int(v1[i]) < int(v2[i]):
            return -1
        i += 1
    
    return 0
        
def compareVersionBetter(version1, version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    i = 0
    
    while i < max(len(v1), len(v2)):
        num1 = int(v1[i]) if i < len(v1) else 0
        num2 = int(v2[i]) if i < len(v2) else 0
        
        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
        
        i += 1
    
    return 0


print(compareVersion("1.0", "1.0.0"))  # Output: 0
print(compareVersion("1.0.1", "1.0"))  # Output: 1
print(compareVersion("1.0", "1.0.1"))  # Output: -1
print(compareVersion("1.0.1", "1.0.1"))  # Output: 0

