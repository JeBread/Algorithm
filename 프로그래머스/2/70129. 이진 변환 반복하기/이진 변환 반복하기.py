def solution(s):
    ans = []
    total = 0   # 이진 변환의 횟수
    ln = 0   # 길이 담아줄 변수
    cnt = 0   # 제거된 모든 0의 개수 담을 변수
    
    def replay(st):
        nonlocal cnt, total
        if st == "1":  # 최종 탈출 조건
            return
             
        for x in st:   # 제거할 0의 개수 세기
            if x == "0":
                cnt += 1
                
        st = st.replace("0","")   # 0 제거
        st = bin(len(st))[2:]     # 길이 담아주기
        total += 1                # 이진 변환 횟수 증가
        ln = len(st)
        replay(st)             # 재귀
        
    replay(s)
    
    ans.append(total)
    ans.append(cnt)
    return ans