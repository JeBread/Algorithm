def solution(brown, yellow):
    answer = []
    yellow_x = 0
    yellow_y = 0
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yellow_x = yellow // i
            yellow_y = i
            if 2*yellow_x + 2*yellow_y + 4 == brown:
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                break 
            answer.sort(reverse = True)
    return answer


# 다른 사람의 풀이
# def solution(brown, yellow):
#     for i in range(1, int(yellow**0.5) + 1):
#         if yellow % i == 0:  # i가 yellow의 약수일 때
#             y = i
#             x = yellow // i
#             if brown == (x + 2) * 2 + y * 2:
#                 return [x + 2, y + 2]