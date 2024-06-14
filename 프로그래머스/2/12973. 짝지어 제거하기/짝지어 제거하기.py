def solution(s):
    ans = 0   # 가능 불가능 여부 체크할 변수 ans
#     s_lst = list(s) # 문자열 s를 리스트 형태로
#     keep = 1
    
#     def delPair(x):
#         nonlocal ans, keep   #  nonlocal 키워드로 상위 스코프에 있는 ans 가져오기
#         if len(x) == 0:   # 문자열 길이 0이면 리턴 조건
#             ans = 1 
#             keep = 0 # 가능 여부 체크
#             return
#         for i in range(len(x)-1):
#             if x[i] == x[i+1]:  #  앞글자 뒷글자 확인
#                 del(x[i])   # 앞글자 지워
#                 del(x[i])   # 뒷글자도 지워
#                 # print(x)
#                 # delPair(x)   # 재귀 반복
#                 return
#         keep = 0
#         return 
    
#     while keep:
#         delPair(s_lst)
    
#     if len(s_lst) == 0:
#         ans = 1
        
    # 위에서 1. 재귀 , 2. while문으로 풀어봤는데 런타임 에러, 시간 초과로 해결 못함
    # 이번에는 stack을 활용해서 풀어보려 함. => 성공
    
    stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    
    if len(stack) == 0:
        ans = 1
    
    return ans
