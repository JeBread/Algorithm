def solution(price, money, count):
    ans = 0
    for i in range(1, count+1):
        ans += i * price
    if ans <= money:
        ans = 0
    else:
        ans -= money
    
    return ans