def solution(n):
    ans = 0
    for i in range(1, n+1):
        sum1 = 0
        for j in range(i, n+1):
            sum1 += j
            if sum1 == n:
                ans += 1
                break
            elif sum1 > n:
                break

    return ans