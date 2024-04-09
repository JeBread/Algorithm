T = 10
for test_case in range(1, T + 1):
    N = int(input())
    box = list(map(int, input().split()))

    for i in range(N):
        maxV = -21e8
        minV = 21e8
        for j in range(100):
            if box[j] > maxV:
                maxV = box[j]
                minus1 = j
        for k in range(100):
            if box[k] < minV:
                minV = box[k]
                plus1 = k
        box[plus1] += 1
        box[minus1] -= 1

    maxV = -21e8
    minV = 21e8

    for i in range(100):
        if box[i] > maxV:
            maxV = box[i]
        if box[i] < minV:
            minV = box[i]

    ret = maxV - minV
    print(f'#{test_case} {ret}')