standard = [1, 1, 2, 2, 2, 8]
dh = list(map(int, input().split()))
for i in range(6):
    if standard[i] == dh[i]:
        print('0', end=' ')
    else:
        print(standard[i] - dh[i], end=' ')