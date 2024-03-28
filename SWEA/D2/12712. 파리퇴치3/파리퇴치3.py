T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    def getsum1(y, x):
        sum = 0
        directy = [-1, 1, 0, 0]
        directx = [0, 0, -1, 1]
        for i in range(4):
            for j in range(1, M):
                dy = y + directy[i] * j
                dx = x + directx[i] * j
                if 0 <= dy < N and 0 <= dx < N:
                    sum += arr[dy][dx]
        sum1 = sum + arr[y][x]
        return sum1


    def getsum2(y, x):
        sum = 0
        crossy = [-1, -1, 1, 1]
        crossx = [-1, 1, -1, 1]
        for i in range(4):
            for j in range(1, M):
                dy = y + crossy[i] * j
                dx = x + crossx[i] * j
                if 0 <= dy < N and 0 <= dx < N:
                    sum += arr[dy][dx]
        sum2 = sum + arr[y][x]
        return sum2


    maxvalue1 = -21e8
    maxvalue2 = -21e8
    for i in range(N):
        for j in range(N):
            result1 = getsum1(i, j)
            result2 = getsum2(i, j)
            if result1 > maxvalue1:
                maxvalue1 = result1
            if result2 > maxvalue2:
                maxvalue2 = result2

    if maxvalue1 > maxvalue2:
        print(f'#{test_case} {maxvalue1}')
    elif maxvalue1 < maxvalue2:
        print(f'#{test_case} {maxvalue2}')