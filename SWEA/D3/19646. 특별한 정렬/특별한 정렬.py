T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst1 = list(map(int, input().split()))
    lst2 = [0]*N

    for i in range(N):
        lst2[i] = lst1[i]
    ret = []
    lst1.sort()
    lst2.sort(reverse=True)

    for i in range(0, 5):
        ret.append(lst2[i])
        ret.append(lst1[i])

    print(f'#{tc}',end=' ')
    for i in range(10):
        print(ret[i],end=' ')
    print()