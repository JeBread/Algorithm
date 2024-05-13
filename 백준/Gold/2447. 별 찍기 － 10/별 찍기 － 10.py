def make_star(n):
    # 기본 패턴 (n = 3) 설정
    if n == 3:
        return ["***", "* *", "***"]
    
    # n/3 크기의 패턴을 재귀적으로 생성
    sub_pattern = make_star(n // 3)
    pattern = []
    
    # 전체 그리드를 위해 3개의 섹션으로 나누고 각 섹션을 처리
    for i in range(3):
        for line in sub_pattern:
            if i == 1:  # 중간 섹션은 가운데 공백 처리
                pattern.append(line + " " * (n // 3) + line)
            else:  # 외부 섹션은 그대로 별 패턴 처리
                pattern.append(line * 3)
                
    return pattern

def main():
    N = int(input().strip())  # 입력을 받아 정수형으로 변환
    res = make_star(N)  # 별 패턴 생성
    for line in res:
        print(line)  # 결과 출력

if __name__ == "__main__":
    main()