def solution(str_list, ex):
    ans = ''
    for st in str_list:
        if ex in st:
            continue
        else:
            ans += st
    return ans