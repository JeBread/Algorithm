def solution(numbers, n):
    ans = 0
    for num in numbers:
        ans += num
        if ans > n:
            return ans