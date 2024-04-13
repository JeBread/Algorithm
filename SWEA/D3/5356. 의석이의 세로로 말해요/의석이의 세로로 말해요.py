T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    maxV = -21e8
    print(f'#{tc}', end=' ')
    for row in arr:
        if len(row) > maxV:
            maxV = len(row)
    for row in arr:
        while len(row) < maxV:
            row.append('_')
    for j in range(maxV):
        for i in range(5):
            if arr[i][j] == '_': continue
            else:
                print(arr[i][j],end='')
    print()