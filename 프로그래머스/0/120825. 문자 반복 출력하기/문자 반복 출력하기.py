def solution(my_string, n):
    ans = ''
    for x in my_string:
        ans += x*n
    return ans