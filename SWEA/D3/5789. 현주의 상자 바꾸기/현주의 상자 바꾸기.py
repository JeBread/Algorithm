T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    lst = [0]*N
    for k in range(1, Q+1):
        L, R = map(int, input().split())
        for i in range(L-1, R):
            lst[i] = k

    print(f'#{tc}', end = ' ')
    print(*lst)