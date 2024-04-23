T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input()))
    cnt = 1
    maxV = 1

    for i in range(1, N):
        if lst[i] == 1 and lst[i] == lst[i-1]:
            cnt += 1
            if cnt > maxV:
                maxV = cnt
        else:
            cnt = 1

    print(f'#{test_case} {maxV}')