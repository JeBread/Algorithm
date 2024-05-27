def solution(arr, divisor):
    ans = []
    for x in arr:
        if x % divisor == 0:
            ans.append(x)
    ans.sort()
    if len(ans) == 0:
        ans.append(-1)
    return ans

## 다른 사람 풀이
# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]