def solution(s):
    s2 = s.lower() # 전체 문자열 소문자로 만들기
    lst = list(s2) # 문자열을 리스트 형태로
    if not lst[0].isdigit(): # 첫 문자가 글자면 
        lst[0] = lst[0].upper() # 대문자로 만들기
    for i in range(len(lst)-1): # 인덱스 안 나가게 끝 바로 직전 지점까지
        if lst[i] == " ": # 빈 공백 만나면
            lst[i+1] = lst[i+1].upper() # 그 다음 문자 대문자 만들기
    
    return ''.join(lst)  # 리스트 형태를 문자열로 다시 만들기 ''기준으로 다 붙이기 join 