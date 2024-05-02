def solution(array, height):
    ans = 0
    for x in array:
        if x > height:
            ans += 1
    return ans