def solution(my_string):
    ans = 0
    for x in my_string:
        if x.isdigit():
            ans += int(x)
    return ans