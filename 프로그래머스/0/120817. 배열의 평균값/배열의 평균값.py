def solution(numbers):
    sum = 0
    for i in numbers:
        sum += i
    ans = sum / len(numbers)
    return ans