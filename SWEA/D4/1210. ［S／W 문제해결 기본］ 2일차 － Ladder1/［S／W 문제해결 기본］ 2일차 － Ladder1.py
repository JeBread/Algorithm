for test in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    retx = 0
    used = [[0]*100 for _ in range(100)]
    for j in range(100):
        if arr[99][j] == 2:
            x = j
            y = 99
    directy = [0,0,-1]
    directx = [-1,1,0]
    flag = 1
    while flag:
        if y == 0:
            flag = 0
            retx = x
        for i in range(3):
            dy = y + directy[i]
            dx = x + directx[i]
            if 0 <= dy < 100 and 0 <= dx < 100:
                if arr[dy][dx] == 1 and used[dy][dx] == 0:
                    used[dy][dx] = 1
                    y = dy
                    x = dx

    print(f'#{tc} {retx}')