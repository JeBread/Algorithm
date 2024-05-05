def solution(array, n):
    array.sort(reverse=True)
    ans = 0
    minV = 21e8
    for x in array:
        if abs(x-n) <= minV:
            minV = abs(x-n)
    for x in array:
        if abs(x-n) == minV:
            ans = x
    return ans