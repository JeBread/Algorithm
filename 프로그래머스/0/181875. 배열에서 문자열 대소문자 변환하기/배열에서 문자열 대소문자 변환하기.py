def solution(strArr):
    ans = []
    for i in range(len(strArr)):
        st = ''
        for x in strArr[i]:
            if i % 2 == 1:
                st += x.upper()
            else:
                st += x.lower()
        ans.append(st)
            
    return ans