def solution(n):
    ans = 1
    while (ans * 6) % n != 0:
        ans += 1
    return ans