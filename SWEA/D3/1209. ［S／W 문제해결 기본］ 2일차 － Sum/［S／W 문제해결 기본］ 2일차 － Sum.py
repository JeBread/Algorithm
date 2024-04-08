T = 10
for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum = 0
    maxV = -21e8
    def haengsum(arr):
        global sum, maxV
        for i in range(100):
            sum = 0
            for j in range(100):
                sum += arr[i][j]
            if sum > maxV:
                maxV = sum

    def yeolsum(arr):
        global sum, maxV
        for j in range(100):
            sum = 0
            for i in range(100):
                sum += arr[i][j]
            if sum > maxV:
                maxV = sum

    def cross1Sum(arr):
        global sum, maxV
        sum = 0
        for i in range(100):
            for j in range(100):
                if i == j:
                    sum += arr[i][j]
        if sum > maxV:
            maxV = sum

    def cross2Sum(arr):
        global sum, maxV
        sum = 0
        for i in range(100):
            for j in range(100):
                if i == 100 - (j+1):
                    sum += arr[i][j]
        if sum > maxV:
            maxV = sum

    haengsum(arr)
    yeolsum(arr)
    cross1Sum(arr)
    cross2Sum(arr)

    print(f'#{test_case} {maxV}')
