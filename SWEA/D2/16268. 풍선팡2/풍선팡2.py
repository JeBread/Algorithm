T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = -21e8
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    sum = 0
    def powder(y, x):
        global sum
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if 0 <= dy < N and 0 <= dx < M:
                sum += arr[dy][dx]
        sum += arr[y][x]

    for i in range(N):
        for j in range(M):
            sum = 0
            powder(i, j)
            if sum > maxV:
                maxV = sum

    print(f'#{tc} {maxV}')