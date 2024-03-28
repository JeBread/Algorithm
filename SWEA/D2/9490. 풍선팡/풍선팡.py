T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = -21e8
    directy = [-1,1,0,0]   # y 방향 이동
    directx = [0,0,-1,1]   # x 방향 이동
    sum = 0
    def powder(y, x):   # 날리는 꽃가루 합 구하는 함수
        global sum
        for i in range(4):
            for j in range(1, arr[y][x] + 1):
                dy = y + directy[i] * j
                dx = x + directx[i] * j
                if 0 <= dy < N and 0 <= dx < M: # 범위 설정 !
                    sum += arr[dy][dx]
        sum += arr[y][x]    # 터트린 좌표 지점도 더해줘야 함.

    for i in range(N):
        for j in range(M):
            sum = 0
            powder(i, j)
            if sum > maxV:  # 최대값 구하기
                maxV = sum

    print(f'#{tc} {maxV}')