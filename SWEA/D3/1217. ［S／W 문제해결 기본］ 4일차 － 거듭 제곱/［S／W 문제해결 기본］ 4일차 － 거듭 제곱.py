T = 10
for tc in range(1,T+1):
    x = int(input())
    N, M = map(int, input().split())
    ret = N
    def abc(level):
        global ret, N, M
        if level == M:
            return ret
        ret = ret * N
        abc(level+1)
    abc(1)
    print(f'#{tc} {ret}')