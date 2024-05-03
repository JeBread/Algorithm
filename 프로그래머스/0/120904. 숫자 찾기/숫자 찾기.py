def solution(num, k):
    ans = -1
    st = str(num)
    for i in range(len(st)):
        if str(k) == st[i]:
            ans = i+1
            break
    return ans