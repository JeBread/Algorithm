def solution(n):
    num = []
    cnt = 0
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            if i % j == 0 :
                num.append(i)
        if num.count(i) >= 3:
            cnt += 1
    return cnt
