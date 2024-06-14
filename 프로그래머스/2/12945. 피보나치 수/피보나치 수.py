def solution(n):
    ans = 0
    
#     def fibo(x):    테스트 케이스 7부터 런타임 에러 뜸. 재귀가 너무 깊음.
#         if x == 0:
#             return 0
#         if x == 1:
#             return 1
#         return fibo(x-1) + fibo(x-2)
    
#     ans = fibo(n)

    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append(fibo[i-2] + fibo[i-1])
    ans = fibo[-1]%1234567
    
    return ans