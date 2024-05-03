def solution(my_string):
    ans = ''
    for i in my_string:
        ans += i.lower()
    return ''.join(sorted(ans))