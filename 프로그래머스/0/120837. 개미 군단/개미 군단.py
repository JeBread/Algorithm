def solution(hp):
    ans = 0
    ans += hp // 5
    ans += (hp % 5) // 3
    ans += ((hp % 5) % 3) // 1
    return ans