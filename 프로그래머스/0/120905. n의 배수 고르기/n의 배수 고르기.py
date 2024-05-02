def solution(n, numlist):
    ans = []
    for x in numlist:
        if x % n == 0:
            ans.append(x)
    return ans