def solution(t, p):
    ans = 0
    for i in range((len(t)-len(p))+1):
        temp = ''
        for j in range(i, i+len(p)):
            temp += t[j]
        if int(temp) <= int(p):
            ans += 1
        
    return ans