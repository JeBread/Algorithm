T = int(input())
for tc in range(1, T+1):
    str1, str2 = input().split()
    cnt = str1.count(str2)

    ret = len(str1) - (cnt * len(str2)) + cnt

    print(f'#{tc} {ret}')