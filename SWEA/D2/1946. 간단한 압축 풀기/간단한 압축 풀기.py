T = int(input())
for tc in range(1, T+1):
    N = int(input())

    lst = []
    for _ in range(N):
        arr = [[0] * 10 for _ in range(6)]
        st1, st2 = input().split()
        num = int(st2)
        st3 = st1 * num
        for st in st3:
            lst.append(st)
    print(f'#{tc}')
    for i in range(len(lst)):
        if i != 0 and i % 10 == 0:
            print()
        print(lst[i],end='')
    print()