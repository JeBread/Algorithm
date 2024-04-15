T = int(input())
for tc in range(1, T+1):
    N, str1 = input().split()
    ret = bin(int(str1, 16))
    if len(ret[2:]) % 4 == 0: print(f'#{tc} {ret[2:]}')
    else: print(f'#{tc} 0{ret[2:]}')