def solution(numbers, num1, num2):
    ans = []
    for i in range(num1, num2+1):
        ans.append(numbers[i])
    return ans