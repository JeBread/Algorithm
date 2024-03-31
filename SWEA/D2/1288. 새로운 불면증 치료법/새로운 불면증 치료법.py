T = int(input())
for tc in range(1,T+1):
    N = int(input())
    DAT = [0]*10
    flag = 0

    def checknum(value):
        global flag
        N_str = str(value)

        for i in range(len(N_str)):
            DAT[int(N_str[i])] += 1

        for i in range(10):
            if DAT[i] == 0:
                return
            else: continue

        flag = 1
        if flag == 1:
            print(f'#{tc} {N_str}')
            return

    while flag == 0:
        for i in range(1, 100):
            checknum(N*i)
            if flag == 1:
                break