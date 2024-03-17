T = int(input())
for tc in range(1, T+1):
    lst = input()

    sum = 0
    cnt = 0

    for l in lst:
        if l == 'O':
            cnt += 1
        elif l == 'X':
            cnt = 0

        sum += cnt

    print(sum)