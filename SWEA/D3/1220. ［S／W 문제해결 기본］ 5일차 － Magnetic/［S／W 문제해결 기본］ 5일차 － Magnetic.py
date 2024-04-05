T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    # 1 is red(N) 아래로 내려감 , 2 is blue(S) 위로 올라감
    # 교착상태 1과 2가 맞닿을 때.
    # 연달아 1과 2가 나올 때   => '12'
    arr = list(zip(*arr))
    arr2 = ''
    for ar in arr:
        for st in ar:
            if st > 0:
                arr2 += str(st)
        arr2 += '_'

    ret = arr2.count('12')
    print(f'#{tc} {ret}')