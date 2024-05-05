def solution(num_list, n):
    ans = []
    cnt = 0
    temp = []
    for num in num_list:
        temp.append(num)
        cnt += 1
        if cnt == n:
            ans.append(temp)
            temp = []
            cnt = 0

    return ans

# import numpy as np
# def solution(num_list, n):
#     li = np.array(num_list).reshape(-1,n)
#     return li.tolist()