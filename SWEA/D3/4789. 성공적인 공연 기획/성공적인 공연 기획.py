T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))
    sum = cnt = 0
    for i in range(len(lst)):
        if lst[i] == 0 and sum < i + 1:
            cnt += 1
            sum += 1
        sum += lst[i]
    print(f'#{tc} {cnt}')