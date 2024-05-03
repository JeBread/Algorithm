def solution(order):
    ans = 0
    lst = '369'
    for st in str(order):
        if st in lst:
            ans += 1
    return ans