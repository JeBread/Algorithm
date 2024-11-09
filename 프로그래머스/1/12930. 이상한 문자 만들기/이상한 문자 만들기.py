def solution(s):
    ans = ''
    res = s.split(' ')
    for x in res:
        for i in range(len(x)):
            if i % 2 == 0:
                ans += x[i].upper()
            else:
                ans += x[i].lower()
        ans += ' '
    return ans[:-1]