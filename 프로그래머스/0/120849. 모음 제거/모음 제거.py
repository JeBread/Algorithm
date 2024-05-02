def solution(my_string):
    ans = ''
    lst = 'aeiou'
    for st in my_string:
        if st not in lst:
            ans += st
    return ans