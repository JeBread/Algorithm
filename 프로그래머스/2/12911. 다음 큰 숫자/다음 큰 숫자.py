def solution(n):
    ans = 0
    count1_n = str(bin(n)).count("1")
    
    for i in range(n+1, 1000001):
        if str(bin(i)).count("1") == count1_n:
            ans = i
            break
    
    return ans