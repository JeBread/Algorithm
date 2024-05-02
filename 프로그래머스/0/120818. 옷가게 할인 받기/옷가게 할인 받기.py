import math

def solution(price):
    ans = 0
    if price >= 500000:
        ans = price * 0.8
    elif price >= 300000:
        ans = price * 0.9
    elif price >= 100000:
        ans = math.floor(price * 0.95)
    else:
        ans = price
    return ans