def solution(my_string, is_suffix):
    ans = 0
    for i in range(len(my_string)):
        if my_string[i:] == is_suffix:
            ans = 1
    return ans