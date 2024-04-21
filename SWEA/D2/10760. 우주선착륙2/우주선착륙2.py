T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    hubo = 0
    def findLand(y, x):
        global hubo
        directy = [1,-1,0,0,1,1,-1,-1]
        directx = [0,0,-1,1,-1,1,-1,1]
        cnt = 0
        for i in range(8):
            dy = y + directy[i]
            dx = x + directx[i]
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] < arr[y][x]:
                    cnt += 1
        if cnt >= 4:
            hubo += 1
    for i in range(N):
        for j in range(M):
            findLand(i,j)
    print(f'#{test_case} {hubo}')