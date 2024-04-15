# 테스트 케이스의 수 입력
T = int(input())

# 테스트 케이스 수 만큼 반복
for tc in range(1, T+1):
    # 재료의 수와 제한 칼로리 입력
    N, L = map(int, input().split())

    # 재료에 대한 맛과 칼로리 입력
    ingredients = []
    for _ in range(N):
        T, K = map(int, input().split())
        ingredients.append((T, K))

    # DP를 위한 2차원 리스트 초기화
    dp = [[0] * (L+1) for _ in range(N+1)]

    # DP 진행
    for i in range(1, N+1):
        for j in range(1, L+1):
            # i번째 재료를 선택하지 않는 경우
            dp[i][j] = dp[i-1][j]
            # i번째 재료를 선택하는 경우
            if j - ingredients[i-1][1] >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1]
                               [j-ingredients[i-1][1]] + ingredients[i-1][0])

    # 결과 출력
    print(f'#{tc} {dp[N][L]}')