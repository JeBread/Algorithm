def solution(a, b):
    ans1, ans2 = '', ''
    ans1 += str(a)
    ans1 += str(b)
    ans2 += str(b)
    ans2 += str(a)
    if ans1 > ans2:
        return int(ans1)
    else: return int(ans2)