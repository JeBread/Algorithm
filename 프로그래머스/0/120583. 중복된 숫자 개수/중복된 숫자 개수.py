def solution(array, n):
    cnt = 0
    for x in array:
        if x == n:
            cnt += 1
    return cnt