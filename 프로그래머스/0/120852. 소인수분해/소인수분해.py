def solution(n):
    ans = []
    
    x = 2
    while x <= n:
        if n % x == 0:
            if x not in ans:
                ans.append(x)
            n //= x
        else:
            x += 1
    return ans