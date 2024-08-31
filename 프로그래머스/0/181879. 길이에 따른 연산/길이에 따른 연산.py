def solution(num_list):
    res = 1
    if len(num_list) > 10:
        return sum(num_list)
    else:
        for num in num_list:
            res *= num
        return res