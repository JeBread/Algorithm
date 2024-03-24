N = int(input())
lst = list(map(int, input().split()))
minV, maxV = 21e8, -21e8
for l in lst:
    if l > maxV:
        maxV = l
    if l < minV:
        minV = l
print(f'{minV} {maxV}')