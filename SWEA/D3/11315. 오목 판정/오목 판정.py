T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    flag = 0

    def garo(y, x):
        global flag
        directx = [-2,-1,0,1,2]
        for i in range(5):
            dx = x + directx[i]
            if 0 <= dx < N:
                if arr[y][dx] != 'o':
                    return
                else: continue
            else: return
        flag = 1

    def sero(y, x):
        global flag
        directy = [-2,-1,0,1,2]
        for i in range(5):
            dy = y + directy[i]
            if 0 <= dy < N:
                if arr[dy][x] != 'o':
                    return
                else: continue
            else: return
        flag = 1

    def rightX_check(y, x):
        global flag
        directy = [-2,-1,0,1,2]
        directx = [2,1,0,-1,-2]
        for i in range(5):
            dy = y + directy[i]
            dx = x + directx[i]
            if 0 <= dy < N and 0 <= dx < N:
                if arr[dy][dx] != 'o':
                    return
                else: continue
            else: return
        flag = 1

    def leftX_check(y, x):
        global flag
        directy = [-2,-1,0,1,2]
        directx = [-2,-1,0,1,2]
        for i in range(5):
            dy = y + directy[i]
            dx = x + directx[i]
            if 0 <= dy < N and 0 <= dx < N:
                if arr[dy][dx] != 'o':
                    return
                else: continue
            else: return
        flag = 1

    for i in range(N):
        for j in range(N):
            garo(i, j)
            sero(i, j)
            rightX_check(i, j)
            leftX_check(i, j)

    if flag:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')