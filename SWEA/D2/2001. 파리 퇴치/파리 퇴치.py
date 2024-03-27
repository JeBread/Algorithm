T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    def getSum(y, x):
        sum = 0
        for i in range(M):
            for j in range(M):
                sum += arr[i+y][j+x]
        return sum

    maxV = -21e8
    ret = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            ret = getSum(i,j)
            if ret > maxV:
                maxV = ret

    print(f'#{test_case} {maxV}')
