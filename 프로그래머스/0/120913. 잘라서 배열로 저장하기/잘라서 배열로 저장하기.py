# def solution(my_str, n):
#     answer = [my_str[i:i+n] for i in range(0, len(my_str), n)]
#     return answer

def solution(my_str, n):
    ans = []
    for i in range(0, len(my_str), n):
        ans.append(my_str[i:i+n])
    return ans