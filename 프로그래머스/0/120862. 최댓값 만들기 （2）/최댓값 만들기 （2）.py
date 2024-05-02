def solution(numbers):
    numbers.sort()
    x = numbers[0] * numbers[1]
    y = numbers[-1] * numbers[-2]
    if x >= y:
        return x
    else:
        return y