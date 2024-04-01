T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    bread_lst = [0] * 11112
    flag = 1

    for i in range(len(people)):
        bread_lst[people[i]] -= 1

    for i in range(1, len(bread_lst)):
        if i % M == 0:
            bread_lst[i] += bread_lst[i-1] + K
        else:
            bread_lst[i] += bread_lst[i - 1]

    for i in range(len(bread_lst)):
        if bread_lst[i] < 0:
            flag = 0
            break

    if flag == 0:
        print(f'#{tc} Impossible')
    else:
        print(f'#{tc} Possible')