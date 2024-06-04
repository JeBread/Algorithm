def solution(num_list):
    ans = -1
    for i in range(len(num_list)):
        if num_list[i] < 0:
            ans = i
            break
    
            
    return ans