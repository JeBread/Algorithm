T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ret = 0
    cnt2 = 0
    # 가로 찾기
    for i in range(N):
        cnt1 = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt1 += 1
            if arr[i][j] == 0:
                cnt1 = 0
            if cnt1 == K and j == N-1:
                ret += 1
            elif cnt1 == K and arr[i][j+1] == 0:
                ret += 1
                cnt1 = 0
    # 세로 찾기
    for j in range(N):
        cnt2 = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt2 += 1
            if arr[i][j] == 0:
                cnt2 = 0
            if cnt2 == K and i == N-1:
                ret += 1
            elif cnt2 == K and arr[i+1][j] == 0:
                ret += 1
                cnt2 = 0

    print(f'#{tc} {ret}')