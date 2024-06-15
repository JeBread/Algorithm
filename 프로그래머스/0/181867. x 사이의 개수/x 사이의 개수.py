def solution(myString):
    ans = []
    cnt = 0
    for i in myString:
        if i == "x":
            ans.append(cnt)
            cnt = 0
        else:
            cnt += 1
    ans.append(cnt)
    return ans