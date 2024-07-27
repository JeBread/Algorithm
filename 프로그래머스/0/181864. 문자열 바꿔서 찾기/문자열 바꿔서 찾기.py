def solution(myString, pat):
    res = 0
    ans = []
    for st in myString:
        if st == 'A':
            ans.append('B')
        else:
            ans.append('A')
    if pat in ''.join(ans):
        res = 1
    else:
        pass
    return res