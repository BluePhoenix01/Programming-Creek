def simplifyPath(path):
    path_list = path.split('/')
    i = len(path_list)-1
    simple_path = ""
    skip_count = 0

    while i >= 0:
        if path_list[i] in {'.', ''}:
            i -= 1
            continue
        if path_list[i] == '..':
            skip_count += 1
            i -= 1
            continue
        if skip_count > 0:
            skip_count -= 1
            i -= 1
            continue
        simple_path = '/' + path_list[i] + simple_path
        i -= 1
    
    return simple_path if simple_path != '' else '/'

print(simplifyPath("/a/./b/../../c/"))  # Output: "/c"
print(simplifyPath("/../"))  # Output: "/"
print(simplifyPath("/home//foo/"))  # Output: "/home/foo"
print(simplifyPath("/a/../../b/../c//.//"))  # Output: "/c"
print(simplifyPath("/a//b////c/d//././/.."))  # Output: "/a/b/c/d"