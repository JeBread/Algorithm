def solution(s):
    s_lst = list(s)
    s_lst.sort(reverse=True)
    return str(''.join(s_lst))