def solution(i, j, k):
    ans = 0
    for x in range(i, j+1):
        for y in str(x):
            if str(k) == y:
                ans += 1
    return ans


# def solution(i, j, k):
#     answer = 0
#     for n in range(i, j + 1):
#         answer += str(n).count(str(k))
#     return answer