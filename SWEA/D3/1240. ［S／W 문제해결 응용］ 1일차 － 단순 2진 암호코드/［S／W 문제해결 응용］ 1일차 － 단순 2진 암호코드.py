T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # arr = [list(map(int, input())) for _ in range(N)]
    arr = [input() for _ in range(N)]
    y = 0
    x = 0
    flag = 0
    code = []
    code1 = []
    num_lst = '0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011'
    # zro, one, two, thr, four = '0001101','0011001','0010011','0111101','0100011'
    # fiv, six, svn, eit, nin = '0110001','0101111','0111011','0110111','0001011'
    for i in range(N):   
        for j in range(M-1, -1, -1):   # 맨 오른쪽 위의 1 찾기
            if arr[i][j] == "1":
                y = i
                x = j
                break
    for j in range(x-55, x+1):
        code.append(arr[y][j])
    for i in range(8):
        code1.append(''.join(code[7*i:7*i + 7]))  # ''.join 학습하기
    ret = []
    for cd1 in code1:
        for i in range(len(num_lst)):
            if cd1 == num_lst[i]:
                ret.append(i)
    sum1 = 0
    sum2 = 0
    ans = 0
    for i in range(len(ret)):
        if i % 2 == 0:
            sum1 += ret[i]
        else:
            sum2 += ret[i]
    if ((sum1 * 3) + sum2) % 10 == 0:
        ans = sum1 + sum2
        flag = 1
    else:
        flag = 0

    if flag == 1:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} 0')