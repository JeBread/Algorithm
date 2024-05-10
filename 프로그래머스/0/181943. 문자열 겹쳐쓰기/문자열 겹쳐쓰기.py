def solution(my_string, overwrite_string, s):
    ans = ''
    for i in range(0, s):
        ans += my_string[i]
    for i in range(len(overwrite_string)):
        ans += overwrite_string[i]
    for i in range(s+len(overwrite_string), len(my_string)):
        ans += my_string[i]
    return ans