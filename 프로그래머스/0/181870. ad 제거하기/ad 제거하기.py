def solution(strArr):
    ans = []
    for st in strArr:
        if "ad" in st:
            continue
        else:
            ans.append(st)
    return ans